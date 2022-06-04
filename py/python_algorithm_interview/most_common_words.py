import collections
import re


def main():
    paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
    banned = ['hit']

    words = [
        word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
        if not word in banned
    ]

    count_dict = collections.defaultdict(int)

    for word in words:
        count_dict[word] += 1

    print(max(count_dict, key=count_dict.get))

    # expected: 'ball'
    pass


if __name__ == '__main__':
    main()
