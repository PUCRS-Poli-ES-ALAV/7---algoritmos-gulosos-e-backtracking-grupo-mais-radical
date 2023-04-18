import sys
from typing import List, Tuple

from benchmark import benchmark


def schedule_greedy(intervals: List[Tuple[int, int]]) -> Tuple[List[int], int]:
    # Force the first interval to be selected.
    intervals = [(0, intervals[0][0] - 1)] + intervals
    res = []
    num_iter = 0
    i = 0

    for k in range(1, len(intervals)):
        num_iter += 1

        if intervals[k][0] > intervals[i][1]:
            res.append(k - 1)
            i = k

    return (res, num_iter)


if __name__ == "__main__":
    intervals = sorted([
        (4, 8),
        (6, 7),
        (13, 14),
        (4, 5),
        (2, 4),
        (6, 9),
        (7, 10),
        (9, 11),
        (1, 6),
        (3, 13),
        (9, 12)
    ], key=lambda x: x[1])

    benchmark(schedule_greedy, True, intervals)
