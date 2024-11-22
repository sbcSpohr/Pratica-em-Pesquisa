import numpy as np
import matplotlib.pyplot as plt

kernels = ['bt', 'ep', 'ft', 'cg', 'mg', 'is', 'sp', 'lu']

jetson_nano_times = {
    'bt': [193.18, 99.59, 70.20, 55.84],
    'ep': [94.99, 47.74, 31.39, 24.00],
    'ft': [21.97, 11.22, 7.65, 5.97],
    'cg': [4.57, 3.53, 3.47, 3.34],
    'mg': [4.40, 2.69, 2.89, 2.16],
    'is': [2.12, 1.06, 0.73, 0.57],
    'sp': [120.12, 70.83, 59.10, 55.05],
    'lu': [151.93, 80.97, 60.71, 52.84]
}

odroid_times = {
    'bt': [110.63, 61.21, 46.04, 38.82],
    'ep': [33.90, 16.99, 11.29, 8.55],
    'ft': [14.35, 9.42, 6.50, 5.91],
    'cg': [3.06, 2.08, 1.77, 1.58],
    'mg': [3.29, 2.15, 2.53, 2.02],
    'is': [0.70, 0.39, 0.32, 0.30],
    'sp': [64.53, 64.08, 75.49, 79.29],
    'lu': [115.38, 77.44, 71.85, 79.29]
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
ax.set_title('Comparação de Tempo de Execução Médio por Kernel (TBB)')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()
