PYTHON ?= python3
CXX ?= g++
CXXFLAGS := -std=c++17 -Wall -Wextra -Werror -pedantic
ETAPA ?= 00

.PHONY: build test planta controlador supervisor
build: build/controlador

build/controlador: controlador/main.cpp
	mkdir -p build
	$(CXX) $(CXXFLAGS) controlador/main.cpp -o $@

test: build
	$(PYTHON) tools/testar.py --etapa $(ETAPA)

planta:
	$(PYTHON) -m planta.simulador --dados dados

controlador: build
	./build/controlador --dados dados --uma-vez

supervisor:
	$(PYTHON) -m streamlit run supervisor/app.py --browser.gatherUsageStats=false
