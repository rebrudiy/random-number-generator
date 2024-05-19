from first_generator import generate as gen1
from second_genarator import generate as gen2
from datetime import datetime
import matplotlib.pyplot as plt

sizes = [10, int(1e3), int(1e6)]
alg1_time = []
alg2_time = []

for i in sizes:
    now = datetime.now()
    seed = now.microsecond
    gen1(seed, i)
    new_now = datetime.now()
    alg1_time.append((new_now - now).microseconds)

for i in sizes:
    now = datetime.now()
    seed = now.microsecond
    gen2(seed, i)
    new_now = datetime.now()
    alg2_time.append((new_now - now).microseconds)

plt.plot(sizes, alg1_time, color='r', label='1')
plt.plot(sizes, alg2_time, color='g', label='2')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("len")
plt.ylabel("time")
plt.legend()

# To load the display window
plt.show()
