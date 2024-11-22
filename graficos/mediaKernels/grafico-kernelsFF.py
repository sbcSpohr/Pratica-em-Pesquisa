import numpy as np
import matplotlib.pyplot as plt

kernels = ['bt', 'ep', 'ft', 'cg', 'mg', 'is', 'sp', 'lu']

jetson_nano_times = {
    'bt': [192.68, 100.59, 70.61, 55.77],
    'ep': [96.04, 47.92, 31.52, 24.40],
    'ft': [21.30, 11.01, 7.52, 5.85],
    'cg': [4.46, 3.82, 3.61, 3.44],
    'mg': [4.66, 3.00, 2.46, 2.22],
    'is': [2.06, 1.09, 0.73, 0.66],
    'sp': [119.60, 72.68, 60.75, 55.17],
    'lu': [157.43, 83.56, 63.45, 53.20]
}

odroid_times = {
    'bt': [109.80, 219.86, 152.45, 118.12],
    'ep': [84.06, 56.12, 43.13, 32.40],
    'ft': [14.31, 17.45, 12.49, 9.78],
    'cg': [3.32, 3.23, 3.07, 3.02],
    'mg': [3.39, 2.24, 4.94, 7.17],
    'is': [0.70, 1.11, 0.73, 0.59],
    'sp': [64.28, 176.08, 139.45, 125.36],
    'lu': [114.18, 185.56, 133.50, 109.90]
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
ax.set_title('Comparação de Tempo de Execução Médio por Kernel (FF)')
ax.set_xticks(index)
ax.set_xticklabels(kernels)
ax.legend()

plt.tight_layout()
plt.show()
