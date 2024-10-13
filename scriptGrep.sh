#!/bin/bash

result_base_dir="$HOME/Faculdade/PEP/TESTES"

platforms=("NPB-OMP" "NPB-FF" "NPB-TBB" "NPB-SER")

benchmarks=("EP" "CG" "MG" "IS" "FT" "BT" "SP" "LU")

output_file="$result_base_dir/benchmark_times.txt"

> "$output_file"

for platform in "${platforms[@]}"; do
    platform_dir="$result_base_dir/result$platform"
 
    echo "Resultados da plataforma: $platform" >> "$output_file"


    for benchmark in "${benchmarks[@]}"; do
        echo "Resultados do benchmark: $benchmark" >> "$output_file"
 
        for run in {1..5}; do

            result_file="$platform_dir/result${benchmark}_S_run${run}.txt"

            if [ -f "$result_file" ]; then
                # Extrai a linha que contém o tempo ("Time in seconds")
                time_line=$(grep "Time in seconds" "$result_file")

                if [ -n "$time_line" ]; then
                    echo "Run $run: $time_line" >> "$output_file"
                else
                    echo "Run $run: Time in seconds não encontrado" >> "$output_file"
                fi
            else
                echo "Run $run: Arquivo de resultado não encontrado" >> "$output_file"
            fi
        done

        echo "" >> "$output_file"
    done
done

echo "Resultados organizados em $output_file"
