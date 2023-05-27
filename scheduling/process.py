from abc import ABC, abstractmethod


class AbstractProcess(ABC):
    def __init__(self, name: str, burst_time: int):
        self.name = name
        self.burst_time = burst_time

    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, o: object) -> bool:
        return issubclass(o.__class__, AbstractProcess) and isinstance(self, o.__class__) and self.name == o.name


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
        self.deadline = period

    def __repr__(self):
        return f'{self.name} {self.burst_time} {self.period}'


class ScheduledProcess:
    def __init__(self, name: str, start: int, end: int):
        self.name = name
        self.start = start
        self.end = end

    def __repr__(self):
        return f'{self.name} {self.start}->{self.end}'

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ScheduledProcess) and self.name == o.name and self.start == o.start and self.end == o.end
