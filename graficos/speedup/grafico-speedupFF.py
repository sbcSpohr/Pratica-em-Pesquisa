import numpy as np
import matplotlib.pyplot as plt

jetson_times_1_thread_FF = {
    'bt': 192.68, 'ep': 96.04, 'ft': 21.30, 'cg': 4.46, 'mg': 4.66,
    'is': 2.06, 'sp': 119.60, 'lu': 157.43
}

jetson_times_4_threads_FF = {
    'bt': 55.77, 'ep': 24.40, 'ft': 5.85, 'cg': 3.44, 'mg': 2.22,
    'is': 0.66, 'sp': 55.17, 'lu': 53.20
}

odroid_times_1_thread_FF = {
    'bt': 109.80, 'ep': 84.06, 'ft': 14.31, 'cg': 3.32, 'mg': 3.39,
    'is': 0.70, 'sp': 64.28, 'lu': 114.18
}

odroid_times_4_threads_FF = {
    'bt': 118.12, 'ep': 32.40, 'ft': 9.78, 'cg': 3.02, 'mg': 7.17,
    'is': 0.59, 'sp': 125.36, 'lu': 109.90
}

# Função para calcular o speedup
def calculate_speedup(times_1_thread, times_4_threads):
    return {kernel: times_1_thread[kernel] / times_4_threads[kernel] for kernel in times_1_thread}

# Calcular o speedup para Jetson e Odroid com FF
jetson_speedup_FF = calculate_speedup(jetson_times_1_thread_FF, jetson_times_4_threads_FF)
odroid_speedup_FF = calculate_speedup(odroid_times_1_thread_FF, odroid_times_4_threads_FF)

# Listar os kernels
kernels = list(jetson_speedup_FF.keys())

# Valores de speedup para Jetson e Odroid
jetson_values_FF = list(jetson_speedup_FF.values())
odroid_values_FF = list(odroid_speedup_FF.values())

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(kernels, jetson_values_FF, label='Jetson Nano', marker='o', color='blue')
plt.plot(kernels, odroid_values_FF, label='Odroid', marker='o', color='orange')

# Adicionar título e rótulos
plt.title('Speedup (Jetson Nano vs Odroid) FF', fontsize=14)
plt.xlabel('Kernel', fontsize=12)
plt.ylabel('Speedup', fontsize=12)

# Exibir legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()

