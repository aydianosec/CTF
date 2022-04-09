import subprocess
from time import *

def digit_nth(elit_prefix):
    times = [[], [], [], [], [], [], [], [], [], []]
    
    for i in range(5):
        for i in range(10):
            proc = subprocess.Popen('./pin_checker', stdin = subprocess.PIPE, stdout = subprocess.DEVNULL)
            
            t1 = perf_counter_ns()
            proc.communicate(elit_prefix.encode("utf-8") + str(i).encode("utf-8") + b"0" * (8 - (len(elit_prefix) + 1)))
            t2 = perf_counter_ns()

            times[i].append(t2 - t1)
            
    for i in range(len(times)):
        times[i] = sum(times[i]) / len(times[i])

    print(f"Average execution times for each digit: {times}")

    i = 0
    n = 0
    for j, m in enumerate(times):
        if m > n:
            n = m
            i = j
    
    return i, n

elit = ""
for i in range(8):
    found = str(digit_nth(elit)[0])
    elit += found
    print(f"The character {i + 1} is {found}")

print("PIN CODE =", elit)