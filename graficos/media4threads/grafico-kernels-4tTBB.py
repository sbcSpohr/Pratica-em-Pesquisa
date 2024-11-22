import numpy as np
import matplotlib.pyplot as plt

# Dados do TBB com 4 threads
jetson_nano_times_4_threads = {
    'bt': 55.84,
    'ep': 24.00,
    'ft': 5.97,
    'cg': 3.34,
    'mg': 2.16,
    'is': 0.57,
    'sp': 55.05,
    'lu': 52.84
}

odroid_times_4_threads = {
    'bt': 38.82,
    'ep': 8.55,
    'ft': 5.91,
    'cg': 1.58,
    'mg': 2.02,
    'is': 0.30,
    'sp': 79.29,
    'lu': 67.23
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
ax.set_title('Comparação de Tempo de Execução por Kernel (4 threads) TBB')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()
