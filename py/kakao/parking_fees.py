import math
from typing import List

MAX_MIN = 1439


def solution(fees: List[int], records: List[str]) -> List[int]:
    def charge(minute: int) -> int:
        if minute <= default_time:
            return default_fee

        return int(math.ceil((minute - default_time) / time)) * fee + default_fee

    answer = []
    default_time, default_fee, time, fee = fees

    total_fee_map = {}
    total_min_map = {}

    cache = {}
    for rec in records:
        timecode, car_number, action = rec.split(' ')
        timecode_min = (int(timecode[:2]) * 60) + int(timecode[3:])

        answer.append(car_number)

        if action == 'IN':
            cache[car_number] = timecode_min
        if action == 'OUT':
            charge_min = timecode_min - cache[car_number]
            cache.pop(car_number)

            if car_number in total_min_map:
                total_min_map[car_number] += charge_min
            else:
                total_min_map[car_number] = charge_min

    for key in cache:
        if key in total_min_map:
            total_min_map[key] += MAX_MIN - cache[key]
        else:
            total_min_map[key] = MAX_MIN - cache[key]

    for car_number in total_min_map:
        total_fee_map[car_number] = charge(total_min_map[car_number])

    answer = [total_fee_map.get(car_number) for car_number in sorted(set(answer))]

    return answer


f = [1, 461, 1, 10]
r = ["00:00 1234 IN"]

#            0000   0148  5961
# result = [14600, 34400, 5000]


res = solution(f, r)
print(res)
