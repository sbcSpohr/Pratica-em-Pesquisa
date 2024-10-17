from matplotlib import pyplot as plt

num_threads = [1, 2, 3, 4, 5, 6]

#------------------------------------------------------------------------

# OMP
OMP_times = [0.15, 0.07, 0.05, 0.04, 0.04, 0.04]

plt.subplot(2, 2, 1)
plt.plot(num_threads, OMP_times, marker='o', label='NPB-OMP', color='blue')
plt.title("Média 'Time in seconds' NPB-OMP")
plt.xlabel("Threads")
plt.ylabel("Segundos")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, 0.16)
plt.xticks(num_threads)
plt.grid()

#------------------------------------------------------------------------

# FF
FF_times = [0.15, 0.10, 0.09, 0.07, 0.06, 0.04]

plt.subplot(2, 2, 2)
plt.plot(num_threads, FF_times, marker='o', label='NPB-FF', color='orange')
plt.title("Média 'Time in seconds' NPB-FF")
plt.xlabel("Threads")
plt.ylabel("Segundos")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, 0.16)
plt.xticks(num_threads)
plt.grid()

#------------------------------------------------------------------------

# TBB
TBB_times = [0.15, 0.08, 0.05, 0.04, 0.04, 0.03]

plt.subplot(2, 2, 3)
plt.plot(num_threads, TBB_times, marker='o', label='NPB-TBB', color='green')
plt.title("Média 'Time in seconds' NPB-TBB")
plt.xlabel("Threads")
plt.ylabel("Segundos")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, 0.16)
plt.xticks(num_threads)
plt.grid()

#------------------------------------------------------------------------

# SER
SER_runs = [1, 2, 3, 4, 5, 6]
SER_times = [0.15, 0.15, 0.15, 0.15, 0.15, 0.15]

plt.subplot(2, 2, 4)
plt.plot(SER_runs, SER_times, marker='o', label='NPB-SER', color='red')
plt.title("Média 'Time in seconds' NPB-SER")
plt.xlabel("Execuções")
plt.ylabel("Segundos")
plt.xlim(min(SER_runs), max(SER_runs))
plt.ylim(0, 0.16)
plt.xticks(SER_runs)
plt.grid()

#------------------------------------------------------------------------

plt.tight_layout()
plt.show()
