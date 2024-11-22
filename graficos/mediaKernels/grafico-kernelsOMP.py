import numpy as np
import matplotlib.pyplot as plt

kernels = ['bt', 'ep', 'ft', 'cg', 'mg', 'is', 'sp', 'lu']

jetson_nano_times = {
    'bt': [189.63, 98.89, 69.73, 55.78],
    'ep': [94.88, 47.82, 31.50, 24.04],
    'ft': [21.00, 10.85, 7.49, 5.75],
    'cg': [4.36, 3.50, 3.50, 3.31],
    'mg': [4.55, 2.81, 2.30, 2.17],
    'is': [1.92, 0.96, 0.66, 0.52],
    'sp': [118.32, 71.04, 59.08, 54.98],
    'lu': [156.55, 83.60, 63.12, 53.20]
}

odroid_times = {
    'bt': [109.29, 60.65, 45.67, 38.82],
    'ep': [33.84, 16.96, 11.31, 8.50],
    'ft': [13.83, 9.24, 6.33, 5.62],
    'cg': [2.98, 2.06, 1.68, 1.49],
    'mg': [3.26, 2.15, 2.00, 1.99],
    'is': [0.66, 0.38, 0.32, 0.30],
    'sp': [64.32, 63.66, 75.10, 79.63],
    'lu': [116.98, 78.99, 69.43, 66.45]
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
ax.set_title('Comparação de Tempo de Execução Médio por Kernel (OMP)')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()
