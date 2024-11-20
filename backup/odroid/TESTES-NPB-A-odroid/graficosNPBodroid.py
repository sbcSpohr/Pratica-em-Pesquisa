from matplotlib import pyplot as plt

num_threads = [1, 2, 3, 4]

OMP_means = [43.14, 29.26, 26.48, 25.35]
FF_means = [51.11, 100.38, 73.93, 61.82]
TBB_means = [43.23, 29.22, 26.97, 25.46]
SER_means = [40.64, 40.59, 40.76, 40.87]

plt.figure(figsize=(10, 8))

#------------------------------------------------------------------------

#OMP
plt.subplot(2, 2, 1)
plt.plot(num_threads, OMP_means, marker='o', label='NPB-OMP', color='blue')
plt.title("NPB-OMP")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)
plt.grid()

#------------------------------------------------------------------------

#FF
plt.subplot(2, 2, 2)
plt.plot(num_threads, FF_means, marker='o', label='NPB-FF', color='orange')
plt.title("NPB-FF")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 120)
plt.grid()

#------------------------------------------------------------------------

#TBB
plt.subplot(2, 2, 3)
plt.plot(num_threads, TBB_means, marker='o', label='NPB-TBB', color='green')
plt.title("NPB-TBB")
plt.xlabel("Threads")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)
plt.grid()

#------------------------------------------------------------------------

#SER
plt.subplot(2, 2, 4)
plt.plot(num_threads, SER_means, marker='o', label='NPB-SER', color='red')
plt.title("NPB-SER")
plt.xlabel("Execuções")
plt.ylabel("Tempo médio (s)")
plt.xticks(num_threads)
plt.ylim(0, 80)
plt.grid()

#------------------------------------------------------------------------

plt.tight_layout()
plt.show()
