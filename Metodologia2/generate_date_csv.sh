#!/bin/bash

if [ "$#" -lt 3 ]; then
    echo -e "Error: Please, enter correct arguments as follows:\n $0 <input_csv> <date_dir> <output_final_csv>"
    exit 1
fi

INPUT_CSV=$1
DATE_DIR=$2
OUTPUT_CSV=$3

echo "app_name,num_worker,date,elapsed_time" > "$OUTPUT_CSV"

# Lê o CSV de entrada e processa cada linha
tail -n +2 "$INPUT_CSV" | while IFS=, read -r app_name num_worker elapsed_time; do
    # Encontra o arquivo de data que corresponde ao app_name e ao padrão
    date_file=$(find "$DATE_DIR" -name "NPB-$app_name*.txt" | head -n 1)

    # Verifica se o arquivo de data foi encontrado
    if [[ -f "$date_file" ]]; then
        # Lê uma linha de data do arquivo
        {
            read -r date || date="N/A"  # Define "N/A" caso não tenha mais datas no arquivo
        } < "$date_file"
        
        # Escreve no CSV final com a data incluída
        echo "$app_name,$num_worker,$date,$elapsed_time" >> "$OUTPUT_CSV"
    else
        echo "Warning: Arquivo de data não encontrado para $app_name" >&2
        echo "$app_name,$num_worker,N/A,$elapsed_time" >> "$OUTPUT_CSV"
    fi
done

echo "CSV final gerado em: $OUTPUT_CSV"
