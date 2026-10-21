#include <iostream>
#include <string>

// Esqueleto executável. A aquisição, as classes e o controle são trabalho da equipe.
// Preserve a CLI: --dados DIRETORIO --uma-vez (um ciclo, sem esperar).
// Em execução contínua, não recrie ids enquanto a sessão da planta for a mesma.
int main(int argc, char* argv[]) {
    if (argc == 2 && std::string(argv[1]) == "--ajuda") {
        std::cout << "Uso futuro: controlador --dados dados --uma-vez\n";
        return 0;
    }
    std::cout << "CONTROLADOR INCOMPLETO: implemente a aquisicao e a estrategia.\n";
    std::cout << "Consulte docs/CONTRATO.md antes de produzir telemetria ou comandos.\n";
    return 0;
}
