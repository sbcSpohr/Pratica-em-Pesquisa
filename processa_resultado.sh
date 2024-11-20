#!/bin/bash

base_dir="." 
output_file="benchmark_times.txt"
debug_file="resultados_debug.txt"
> "$output_file"

platforms=("NPB-OMP" "NPB-FF" "NPB-TBB" "NPB-SER")

for platform in "${platforms[@]}"; do
    for threads in {1..4}; do
        echo "Resultados da plataforma: ${platform} com ${threads} threads" >> "$output_file"
        echo "Resultados da plataforma: ${platform} com ${threads} threads" >> "$debug_file"
        for kernel in bt ep ft cg mg is sp lu; do
            result_file="${base_dir}/result${platform}/result${kernel}_A_threads${threads}_run1.txt"
            echo "Resultados do kernel: ${kernel} com ${threads} threads" >> "$output_file"
            echo "Procurando arquivo: ${result_file}" >> "$debug_file"

            if [[ -f "$result_file" ]]; then

                time_line=$(grep "Time in seconds" "$result_file")
                if [[ -n "$time_line" ]]; then
                    echo "Run 1: ${time_line}" >> "$output_file"
                    echo "Run 1: ${time_line}" >> "$debug_file"
                else
                    echo "Run 1: Resultado não encontrado no arquivo" >> "$output_file"
                    echo "Run 1: Resultado não encontrado no arquivo" >> "$debug_file"
                fi
            else
                echo "Run 1: Arquivo de resultado não encontrado" >> "$output_file"
                echo "Run 1: Arquivo de resultado não encontrado" >> "$debug_file"
            fi
        done
    done
done
