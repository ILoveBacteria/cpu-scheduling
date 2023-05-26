from abc import ABC, abstractmethod
from .process import ScheduledProcess


class Algorithm(ABC):
    def __init__(self, processes: list):
        self.processes = processes.copy()

    @abstractmethod
    def schedule(self):
        pass


class FIFO(Algorithm):
    def __init__(self, processes: list):
        super(FIFO, self).__init__(processes)

    def schedule(self) -> list:
        self.processes.sort(key=lambda x: x.arrival_time)
        result = []
        time = 0
        for i in self.processes:
            result.append(ScheduledProcess(i.name, time, time + i.burst_time))
            time += i.burst_time
        return result
