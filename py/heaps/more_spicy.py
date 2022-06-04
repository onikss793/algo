import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            minimum = heapq.heappop(scoville)
            sec_min = heapq.heappop(scoville)
            heapq.heappush(scoville, minimum + (sec_min * 2))
            answer += 1

    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    answer = solution(scoville, K)
    print(answer)
