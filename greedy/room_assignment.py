def main():
    N = int(input())

    nodes = [tuple(map(int, input().split(" "))) for _ in range(N)]
    nodes.sort(key=lambda node: (node[1], node[0]))

    count = 1
    end_time = nodes[0][1]

    for start, end in nodes:
        if start >= end_time:
            count += 1
            end_time = end

    print(count)


main()
