import numpy as np
import matplotlib.pyplot as plt

kernels = ['bt', 'ep', 'ft', 'cg', 'mg', 'is', 'sp', 'lu']

jetson_nano_times = {
    'bt': [182.05, 178.69, 180.17, 181.60],
    'ep': [95.02, 94.79, 94.56, 94.78],
    'ft': [21.23, 21.55, 21.30, 21.43],
    'cg': [4.46, 4.38, 4.48, 4.45],
    'mg': [4.32, 4.52, 4.45, 4.32],
    'is': [1.92, 1.97, 1.95, 1.92],
    'sp': [132.08, 131.99, 131.80, 132.53],
    'lu': [150.85, 151.71, 151.64, 150.23]
}

odroid_times = {
    'bt': [101.47, 101.52, 101.73, 101.51],
    'ep': [33.99, 33.95, 33.94, 33.94],
    'ft': [14.09, 14.41, 14.12, 14.12],
    'cg': [2.99, 3.05, 2.99, 2.99],
    'mg': [3.23, 3.25, 3.21, 3.22],
    'is': [0.64, 0.64, 0.64, 0.64],
    'sp': [73.24, 72.71, 72.52, 74.58],
    'lu': [95.50, 95.19, 96.90, 95.92]
}

def calculate_mean(times):
    return np.mean(times)

jetson_nano_means = {key: calculate_mean(value) for key, value in jetson_nano_times.items()}
odroid_means = {key: calculate_mean(value) for key, value in odroid_times.items()}

kernels = list(jetson_nano_means.keys())

jetson_nano_means_values = list(jetson_nano_means.values())
odroid_means_values = list(odroid_means.values())

bar_width = 0.35

index = np.arange(len(kernels))

fig, ax = plt.subplots(figsize=(12, 8))

bar1 = ax.bar(index - bar_width / 2, jetson_nano_means_values, bar_width, label='Jetson Nano (Média)', color='blue')
bar2 = ax.bar(index + bar_width / 2, odroid_means_values, bar_width, label='Odroid (Média)', color='orange')

ax.set_xlabel('Kernel')
ax.set_ylabel('Tempo médio (s)')
ax.set_title('Comparação de Tempo de Execução Médio por Kernel (SER)')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()
