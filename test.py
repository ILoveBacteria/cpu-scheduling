import unittest
from scheduling.process import Process, ScheduledProcess
from scheduling.algorithm import FIFO, RR


class MyTestCase(unittest.TestCase):
    def test_fifo(self):
        processes = [
            Process('P0', 4, 0),
            Process('P1', 3, 2),
            Process('P2', 7, 5),
        ]
        expected = [
            ScheduledProcess('P0', 0, 4),
            ScheduledProcess('P1', 4, 7),
            ScheduledProcess('P2', 7, 14),
        ]
        self.assertListEqual(expected, FIFO(processes).schedule())

    def test_round_robin(self):
        processes = [
            Process('P0', 5, 0),
            Process('P1', 3, 1),
            Process('P2', 1, 2),
            Process('P3', 2, 3),
            Process('P4', 3, 4),
        ]
        expected = [
            ScheduledProcess('P0', 0, 2),
            ScheduledProcess('P1', 2, 4),
            ScheduledProcess('P2', 4, 5),
            ScheduledProcess('P0', 5, 7),
            ScheduledProcess('P3', 7, 9),
            ScheduledProcess('P4', 9, 11),
            ScheduledProcess('P1', 11, 12),
            ScheduledProcess('P0', 12, 13),
            ScheduledProcess('P4', 13, 14),
        ]
        self.assertListEqual(expected, RR(processes, 2).schedule())


if __name__ == '__main__':
    unittest.main()
