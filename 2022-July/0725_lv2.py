# 2021 KAKAO BLIND RECRUITMENT - 괄호 변환

from collections import deque

def isright(p):
    stack = deque()
    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True

def flip(p):
    p_new = []
    for i in range(len(p)):
        if p[i] == '(':
            p_new.append(')')
        else:
            p_new.append('(')
    return "".join(p_new)

def solution(p):
    # Step 1
    if len(p) == 0:
        return p
    
    # Step 2
    num_left = 0
    num_right = 0
    for i in range(len(p)):
        if p[i] == '(':
            num_left += 1
        else:
            num_right += 1
        if num_left == num_right:
            u = p[:i+1]
            v = p[i+1:]
            break

    # Step 3
    if isright(u):
        return u + solution(v)
    
    # Step 4
    answer = '('
    answer += solution(v)
    answer += ')'
    answer += flip(u[1: -1])
    return answer


if __name__ == "__main__":
    example_p = ["(()())()", ")(", "()))((()"]
    example_result = ["(()())()", "()", "()(())()"]

    my_result = [solution(example_p[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")