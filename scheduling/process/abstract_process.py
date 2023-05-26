from abc import ABC, abstractmethod


class AbstractProcess(ABC):
    def __init__(self, name: str, burst_time: int):
        self.name = name
        self.burst_time = burst_time

    @abstractmethod
    def __repr__(self):
        pass
