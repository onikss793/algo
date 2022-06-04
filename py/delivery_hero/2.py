# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    seperated_sentence = seperate_lines(S)

    results = []

    for sentence in seperated_sentence:
        args = divide_args(sentence)

        if check(args):
            file_name = args[2]
            results.append(file_name)

    shortest_name = min(results, key=lambda name: len(name))

    return f"{len(shortest_name)}"


def check(args: list):
    user = args[0]
    permissions = args[1]
    name = args[2]
    ext = name.split(".")[-1]

    return user == "root" and permissions[:2] == "r-" and ext in ["doc", "xls", "pdf"]


def divide_args(sentence):
    sent = sentence.split(" ")
    result = []

    for sent in sentence.split(" "):
        if len(sent):
            result.append(sent)

    return result


def seperate_lines(sentence):
    result = []

    for sent in sentence.split("\n"):
        if len(sent):
            result.append(sent)

    return result


T = """
  root r-x delete-this.xls
  root r-- bug-report.pdf
  root r-- doc.xls
  root r-- podcast.flac
 alice r-- system.xls
  root --x invoices.pdf
 admin rwx SETUP.PY
"""

result = solution(T)
print(result)
