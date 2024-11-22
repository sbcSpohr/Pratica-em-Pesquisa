#!/bin/bash

platforms=("NPB-OMP" "NPB-FF" "NPB-TBB" "NPB-SER")
kernels=("ep" "cg" "mg" "is" "ft" "bt" "sp" "lu")
classes=("A")

BASE_DIR="$HOME/Faculdade/PEP/TESTES-NPB"
runs=5
threads=(1 2 3 4)

output_file="$BASE_DIR/benchmark_times.txt"

> "$output_file"

for platform in "${platforms[@]}"; do
    platform_result_dir="$BASE_DIR/result$platform"

    rm -rf "$platform_result_dir"
    mkdir -p "$platform_result_dir"

    if [ -d "$platform" ]; then
        cd "$platform" || exit
    else
        echo "Diretório $platform não encontrado." >> "$output_file"
        continue
    fi

    for thread in "${threads[@]}"; do

        case $platform in
            NPB-OMP)
                export OMP_NUM_THREADS=$thread
                ;;
            NPB-FF)
                export FF_NUM_THREADS=$thread
                ;;
            NPB-TBB)
                export TBB_NUM_THREADS=$thread
                ;;
        esac

        for kernel in "${kernels[@]}"; do

            for class in "${classes[@]}"; do
                for run in $(seq 1 $runs); do
                    result_file="$platform_result_dir/result${kernel}_${class}_threads${thread}_run${run}.txt"
                    >"$result_file"

                    make "$kernel" CLASS="$class"
                    if [ $? -eq 0 ]; then
                        ./bin/${kernel}.${class} >> "$result_file"
                    else
                        echo "Erro ao compilar $kernel para $class" >> "$platform_result_dir/error.log.txt"
                    fi
                done
            done
        done

        echo "Resultados da plataforma: $platform com $thread threads" >> "$output_file"

        for kernel in "${kernels[@]}"; do
            echo "Resultados do kernel: $kernel com $thread threads" >> "$output_file"

            for run in $(seq 1 $runs); do
                result_file="$platform_result_dir/result${kernel}_S_threads${thread}_run${run}.txt"

                if [ -f "$result_file" ]; then
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

    cd .. || exit
done

echo "Resultados organizados em $output_file"
