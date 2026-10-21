# Operação do starter

Este documento trata da infraestrutura pública; enunciado, rubrica e solução
de referência ficam fora deste repositório. Não publicar soluções das extensões.

## Base e branches

A main inicial usa `ETAPA_ATUAL=00`. O build e os testes da planta passam; o
controlador e a tela informam que estão incompletos. A CI mapeia explicitamente
as branches para etapas e rejeita nomes `projeto/**` sem correspondência.
Cada PR deve atualizar `ETAPA_ATUAL` para manter o contrato após o merge na main.
Não usar `pull_request_target`, segredos ou permissões de escrita.

Para verificar a distribuição:

```bash
make test ETAPA=00
make test ETAPA=01
```

O primeiro passa; o segundo falha nos comportamentos ainda não implementados.
Não afrouxar o contrato para obter um verde inicial nas etapas autorais.

## Uso em aula de arquivos

1. Gerar três ciclos finitos e abrir `planta.json` com `python3 -m json.tool`.
2. Identificar envelope, lista de leituras, unidades e campos de confirmação.
3. Reiniciar e comparar sessões, sem confundir reinício com ciclo novo da sessão anterior.
4. Usar o comissionador com a planta contínua para observar atuação no ciclo seguinte.
5. Corromper um comando em diretório de teste e observar diagnóstico e atuação zerada.

Nenhuma dessas demonstrações implementa a política de controle do estudante.
Os exemplos das aulas podem usar a planta isoladamente antes de iniciar o projeto.

## Limites da automação

Os contratos são verificações formativas, não um mecanismo inviolável de autoria.
A suíte verifica aquisição, ida/volta de comando e apresentação básica. O docente
deve ler as estratégias, os testes autorais e a persistência, além de conferir o
diff dos testes e do workflow. Na defesa, cada aluno deve explicar todo o fluxo,
inclusive código proposto por IA, bibliotecas usadas e decisões que não implementou sozinho.

Para outro domínio, negociar o contrato e fixtures; preservar a configuração
original permite executar as regressões da planta fornecida. Não reintroduzir
parâmetros derivados de matrícula.

O projeto usa um fork separado do starter da Parte 1. Alunos podem reaproveitar
suas próprias classes com atribuição e revisão, sem substituir a planta nem
confundir os comandos e workflows dos dois repositórios.
