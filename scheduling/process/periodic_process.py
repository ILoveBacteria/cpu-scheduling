from abstract_process import AbstractProcess


class PeriodicProcess(AbstractProcess):
    def __init__(self, name: str, burst_time: int, period: int):
        super(PeriodicProcess, self).__init__(name, burst_time)
        self.period = period

    def __repr__(self):
        return f'{self.name} {self.burst_time} {self.period}'

