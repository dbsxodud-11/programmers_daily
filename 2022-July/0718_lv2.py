# 연습문제 - 더 맵게
# List에서 가장 작은 원소를 찾는 데 걸리는 시간복잡도는 O(n)이지만, Heap과 같은 구조에서는 O(logN)입니다.
# Python은 heapq라는 heap 자료구조 구현체를 지원하고 있습니다

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for sc in scoville:
        heapq.heappush(heap, sc)
        
    for i in range(len(scoville)-1):
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        heapq.heappush(heap, min1 + min2 * 2)
        answer += 1
        if heap[0] >= K:
            return answer
    return -1


if __name__ == "__main__":
    example_scoville = [[1, 2, 3, 9, 10, 12]]
    example_K = [7]
    example_result = [2]
    
    my_result = [solution(example_scoville[i], example_K[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")
