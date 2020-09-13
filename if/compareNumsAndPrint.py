A, B = map(int, input().split())

print(['==', '<>'[A > B]][len({A, B}) - 1])
