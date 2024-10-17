from matplotlib import pyplot as plt

num_threads = [1, 2, 3]

bzip2_times = [123.59, 102.70, 96.12]
lane_times = [173.95, 142.48, 132.63]
ferret_times = [45.90, 32.36, 27.80]
person_times = [706.19, 559.93, 516.64]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(num_threads, bzip2_times, marker='o', label='BZIP2', color='blue')
plt.title("Latência média BZIP2")
plt.xlabel("Threads")
plt.ylabel("Latência")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, max(bzip2_times) * 1.1)
plt.xticks(num_threads)
plt.grid()
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(num_threads, lane_times, marker='o', label='LANE', color='orange')
plt.title("Latência média LANE")
plt.xlabel("Threads")
plt.ylabel("Latência")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, max(lane_times) * 1.1)
plt.xticks(num_threads)
plt.grid()
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(num_threads, ferret_times, marker='o', label='FERRET', color='green')
plt.title("Latência média FERRET")
plt.xlabel("Threads")
plt.ylabel("Latência")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, max(ferret_times) * 1.1)
plt.xticks(num_threads)
plt.grid()
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(num_threads, person_times, marker='o', label='PERSON', color='red')
plt.title("Latência média PERSON")
plt.xlabel("Threads")
plt.ylabel("Latência")
plt.xlim(min(num_threads), max(num_threads))
plt.ylim(0, max(person_times) * 1.1)
plt.xticks(num_threads)
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
