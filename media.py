import re
from collections import defaultdict
import statistics

def calcular_media_e_desvio_tempos(arquivos):
    # Dicionário para armazenar os tempos de cada plataforma
    resultados = defaultdict(lambda: defaultdict(list))

    for arquivo in arquivos:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            
            # Dividir o conteúdo em blocos por plataforma
            plataformas = conteudo.split('Resultados da plataforma: ')[1:]
            
            for plataforma in plataformas:
                # Separar a plataforma e os benchmarks
                linhas = plataforma.strip().splitlines()
                nome_plataforma = linhas[0].strip()

                # Captura os tempos usando regex
                tempos = re.findall(r'Time in seconds\s*=\s*([\d\.]+)', plataforma)

                # Adiciona os tempos à lista correspondente da plataforma
                resultados[nome_plataforma][arquivo].extend(float(t) for t in tempos)

    # Cálculo da média e desvio padrão para cada plataforma e número de threads
    medias = {}
    for plataforma, tempos_dict in resultados.items():
        medias[plataforma] = {}
        for num_threads, tempos in tempos_dict.items():
            media = sum(tempos) / len(tempos)
            desvio_padrao = statistics.stdev(tempos) if len(tempos) > 1 else 0.0  # Desvio padrão
            medias[plataforma][num_threads] = (media, desvio_padrao)
    
    return medias

# Lista de arquivos a serem processados
arquivos = ['threads1.txt', 'threads4.txt', 'threads8.txt', 'threads12.txt']

# Chama a função e imprime as médias e desvios padrão
medias = calcular_media_e_desvio_tempos(arquivos)

for plataforma, tempos in medias.items():
    print(f'Média dos tempos para {plataforma}:')
    for arquivo, (media, desvio_padrao) in tempos.items():
        num_threads = arquivo.split('threads')[1].split('.')[0]  # extrai o número de threads
        print(f'{num_threads} threads = {media:.4f} segundos (Desvio padrão = {desvio_padrao:.4f})')
    print()  # Linha em branco entre plataformas
