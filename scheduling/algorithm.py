from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, processes: list):
        self.processes = processes

    @abstractmethod
    def schedule(self):
        pass


class FIFO(Algorithm):
    def __init__(self, processes: list):
        super(FIFO, self).__init__(processes)

    def schedule(self) -> list:
        result = self.processes.copy()
        result.sort(key=lambda x: x.arrival_time)
        return result
