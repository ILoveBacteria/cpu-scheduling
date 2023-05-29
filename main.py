from scheduling.algorithm import *
from scheduling.process import *


def read_processes() -> list:
    processes = []
    for _ in range(n):
        data = input().strip().split(' ')
        processes.append(Process(data[0], *map(int, data[1:])))
    return processes


def edf():
    processes = []
    for _ in range(n):
        data = input().strip().split(' ')
        processes.append(PeriodicProcess(data[0], *map(int, data[1:])))
    print(EDF(processes).schedule())


if __name__ == '__main__':
    print('1- FIFO\n2- RR\n3- EDF')
    a = int(input('Choose an algorithm: '))
    n = int(input('Number of processes: '))

    result = None
    if a == 1:
        result = FIFO(read_processes()).schedule()
    elif a == 2:
        q = int(input('Quantum time: '))
        result = RR(read_processes(), q)
    elif a == 3:
        edf()

