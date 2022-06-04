"""
ATM 1대 있다. 
N명의 사람들이 줄을 서있다. 
i번 사람이 돈을 인출하는데 걸리는 시간은 Pi 분이다.

돈을 뽑을 때 걸리는 시간 P에 따라서 모든 사람이 돈을 인출하는데 걸리는 시간 중 최솟값을 구하시오

첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

5
3 1 4 3 2

32
"""


def main():
    _ = int(input())
    p = list(map(int, input().split((' '))))
    p.sort()

    result = 0

    for n in range(len(p)):
        result += sum(p[:n+1])

    print(result)


main()
