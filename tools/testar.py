import argparse
from pathlib import Path
import sys
import unittest

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
sys.path.insert(0, str(RAIZ / "tests"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--etapa", choices=["00", "01", "02", "03"], required=True)
    args = parser.parse_args()
    etapa = int(args.etapa)
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.discover(str(RAIZ / "tests"), pattern="test_planta.py"))
    if etapa >= 1:
        from test_controlador import suite as controlador
        suite.addTests(controlador(etapa))
    if etapa >= 3:
        suite.addTests(unittest.defaultTestLoader.discover(str(RAIZ / "tests"), pattern="test_supervisor.py"))
    # Casos de domínio escritos pela equipe são repetidos em todas as etapas.
    suite.addTests(unittest.defaultTestLoader.discover(str(RAIZ / "tests"), pattern="autorais_*.py"))
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
