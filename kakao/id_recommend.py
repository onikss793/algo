import re


def upper_to_lower(new_id: str):
    return new_id.lower()


def eliminate_wrong_words(lowered_new_id: str):
    result = ''
    regex = '[a-z0-9-_.]'
    for word in lowered_new_id:
        if re.match(regex, word):
            result += word

    return result


def dot_converter(filtered_id: str):
    return filtered_id.replace('...', '.').replace('..', '.')


def dot_eliminator(filtered_id: str):
    if len(filtered_id) and filtered_id[0] == '.':
        filtered_id = filtered_id[1:]

    if len(filtered_id) and filtered_id[-1] == '.':
        filtered_id = filtered_id[:-1]

    return filtered_id


def set_if_empty(filtered_id: str):
    if len(filtered_id) == 0:
        filtered_id = 'a'

    return filtered_id


def delete_if_too_long(filtered_id: str):
    if len(filtered_id) >= 16:
        filtered_id = filtered_id[:15]

    if filtered_id[-1] == '.':
        filtered_id = filtered_id[:-1]

    return filtered_id


def add_if_too_short(filtered_id: str):
    if len(filtered_id) <= 2:
        word = filtered_id[-1]
        while len(filtered_id) < 3:
            filtered_id += word

    return filtered_id


def solution(new_id: str):
    answer = add_if_too_short(
        delete_if_too_long(
            set_if_empty(
                dot_eliminator(
                    dot_converter(
                        eliminate_wrong_words(
                            upper_to_lower(new_id)
                        )
                    )
                )
            )
        )
    )

    return answer


_id = "abcdefghijklmn.p"
print('RESULT: ', solution(_id))
