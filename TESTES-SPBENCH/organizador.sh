#!/bin/bash


DIR_DADOS="$HOME/Faculdade/PEP/SPBench/jetson"

DIR_DESTINO="$HOME/Faculdade/PEP/TESTES-SPBENCH"

mv "$DIR_DADOS"/*dat "$DIR_DESTINO"

echo "Arquivos movidos"
