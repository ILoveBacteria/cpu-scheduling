from abstract_process import AbstractProcess


class Process(AbstractProcess):
    def __init__(self, name: str, burst_time: int, arrival_time: int):
        super(Process, self).__init__(name, burst_time)
        self.arrival_time = arrival_time

    def __repr__(self):
        return f'{self.name} {self.burst_time} {self.arrival_time}'
