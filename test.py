import unittest
from scheduling.process import Process, ScheduledProcess
from scheduling.algorithm import FIFO


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


if __name__ == '__main__':
    unittest.main()
