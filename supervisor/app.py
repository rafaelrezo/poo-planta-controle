"""Ponto de partida da interface; o controlador é responsável pelas decisões."""

import os
from pathlib import Path

import streamlit as st


def main():
    dados = Path(os.environ.get("POO_DADOS", "dados"))
    st.title("Supervisório da planta didática")
    st.caption(f"Diretório de integração: {dados}")
    st.info("Supervisório incompleto: implemente a leitura da telemetria do controlador.")
    # Próximos incrementos: tabela, histórico, alarmes e diagnóstico de dados antigos.
    # Não use planta.json como atalho: consuma telemetria.json produzida pelo C++.


if __name__ == "__main__":
    main()
