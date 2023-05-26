from algorithm import Algorithm


class FIFO(Algorithm):
    def __init__(self, processes: list):
        super(FIFO, self).__init__(processes)

    def schedule(self) -> list:
        result = self.processes.copy()
        result.sort(key=lambda x: x.arrival_time)
        return result
