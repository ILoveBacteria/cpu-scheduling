from abc import ABC, abstractmethod


class Algorithm(ABC):
    def __init__(self, processes: list):
        self.processes = processes

    @abstractmethod
    def schedule(self):
        pass
