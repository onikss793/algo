def main():
    sugar = int(input())

    count = 0

    while sugar >= 0:
        if sugar % 5 == 0:
            count += (sugar // 5)
            print(count)
            break
        else:
            sugar -= 3
            count += 1

    else:
        print(-1)


main()

