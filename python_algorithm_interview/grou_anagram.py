from collections import defaultdict
from pprint import pprint


def main():
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

    anagrams = defaultdict(list)

    for word in words:
        anagrams[''.join(sorted(word))].append(word)

    result = [sorted(a) for a in anagrams.values()]
    pprint(result, indent=4)

    return

# expected: [
# 	['ate', 'eat', 'tea'],
# 	['nat', 'tan'],
# 	['bat']
# ]


if __name__ == '__main__':
    main()
