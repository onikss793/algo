from typing import List


def solution(id_list, report: List[str], k):
    answer = []
    id_set = set(report)

    reported_id_map = {}
    reporter_id_map = {}

    for r in id_set:
        user, target = r.split(" ")

        if target not in reported_id_map:
            reported_id_map[target] = 1
        else:
            reported_id_map[target] += 1

    for r in id_set:
        user, target = r.split(" ")
        count = reported_id_map.get(target)

        reporter_id_map.setdefault(user, 0)

        if count // k > 0:
            reporter_id_map[user] += 1

    for id in id_list:
        result = reporter_id_map.get(id) if reporter_id_map.get(id) else 0
        answer.append(result)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = [
    "muzi frodo",
    "apeach frodo",
    "frodo neo",
    "muzi neo",
    "apeach muzi",
]
k = 2
result = solution(id_list, report, k)
print(result)

# [2,1,1,0]
