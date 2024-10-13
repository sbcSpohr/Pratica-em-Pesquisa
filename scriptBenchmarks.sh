#!/bin/bash

platforms=("NPB-OMP" "NPB-FF" "NPB-TBB" "NPB-SER")
benchmarks=("EP" "CG" "MG" "IS" "FT" "BT" "SP" "LU")
classes=("S")

result_base_dir="$HOME/Faculdade/PEP/TESTES"
runs=5  # Número de execuções

for platform in "${platforms[@]}"; do
    platform_result_dir="$result_base_dir/result${platform}"

    # Limpar diretório de resultados antes de cada execução
    rm -rf "$platform_result_dir"
    mkdir -p "$platform_result_dir"

    if [ -d "$platform" ]; then
        cd "$platform" || exit
    else
        echo "Ocorreu algum erro" >> "$platform_result_dir/error.log.txt"
        continue
    fi

    for benchmark in "${benchmarks[@]}"; do
        benchmark_lower=$(echo "$benchmark" | tr '[:upper:]' '[:lower:]')

        for class in "${classes[@]}"; do
            for run in $(seq 1 $runs); do
                result_file="$platform_result_dir/result${benchmark}_${class}_run${run}.txt"

                >"$result_file"

                make "$benchmark" CLASS="$class"

                if [ $? -eq 0 ]; then
                    ./bin/${benchmark_lower}.${class} >> "$result_file"
                else
                    echo "Erro ao compilar $benchmark para $class" >> "$platform_result_dir/error.log.txt"
                fi
            done
        done
    done
    cd .. || exit
done
