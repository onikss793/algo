def draw_stars(size, matrix):
    if size == 3:
        matrix[1][1] = 0
        return

    next_size = size // 3

    draw_stars(next_size, matrix)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                for k in range(1, next_size + 1):
                    row = next_size * i + k
                    column_start = next_size + 1
                    column_end = next_size *

                    matrix[row][column:]

                    print(row, column)
            # for k in range(next_size):
            #     row = next_size * i + k
            #     column = next_size * j
            #     matrix[row][column:next_size*(j+1)] = matrix[k][:next_size]


def main():
    N = int(input())

    matrix = [[1 for _ in range(N)] for _ in range(N)]

    draw_stars(N, matrix)

    for row in matrix:
        for data in row:
            print('*', end='') if data else print(' ', end='')
        print('')


main()

# # 별 찍는 재귀 함수
# def draw_star(n):
#     global Map
#
#     if n == 3:
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]
#         return
#
#     a = n // 3
#
#     draw_star(a)
#
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]  # 핵심 아이디어
#
#
# N = int(input())
#
# # 메인 데이터 선언
# Map = [[0 for i in range(N)] for i in range(N)]
#
# draw_star(N)
#
# for i in Map:
#     for j in i:
#         if j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
