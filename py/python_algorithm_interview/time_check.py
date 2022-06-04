import time
from types import FunctionType


def time_check(func: FunctionType):
    start_time = time.time()

    func()

    end_time = time.time()

    print(f'{(end_time - start_time):.6f} took')
