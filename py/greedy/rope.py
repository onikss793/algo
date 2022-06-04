def main():
    N = int(input())
    ropes = sorted([int(input()) for _ in range(N)], reverse=True)
    results = []

    for index, weight in enumerate(ropes):
        results.append((index + 1) * weight)

    print(max(results))


main()
