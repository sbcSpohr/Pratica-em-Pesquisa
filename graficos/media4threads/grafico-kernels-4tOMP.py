import numpy as np
import matplotlib.pyplot as plt

jetson_nano_times_4_threads = {
    'bt': 55.77,
    'ep': 24.04,
    'ft': 5.85,
    'cg': 3.44,
    'mg': 2.22,
    'is': 0.66,
    'sp': 55.17,
    'lu': 53.20
}

odroid_times_4_threads = {
    'bt': 38.82,
    'ep': 8.50,
    'ft': 5.62,
    'cg': 1.49,
    'mg': 1.99,
    'is': 0.30,
    'sp': 79.63,
    'lu': 66.45
}

kernels = list(jetson_nano_times_4_threads.keys())

jetson_nano_values = list(jetson_nano_times_4_threads.values())
odroid_values = list(odroid_times_4_threads.values())

bar_width = 0.35
index = np.arange(len(kernels))

fig, ax = plt.subplots(figsize=(12, 8))

bar1 = ax.bar(index - bar_width / 2, jetson_nano_values, bar_width, label='Jetson Nano (4 threads)', color='blue')
bar2 = ax.bar(index + bar_width / 2, odroid_values, bar_width, label='Odroid (4 threads)', color='orange')

ax.set_xlabel('Kernel')
ax.set_ylabel('Tempo de execução (s)')
ax.set_title('Comparação de Tempo de Execução por Kernel (4 threads) OMP')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()

