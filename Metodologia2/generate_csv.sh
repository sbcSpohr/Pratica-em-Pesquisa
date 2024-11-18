#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo -e "Error: Please, enter correct arguments as follows:\n $0 <log_dir> <output_csv>";
    exit 1;
fi

OUTPUT_CSV=$2
LOG_DIR=$1

echo "app_name,num_worker,elapsed_time" > "$OUTPUT_CSV"

for platform in resultNPB-FF resultNPB-OMP resultNPB-SER resultNPB-TBB; do

    app_name=${platform#resultNPB-}

    for file in "$LOG_DIR/$platform"/*.txt; do
    
        if [[ -f "$file" ]]; then

            num_worker=$(grep "Total threads" "$file" | awk '{print $4}')

            elapsed_time=$(grep -oP "Time in seconds\s*=\s*\K[0-9\.]+" "$file")

            if [[ -n $num_worker && -n $elapsed_time ]]; then
                echo "$app_name,$num_worker,$elapsed_time" >> "$OUTPUT_CSV"
            else
                echo "Warning Faltando informacoes: $file"
            fi
        else
            echo "Warning: Arquivo nao encontrado: $file"
        fi
    done
done

echo "CSV gerado em: $OUTPUT_CSV"
