import numpy as np
import matplotlib.pyplot as plt


jetson_times_1_thread = {
    'bt': 189.63, 'ep': 94.88, 'ft': 21.00, 'cg': 4.36, 'mg': 4.55,
    'is': 1.92, 'sp': 118.32, 'lu': 156.55
}

jetson_times_4_threads = {
    'bt': 55.78, 'ep': 24.04, 'ft': 5.75, 'cg': 3.31, 'mg': 2.17,
    'is': 0.52, 'sp': 54.98, 'lu': 53.20
}

odroid_times_1_thread = {
    'bt': 109.29, 'ep': 33.84, 'ft': 13.83, 'cg': 2.98, 'mg': 3.26,
    'is': 0.66, 'sp': 64.32, 'lu': 116.98
}

odroid_times_4_threads = {
    'bt': 38.82, 'ep': 8.50, 'ft': 5.62, 'cg': 1.49, 'mg': 1.99,
    'is': 0.30, 'sp': 79.63, 'lu': 66.45
}

# Calcular speedup (S) = Tempo com 1 thread / Tempo com 4 threads
def calculate_speedup(times_1_thread, times_4_threads):
    return {kernel: times_1_thread[kernel] / times_4_threads[kernel] for kernel in times_1_thread}

# Calcular speedup para Jetson e Odroid
jetson_speedup = calculate_speedup(jetson_times_1_thread, jetson_times_4_threads)
odroid_speedup = calculate_speedup(odroid_times_1_thread, odroid_times_4_threads)

# Listar os kernels
kernels = list(jetson_speedup.keys())

# Valores de speedup para Jetson e Odroid
jetson_values = list(jetson_speedup.values())
odroid_values = list(odroid_speedup.values())

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(kernels, jetson_values, label='Jetson Nano', marker='o', color='blue')
plt.plot(kernels, odroid_values, label='Odroid', marker='o', color='orange')

# Adicionar título e rótulos
plt.title('Speedup (Jetson Nano vs Odroid) OMP', fontsize=14)
plt.xlabel('Kernel', fontsize=12)
plt.ylabel('Speedup', fontsize=12)

# Exibir legenda
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
