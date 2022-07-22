# 2017 팁스타운 - 짝지어 제거하기
# 무조건 문자열의 앞쪽에서 짝지어 문자열을 제거해야 하므로, Stack구조를 쓰는 것이 바람직합니다.
# 2019 카카오 개발자 겨울 인텁쉽 코딩테스트에 나온 크레인 인형뽑기 게임과 유사한 문제입니다.

from collections import deque

def solution(s):
    if len(s) % 2 == 1:
        return 0
    if len(s) == 2:
        return 0 if len(set(s)) == 2 else 1
    
    stack = deque()
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) > 0 and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
            
    return 0 if len(stack) > 0 else 1


if __name__ == "__main__":
    example_s = ["baabaa", "cdcd"]
    example_result = [1, 0]

    my_result = [solution(example_s[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")