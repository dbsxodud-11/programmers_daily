# 연습문제 - 기능개발
# 앞에 있는 기능이 무조건 먼저 배포되어야 하므로, LIFO Policy를 가지는 Stack를 사용하면 효율적입니다
# Python에는 deque라는 stack를 지원하는 자료구조가 구현되어 있습니다

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    for progress, speed in zip(progresses, speeds):
        days.appendleft(math.ceil((100 - progress) / speed))
    
    while len(days) > 0:
        day = days.pop()
        answer.append(1)
        if len(days) == 0:
            break
        while len(days) > 0:
            next_day = days[-1]
            if day >= next_day:
                answer[-1] += 1
                days.pop()
            else:
                break
        
    return answer


if __name__ == "__main__":
    example_progresses = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
    example_speeds = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
    example_result = [[2, 1], [1, 3, 2]]
    
    my_result = [solution(example_progresses[i], example_speeds[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")