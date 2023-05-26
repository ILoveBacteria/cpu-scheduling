from abc import ABC, abstractmethod


class AbstractProcess(ABC):
    def __init__(self, name: str, burst_time: int):
        self.name = name
        self.burst_time = burst_time

    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, o: object) -> bool:
        if issubclass(o.__class__, AbstractProcess) and isinstance(self, o.__class__):
            return self.name == o.name
        return False


class Process(AbstractProcess):
    def __init__(self, name: str, burst_time: int, arrival_time: int):
        super(Process, self).__init__(name, burst_time)
        self.arrival_time = arrival_time

    def __repr__(self):
        return f'{self.name} {self.burst_time} {self.arrival_time}'


class PeriodicProcess(AbstractProcess):
    def __init__(self, name: str, burst_time: int, period: int):
        super(PeriodicProcess, self).__init__(name, burst_time)
        self.period = period

    def __repr__(self):
        return f'{self.name} {self.burst_time} {self.period}'
