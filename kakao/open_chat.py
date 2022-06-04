from typing import List


def solution(record: List[str]):
    answer = []
    id_map = {}

    for rec in record:
        data = rec.split(" ")
        action = data[0]

        if action in ["Enter", "Change"]:
            id_map[data[1]] = data[2]

    for rec in record:
        data = rec.split(" ")
        action = data[0]
        action_message = get_action(data)

        if action in ["Enter", "Leave"]:
            msg = f"{id_map.get(data[1])}님이 {action_message}"
            answer.append(msg)

    return answer


def get_action(data: str):
    action_msg = {
        "Enter": "들어왔습니다.",
        "Leave": "나갔습니다.",
    }

    action = data[0]

    return action_msg.get(action)


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]

result = solution(record)
print(result)

# [
# "Prodo님이 들어왔습니다.",
# "Ryan님이 들어왔습니다.",
# "Prodo님이 나갔습니다.",
# "Prodo님이 들어왔습니다."
# ]
