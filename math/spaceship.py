test_cases = int(input())
tests = []

for _ in range(test_cases):
    x, y = map(int, input().split(' '))

    distance = y - x  # 이동해야 하는 거리
    moved_count = 0  # 이동 횟수
    possible_moving_distance = 1  # 이동횟수 기준 움직일 수 있는 최대 거리
    total_moved_distance = 0  # 총 이동한 거리

    while total_moved_distance < distance:  # 총 이동한 거리가 이동해야 하는 거리보다 작다면... 만약 커지면 횟수 만족할 것임
        moved_count += 1  # 총 이동 거리가 아직 불만족이므로 이동을 한번 더 한다
        total_moved_distance += possible_moving_distance
        # 한번 더 이동했으므로 총 이동 거리에 이동 가능한 최대 거리를 더 하여 갱신한다

        if moved_count % 2 == 0:  # 규칙에 따라 만약 총 이동 거리가 짝수라면,
            possible_moving_distance += 1  # 다음 이동 가능 최대 거리는 1 늘어난다
    # while 문이 끝나게 되면, "총 이동 거리" >= "이동해야 하는 거리" 가 된다
    # 갱신된 이동 횟수가 답이 될 것이다
    tests.append(moved_count)

[print(test) for test in tests]
