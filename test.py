import unittest
from scheduling.process import Process, ScheduledProcess, PeriodicProcess
from scheduling.algorithm import FIFO, RR, EDF


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

    def test_edf(self):
        processes = [
            PeriodicProcess('P0', 15, 30),
            PeriodicProcess('P1', 15, 40),
            PeriodicProcess('P2', 5, 50),
        ]
        expected = [
            ScheduledProcess('P0', 0, 15),
            ScheduledProcess('P1', 15, 30),
            ScheduledProcess('P2', 30, 35),
            ScheduledProcess('P0', 35, 50),
            ScheduledProcess('P1', 50, 65),
            ScheduledProcess('P0', 65, 80),
            ScheduledProcess('P2', 80, 85),
            ScheduledProcess('P0', 85, 100),
            ScheduledProcess('P1', 100, 115),
            ScheduledProcess('P2', 115, 120),
        ]
        self.assertListEqual(expected, EDF(processes).schedule())


if __name__ == '__main__':
    unittest.main()
