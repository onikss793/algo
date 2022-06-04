def main():
    num_1, num_2 = input().strip().split(' ')
    num_1_reversed = int(num_1[::-1])
    num_2_reversed = int(num_2[::-1])

    result = num_1_reversed if num_1_reversed > num_2_reversed else num_2_reversed

    print(result)


main()
