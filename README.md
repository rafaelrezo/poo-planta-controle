# Planta, controlador e supervisório — starter de POO

Repositório-base público: `rafaelrezo/poo-planta-controle`.
Faça fork para desenvolver seu projeto. A planta de tanque é fornecida pronta;
o controlador C++ e o Streamlit são esqueletos executáveis com comportamento
incompleto identificado. A planta também pode ser usada isoladamente em aulas
de arquivos, JSON, validação e tratamento de erros.

## 1. O que já funciona

| Parte | Estado inicial | Responsabilidade |
|---|---|---|
| `planta/simulador.py` | pronta, testada, biblioteca padrão Python | gerar leituras e aplicar comandos |
| `controlador/main.cpp` | compila e informa que está incompleto | aquisição e controle a desenvolver |
| `supervisor/app.py` | abre uma página inicial | supervisão a desenvolver |
| `tools/enviar_comando.py` | pronto | teste manual de atuação, sem política automática |
| `docs/CONTRATO.md` | fornecido | formato, autoria dos arquivos e regras de troca |

Não há algoritmo automático de controle fornecido. Tanque, nível e temperatura
são um ponto de partida; outro contexto pode ser escolhido e documentado.
O enunciado e os critérios de avaliação são distribuídos separadamente pelo docente.

## 2. Fork e requisitos

Use Python 3.12+, compilador C++17 e GNU Make (Linux, WSL ou ambiente equivalente).
Primeiro faça fork pela interface do GitHub. Substitua `SEU_USUARIO` abaixo:

```bash
git clone https://github.com/SEU_USUARIO/poo-planta-controle.git
cd poo-planta-controle
git remote -v
git switch -c projeto/00-ambiente
make test ETAPA=00
```

Mantenha somente `origin`, apontando para seu fork. Abra todas as PRs da branch
para a `main` do próprio fork. Não adicione `upstream` nem abra PR contra a base
do professor. Preserve os commits iniciais e acrescente o trabalho da equipe.

O comando compila o C++ com avisos tratados como erros e roda os testes da planta.
Resultado esperado: `OK`. A etapa 00 confirma a infraestrutura, não o projeto pronto.

## 3. Experimentar arquivos antes de implementar o controle

Na raiz do fork, execute:

```bash
python3 -m planta.simulador --dados dados --passos 3 --intervalo 0 --seed 7
python3 -m json.tool dados/planta.json
make controlador
```

A saída da planta termina em `ciclo=3`; o JSON contém duas leituras, com nível e
temperatura. Sem comando, os atuadores ficam em zero. O C++ mostra
`CONTROLADOR INCOMPLETO`. O arquivo é um snapshot substituído a cada ciclo;
não é um arquivo JSONL nem um histórico de todas as aquisições.

Para observar atuação, execute a planta continuamente em um terminal:

```bash
make planta
```

Em outro terminal, na mesma raiz, envie um comando manual e inspecione o arquivo
depois do próximo ciclo:

```bash
python3 tools/enviar_comando.py --dados dados --bomba 100 --aquecedor 50
python3 -m json.tool dados/planta.json
```

Confirme `ultimo_comando` e as novas atuações. Sem comandos novos, a atuação
expira após 5 ciclos. Não execute o comissionador e o controlador automático
simultaneamente: o arquivo de comando deve ter um único escritor. A planta pode
ser encerrada com Ctrl+C. Cada reinício gera outra sessão e invalida comandos antigos.

## 4. Abrir o esqueleto Streamlit

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make supervisor PYTHON=.venv/bin/python
```

A página inicial tem título, diretório e aviso de implementação incompleta.
A equipe desenvolverá a leitura de `telemetria.json`, sem acesso direto à planta.
A variável `POO_DADOS` pode escolher outro diretório para testes e demonstração.

## 5. Incrementos e testes cumulativos

Integre cada PR antes de abrir a branch seguinte. Parta da main atualizada e
altere `ETAPA_ATUAL` no mesmo incremento, para que a CI da main mantenha as verificações.

| Branch | `ETAPA_ATUAL` | Comando local e da CI | Comportamento verificado |
|---|---|---|---|
| `projeto/00-ambiente` | `00` | `make test ETAPA=00` | planta e build inicial |
| `projeto/01-aquisicao` | `01` | `make test ETAPA=01` | anteriores + aquisição e falhas de entrada |
| `projeto/02-controle` | `02` | `make test ETAPA=02` | anteriores + comando e confirmação da planta |
| `projeto/03-supervisor` | `03` | `make test ETAPA=03` | anteriores + tabela e diagnósticos na tela |
| `projeto/04-entrega` | `03` | `make test ETAPA=03` | regressão completa e casos autorais |

Nas etapas 03, instale `requirements.txt` e use
`make test ETAPA=03 PYTHON=.venv/bin/python`; o ambiente ativo da CI já tem as
dependências. `AppTest` verifica a tela sem iniciar servidor nem navegador.

As etapas 01–03 falham inicialmente porque o aluno ainda não implementou os
comportamentos. A mensagem `Falta telemetria.json` orienta a primeira aquisição.
O controlador deve aceitar `--dados DIRETORIO --uma-vez`; `--uma-vez` processa uma
aquisição e encerra. A equipe também implementa o laço contínuo para a demonstração.

Fluxo de uma etapa, após integrar a anterior:

```bash
git switch main
git pull --ff-only origin main
git switch -c projeto/01-aquisicao
make test ETAPA=01
```

Depois de implementar, atualizar `ETAPA_ATUAL` e validar, faça commits pequenos,
push para `origin` e abra a PR. A PR inclui saída local, link da CI do commit,
explicação técnica, UML quando mudar e registro do uso de IA.

## 6. Testes que a equipe acrescenta

Crie `tests/autorais_*.py` com `unittest`. O runner repete esses casos em todas
as etapas. Se acrescentar classes C++, inclua sua compilação e seus testes no
Makefile; não remova as regressões existentes. Verifique as estratégias com
entradas conhecidas, valores de fronteira, leituras inválidas e cenário escolhido.

Os testes fornecidos verificam contratos observáveis e integração básica. Eles
não provam a correção do controle, a aplicação de padrões, a qualidade da UML,
a persistência nem o entendimento da equipe. Essas evidências dependem dos
testes autorais, da inspeção do diff e da defesa. Workflows e testes são visíveis
e editáveis no fork; CI verde não substitui a revisão técnica.

## 7. Padrões e organização

O controlador concentra as decisões de controle; serialização, arquivos e tela
ficam em fronteiras próprias. Justifique os padrões a partir do problema.

| Técnica/Padrão | Melhor uso | Esforço | Entregável | Limitação |
|---|---|---|---|---|
| Strategy | trocar a política mantendo a aquisição | médio | interface e políticas testadas | exige justificar as variações |
| Command | representar atuações e seus ids | médio | solicitação verificável | não garante aplicação pela planta |
| Repository | separar histórico e apresentação | médio | persistência testável | exige contrato de consulta |
| Observer | notificar mudanças e alarmes | médio | notificações desacopladas | pode duplicar eventos se mal usado |

Comece com Strategy quando variar a política; use Command se a solicitação de
atuação precisar de identidade e rastreio. Para histórico, considere Repository.
O esqueleto não determina sua hierarquia de classes.

## 8. Diagnóstico

- Arquivo ausente: execute a planta e confirme o diretório de trabalho.
- Comando rejeitado: confira sessão, id, chaves e percentuais no contrato.
- Atuadores voltam a zero: a validade é contada em ciclos; gere comandos novos
  somente após novas aquisições e respeite o intervalo da planta.
- Dados repetidos: sessão/ciclo identificam o snapshot; não duplique o histórico.
- Biblioteca JSON C++ ausente: documente sua escolha e instalação no README e CI.

Consulte [o contrato completo](docs/CONTRATO.md) antes de alterar a comunicação.
