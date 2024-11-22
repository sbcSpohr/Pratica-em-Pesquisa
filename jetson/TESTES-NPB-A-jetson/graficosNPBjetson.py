from matplotlib import pyplot as plt

num_threads = [1, 2, 3, 4]

OMP_means = [73.90, 39.93, 29.67, 24.97]
FF_means = [74.78, 40.46, 30.08, 25.09]
TBB_means = [74.16, 39.70, 29.52, 24.97]
SER_means = [73.99, 73.70, 73.79, 73.91]

plt.figure(figsize=(10, 8))

#------------------------------------------------------------------------

#OMP
plt.subplot(2, 2, 1)
plt.plot(num_threads, OMP_means, marker='o', label='NPB-OMP', color='blue')
plt.title("NPB-OMP")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)  # Definindo o limite máximo do eixo y como 80
plt.grid()

#------------------------------------------------------------------------

#FF
plt.subplot(2, 2, 2)
plt.plot(num_threads, FF_means, marker='o', label='NPB-FF', color='orange')
plt.title("NPB-FF")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)  # Definindo o limite máximo do eixo y como 80
plt.grid()

#------------------------------------------------------------------------

#TBB
plt.subplot(2, 2, 3)
plt.plot(num_threads, TBB_means, marker='o', label='NPB-TBB', color='green')
plt.title("NPB-TBB")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)  # Definindo o limite máximo do eixo y como 80
plt.grid()

#------------------------------------------------------------------------

#SER
plt.subplot(2, 2, 4)
plt.plot(num_threads, SER_means, marker='o', label='NPB-SER', color='red')
plt.title("NPB-SER")
plt.xlabel("Execuções")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)  # Definindo o limite máximo do eixo y como 80
plt.grid()

#------------------------------------------------------------------------

plt.tight_layout()
plt.show()
