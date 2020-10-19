def main():
    result = input().strip().split(' ')
    text = [word if len(word) > 0 else None for word in result]
    print(len(list(filter(lambda x: x, text))))


main()
