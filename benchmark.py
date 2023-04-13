import time


def benchmark(f, print_res, *fargs):
    time_start = time.time_ns()
    (res, num_iter) = f(*fargs)
    time_elapsed = (time.time_ns() - time_start) / 1e6

    if print_res:
        print(f'{f.__name__}{fargs} = {res} ({time_elapsed} ms, {num_iter} iters)')
    else:
        print(f'{f.__name__}{fargs} ({time_elapsed} ms, {num_iter} iters)')


if __name__ == "__main__":
    benchmark(lambda x: (x + 1, 1), 2)
