import numpy as np
import matplotlib.pyplot as plt

jetson_times_1_thread_TBB = {
    'bt': 193.18, 'ep': 94.99, 'ft': 21.97, 'cg': 4.57, 'mg': 4.40,
    'is': 2.12, 'sp': 120.12, 'lu': 151.93
}

jetson_times_4_threads_TBB = {
    'bt': 55.84, 'ep': 24.00, 'ft': 5.97, 'cg': 3.34, 'mg': 2.16,
    'is': 0.57, 'sp': 55.05, 'lu': 52.84
}

odroid_times_1_thread_TBB = {
    'bt': 110.63, 'ep': 33.90, 'ft': 14.35, 'cg': 3.06, 'mg': 3.29,
    'is': 0.70, 'sp': 64.53, 'lu': 115.38
}

odroid_times_4_threads_TBB = {
    'bt': 38.82, 'ep': 8.55, 'ft': 5.91, 'cg': 1.58, 'mg': 2.02,
    'is': 0.30, 'sp': 79.29, 'lu': 67.23
}

# Função para calcular o speedup
def calculate_speedup(times_1_thread, times_4_threads):
    return {kernel: times_1_thread[kernel] / times_4_threads[kernel] for kernel in times_1_thread}

# Calcular o speedup para Jetson e Odroid com NPB-TBB
jetson_speedup_TBB = calculate_speedup(jetson_times_1_thread_TBB, jetson_times_4_threads_TBB)
odroid_speedup_TBB = calculate_speedup(odroid_times_1_thread_TBB, odroid_times_4_threads_TBB)

# Listar os kernels
kernels = list(jetson_speedup_TBB.keys())

# Valores de speedup para Jetson e Odroid
jetson_values_TBB = list(jetson_speedup_TBB.values())
odroid_values_TBB = list(odroid_speedup_TBB.values())

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(kernels, jetson_values_TBB, label='Jetson Nano', marker='o', color='blue')
plt.plot(kernels, odroid_values_TBB, label='Odroid', marker='o', color='orange')

# Adicionar título e rótulos
plt.title('Speedup (Jetson Nano vs Odroid) TBB', fontsize=14)
plt.xlabel('Kernel', fontsize=12)
plt.ylabel('Speedup', fontsize=12)

# Exibir legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
