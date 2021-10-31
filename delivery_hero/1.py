# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    splited_sentence = split_sentence(S)
    duplication_map = {}
    emails = []

    for full_name in splited_sentence:
        first_name, last_name = get_name(full_name)

        email = convert_to_email(first_name, last_name)

        if email in emails:
            value = duplication_map.get(email) if email in duplication_map else 1
            duplication_map[email] = value+1
            emails.append(convert_dulication(email, value+1))
            continue
        
        emails.append(email)

    result = "; ".join(emails)
    print(result)
    pass


def split_sentence(sentence):
    return sentence.split("; ")


def get_name(full_name):
    names = full_name.split(" ")

    if len(names) == 2:
        return filter_name(names[0]), filter_name(names[1])
    if len(names) > 2:
        return filter_name(names[0]), filter_name(names[-1])


def filter_name(name: str):
    filtered_name = name.replace("-", "").replace(" ", "").replace("'", "").lower()

    if len(filtered_name) > 8:
        return filtered_name[:8]

    return filtered_name


def convert_to_email(first_name, last_name):
    return f"{first_name}.{last_name}@example.com"


def convert_dulication(email, value):
    splited_email = email.split("@")
    return f"{splited_email[0]}{value}@{splited_email[1]}"


S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Evan Doe; John Belly Doe"
C = "example"

solution(S, C)
