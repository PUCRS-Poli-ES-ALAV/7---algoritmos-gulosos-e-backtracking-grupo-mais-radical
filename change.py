from typing import List

COIN_VALUES = [ 100, 25, 10, 5, 1 ]

def change(n: int) -> List[int]:
    remaining = n
    change = []

    while remaining > 0:
        for cv in COIN_VALUES:
            if remaining >= cv:
                change.append(cv)
                remaining -= cv
                break

    return change


if __name__ == "__main__":
    N = 289
    print(f'Best change for $ {N / 100.0}: {[c / 100.0 for c in change(N)]}')
