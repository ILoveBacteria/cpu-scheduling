from abc import ABC, abstractmethod
from .process import ScheduledProcess, Process


class Algorithm(ABC):
    def __init__(self, processes: list):
        if len(processes) == 0:
            raise ValueError('List is empty')
        self.processes = processes.copy()
        self.processes.sort(key=lambda x: x.arrival_time)

    @abstractmethod
    def schedule(self):
        pass


class FIFO(Algorithm):
    def __init__(self, processes: list):
        super(FIFO, self).__init__(processes)

    def schedule(self) -> list:
        result = []
        time = 0
        for i in self.processes:
            result.append(ScheduledProcess(i.name, time, time + i.burst_time))
            time += i.burst_time
        return result


class RR(Algorithm):
    def __init__(self, processes: list, quantum_time: int):
        super(RR, self).__init__(processes)
        self.quantum_time = quantum_time

    def schedule(self) -> list:
        waiting_queue = self.processes.copy()
        result = []
        rr_queue = []
        self.__first_arrivals(rr_queue, waiting_queue)
        current_time = rr_queue[0].arrival_time

        while len(rr_queue) > 0:
            pick_process = rr_queue.pop()
            current_time, scheduled_process = self.__run_process(current_time, pick_process)
            result.append(scheduled_process)
            self.__check_arrivals(rr_queue, waiting_queue, current_time)
            # Check if the process has been finished or not
            if pick_process.burst_time > 0:
                rr_queue.insert(0, pick_process)

        return result

    def __check_arrivals(self, rr_queue: list, waiting_queue: list, current_time: int):
        for _ in range(len(waiting_queue)):
            if len(waiting_queue) > 0 and waiting_queue[0].arrival_time <= current_time:
                rr_queue.insert(0, waiting_queue.pop(0))

    def __first_arrivals(self, rr_queue: list, waiting_queue: list):
        first_arrival_time = waiting_queue[0].arrival_time
        for i in list(filter(lambda x: x.arrival_time == first_arrival_time, waiting_queue)):
            rr_queue.insert(0, i)
            waiting_queue.pop(0)

    def __run_process(self, current_time: int, process: Process) -> (int, ScheduledProcess):
        burst = process.burst_time if process.burst_time < self.quantum_time else self.quantum_time
        end = current_time + burst
        process.burst_time -= burst
        return end, ScheduledProcess(process.name, current_time, end)
