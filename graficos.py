from matplotlib import pyplot as plt

num_threads = [1, 4, 8, 12]

#------------------------------------------------------------------------

#OMP
OMP_times = [0.0218, 0.0398, 0.0320, 0.0223]

plt.subplot(2, 2, 1)

plt.plot(num_threads, OMP_times, marker='o')

plt.title("Média 'Time in seconds' NPB-OMP (X: threads, Y: segundos)")

plt.xlim(min(num_threads), max(num_threads))
plt.ylim(min(OMP_times), max(OMP_times))

plt.xticks(num_threads)
plt.yticks([0.02, 0.025, 0.03, 0.035, 0.04, 0.045])

plt.grid()

#------------------------------------------------------------------------

#FF
FF_times = [0.1507, 0.0650, 0.0420, 0.0380]

plt.subplot(2, 2, 2)

plt.plot(num_threads, FF_times, marker='o')

plt.title("Média 'Time in seconds' NPB-FF (X: threads, Y: segundos)")

plt.xlim(min(num_threads), max(num_threads))
plt.ylim(min(FF_times), max(FF_times))

plt.xticks(num_threads)
plt.yticks([0.035, 0.060, 0.085, 0.110, 0.135, 0.160])

plt.grid()

#------------------------------------------------------------------------

#TBB

TBB_times = [0.1487, 0.0413, 0.0280, 0.0280]

plt.subplot(2, 2, 3)

plt.plot(num_threads, TBB_times, marker='o')

plt.title("Média 'Time in seconds' NPB-TBB (X: threads, Y: segundos)")

plt.xlim(min(num_threads), max(num_threads))
plt.ylim(min(TBB_times), max(TBB_times))

plt.xticks(num_threads)
plt.yticks([0.025, 0.055, 0.085, 0.115, 0.145, 0.175])

plt.grid()

#------------------------------------------------------------------------

#SER
SER_runs = [1, 2, 3, 4]
SER_times = [0.1495, 0.1492, 0.1495, 0.1497]

plt.subplot(2, 2, 4)

plt.plot(SER_runs, SER_times, marker='o')

plt.title("Média 'Time in seconds' NPB-SER (X: execuções, Y: segundos)")

plt.xlim(min(SER_runs), max(SER_runs))
plt.ylim(min(SER_times), max(SER_times))

plt.xticks(SER_runs)
plt.yticks([0.1490, 0.1492, 0.1494, 0.1496, 0.1498, 0.150])

plt.grid()

#------------------------------------------------------------------------

plt.show()
