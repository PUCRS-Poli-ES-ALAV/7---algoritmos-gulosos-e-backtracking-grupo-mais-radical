from typing import List

from benchmark import benchmark


def change(n: int, coin_values: List[int]) -> List[int]:
    num_iter = 0
    remaining = n
    change = []

    while remaining > 0:
        for cv in coin_values:
            num_iter += 1

            if remaining >= cv:
                change.append(cv)
                remaining -= cv
                break

    return (change, num_iter)


if __name__ == "__main__":
    COIN_VALUES = [ 100, 25, 10, 5, 1 ]
    nums = [ 289, 34810, 8790100, 200312000 ]

    for n in nums:
        benchmark(change, False, n, COIN_VALUES)
