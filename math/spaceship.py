def is_odd(num):
    return num % 2 != 0


def main(tests):
    for (x, y) in tests:
        distance = y - x
        count = 0
        move = 1
        move_total = 0

        while move_total < distance:
            count += 1
            move_total += move

            if is_odd(count):
                move += 1

        print(count)


test_cases = int(input())
tests = []

for _ in range(test_cases):
    x, y = map(int, input().split(' '))

    tests.append((x, y))

main(tests)
