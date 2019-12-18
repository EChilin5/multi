import multiprocessing
import time

start = time.perf_counter()


def do_something():
   print("Sleep 1 second")
   time.sleep(1)
   print('Done sleeping')

proccess = []

for _ in range


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')