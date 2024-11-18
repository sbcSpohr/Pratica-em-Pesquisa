import os
import pandas as pd

directory = 'MEDIAS'

def calcular_media_pandas(prefixo):
    latencies = {1: [], 2: [], 3: []}

    for filename in os.listdir(directory):
        if filename.startswith(prefixo):
            file_path = os.path.join(directory, filename)

            df = pd.read_csv(file_path, delim_whitespace=True)

            for thread in [1, 2, 3]:
                latency_values = df[df['Thread'] == thread]['Average_exec_time']
                latencies[thread].extend(latency_values)

    media_resultados = {thread: (pd.Series(latencies[thread]).mean() if latencies[thread] else None) for thread in latencies}
    return media_resultados

media_bzip2 = calcular_media_pandas('bzip2')
media_lane = calcular_media_pandas('lane')
media_ferret = calcular_media_pandas('ferret')
media_person = calcular_media_pandas('person')

print("Média de Average_exec_time para bzip2:")
for thread in media_bzip2:
    print(f"  Thread {thread}: {media_bzip2[thread]}")

print("\nMédia de Average_exec_time para lane:")
for thread in media_lane:
    print(f"  Thread {thread}: {media_lane[thread]}")

print("\nMédia de Average_exec_time para ferret")
for thread in media_ferret:
    print(f"  Thread {thread}: {media_ferret[thread]}")

print("\nMédia de Average_exec_time para person")
for thread in media_person:
    print(f"  Thread {thread}: {media_person[thread]}")
