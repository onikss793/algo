import time
import re
from collections import deque


def is_palindrome_slice(text=None):
    if not text:
        text = 'A man, a plan, a canal: Panama'

    strs = text.lower()
    strs = re.sub('[^a-z0-9]', '', strs)

    if strs != strs[::-1]:
        print('false')
        return
    print('true')
    return


def is_palindrome_list(text=None):
    if not text:
        text = 'A man, a plan, a canal: Panama'

    strs = []

    for char in text:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            print('false')
            break

    print('true')
    return


def is_palindrome_deque(text=None):
    if not text:
        text = 'A man, a plan, a canal: Panama'

    strs: deque = deque()

    for char in text:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            print('false')
            break

    print('true')
    return


if __name__ == '__main__':
    start_time = time.time()
    is_palindrome_deque()
    end_time = time.time()

    print(f'{(end_time - start_time):.6f} took for deque')

    start_time = time.time()
    is_palindrome_list()
    end_time = time.time()
    print(f'{(end_time - start_time):.6f} took for list')

    start_time = time.time()
    is_palindrome_slice()
    end_time = time.time()
    print(f'{(end_time - start_time):.6f} took for slice')
