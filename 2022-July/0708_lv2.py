# 2019 KAKAO BLIND RECRUITMENT - 실패율

# Sorting Algorithm에는 여러 가지 종류가 있는데, 같은 값을 가지는 element의 위치가 바뀌지 않는 stable한 sorting 방법과 위치가 바뀔
# 가능성이 있는 unstable sorting으로 나눌 수 있습니다. Quicksort는 대표적인 unstable sorting algorithm이고, Mergesort는 대표적인 stable
# sorting algorithm입니다. 이 점에 유의하여 문제에 알맞은 sorting방식을 사용하면 문제를 쉽게 해결할 수 있습니다.

import numpy as np

def solution(N, stages):
    nume = [0 for _ in range(N+1)]
    deno = [0 for _ in range(N)]
    
    for stage in stages:
        nume[stage-1] += 1
    for i in range(1, N+1):
        stages = list(filter(lambda x: x >= i, stages))
        deno[i-1] = len(stages)
        
    failure_rate = [nume / deno if deno > 0 else 0.0 for nume, deno in zip(nume[:-1], deno)][::-1]
    return list(map(lambda x: N-x, np.argsort(failure_rate, kind="stable")[::-1].tolist()))


if __name__ == "__main__":
    example_N = [5, 4]
    example_stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4, 4, 4, 4]]
    example_result = [[3, 4, 2, 1, 5], [4, 1, 2, 3]]
    
    my_result = [solution(example_N[i], example_stages[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")