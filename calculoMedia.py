import re
from statistics import stdev

def ler_resultados(arquivo):
    resultados = {}
    
    with open(arquivo, 'r') as f:
        plataforma_atual = None
        threads_atual = None
        kernel_atual = None
        
        for linha in f:
            linha = linha.strip()  # Remove espaços em branco nas extremidades

            # Verifica se é uma linha de plataforma
            match_plataforma = re.match(r'Resultados da plataforma: (\S+) com (\d+) threads', linha)
            if match_plataforma:
                plataforma_atual = match_plataforma.group(1)
                threads_atual = int(match_plataforma.group(2))
                if plataforma_atual not in resultados:
                    resultados[plataforma_atual] = {}
                if threads_atual not in resultados[plataforma_atual]:
                    resultados[plataforma_atual][threads_atual] = {}
                continue
            
            # Verifica se é uma linha de kernel
            match_kernel = re.match(r'Resultados do kernel: (\S+) com (\d+) threads', linha)
            if match_kernel:
                kernel_atual = match_kernel.group(1)
                if kernel_atual not in resultados[plataforma_atual][threads_atual]:
                    resultados[plataforma_atual][threads_atual][kernel_atual] = []
                continue
            
            # Verifica se é uma linha de tempo
            match_tempo = re.match(r'Run \d+:  Time in seconds =\s+([\d.]+)', linha)
            if match_tempo:
                tempo = float(match_tempo.group(1))
                resultados[plataforma_atual][threads_atual][kernel_atual].append(tempo)

    return resultados

def calcular_media_e_desvio(resultados):
    estatisticas = {}
    
    for plataforma, threads in resultados.items():
        estatisticas[plataforma] = {}
        for thread, kernels in threads.items():
            todos_tempos = []
            for kernel, tempos in kernels.items():
                todos_tempos.extend(tempos)  # Adiciona todos os tempos de todos os kernels
            
            if todos_tempos:
                media_thread = sum(todos_tempos) / len(todos_tempos)  # Média
                desvio_thread = stdev(todos_tempos)  # Desvio padrão
            else:
                media_thread = 0.0
                desvio_thread = 0.0
            
            estatisticas[plataforma][thread] = {
                "media": media_thread,
                "desvio": desvio_thread
            }
            
    return estatisticas

# Chame a função passando o nome do arquivo
resultados = ler_resultados('benchmark_times.txt')
estatisticas = calcular_media_e_desvio(resultados)

# Para visualizar os resultados
for plataforma, threads in estatisticas.items():
    print(f"Média e Desvio Padrão para a Plataforma: {plataforma}")
    for thread, stats in threads.items():
        print(f"  Threads: {thread}, Média: {stats['media']:.2f}, Desvio Padrão: {stats['desvio']:.2f}")

