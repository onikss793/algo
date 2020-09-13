# N 개의 정수
# 최소, 최대값
import sys


def get_array():
    array = map(int, sys.stdin.readline().rstrip().split(' '))

    return array


def main():
    input()
    array = get_array()
    sorted_array = sorted(array)

    print(sorted_array[0], sorted_array[-1])


main()
