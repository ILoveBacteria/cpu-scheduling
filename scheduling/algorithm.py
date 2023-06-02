import copy
from abc import ABC, abstractmethod
from .process import ScheduledProcess, Process, PeriodicProcess


class Algorithm(ABC):
    def __init__(self, processes: list):
        if len(processes) == 0:
            raise ValueError('List is empty')
        self.processes = processes.copy()

    @abstractmethod
    def schedule(self) -> list:
        pass


class FIFS(Algorithm):
    def __init__(self, processes: list):
        super(FIFS, self).__init__(processes)
        self.processes.sort(key=lambda x: x.arrival_time)

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
        self.processes.sort(key=lambda x: x.arrival_time)
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


class EDF(Algorithm):
    def __init__(self, processes):
        super(EDF, self).__init__(processes)

    def schedule(self):
        waiting_queue = copy.deepcopy(self.processes)
        result = []
        periods = self.__all_periods()
        current_time = 0
        paused_process = None

        while len(periods) > 0:
            # Go next period if the waiting queue is empty
            if len(waiting_queue) == 0:
                current_time = periods.pop(0)
                self.__add_new_period_process(current_time, waiting_queue)

            next_period = periods[0]
            picked_process = self.__pick_process(waiting_queue)
            scheduled_process = self.__run_process(picked_process, current_time, next_period)
            current_time = scheduled_process.end
            # If this process was the resume of the last one, just change the end time
            if paused_process and paused_process == picked_process:
                result[-1].end = scheduled_process.end
            else:
                result.append(scheduled_process)
            # Check if reached next period
            if scheduled_process.end == next_period:
                self.__add_new_period_process(periods.pop(0), waiting_queue)
            # Check if the process finished or if not finished add it again to the queue
            if picked_process.burst_time == 0:
                paused_process = None
            else:
                if picked_process.name in map(lambda x: x.name, waiting_queue):     # miss
                    paused_process = None
                else:
                    # Insert it to the first(higher priority with the same deadlines).
                    waiting_queue.insert(0, picked_process)
                    paused_process = picked_process

        return result

    def __run_process(self, process: Process, current_period: int, next_period: int) -> ScheduledProcess:
        burst = min(next_period - current_period, process.burst_time)
        scheduled = ScheduledProcess(process.name, current_period, burst + current_period)
        process.burst_time -= burst
        return scheduled

    def __pick_process(self, waiting_queue: list) -> Process:
        minimum_i = 0
        for i, v in enumerate(waiting_queue):
            if v.deadline < waiting_queue[minimum_i].deadline:
                minimum_i = i
        return waiting_queue.pop(minimum_i)

    def __add_new_period_process(self, period: int, waiting_queue: list):
        for i in self.processes:
            if period % i.period == 0:
                new_process = PeriodicProcess(i.name, i.burst_time, i.period)
                new_process.deadline = period + new_process.period
                waiting_queue.append(new_process)

    def __all_periods(self) -> list:
        periods = set()
        for i in self.processes:
            for j in range(1, 120 // i.period + 1):
                periods.add(j * i.period)
        periods = list(periods)
        periods.sort()
        return periods
