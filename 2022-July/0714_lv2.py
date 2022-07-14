# 연습문제 - 124 나라의 숫자

def solution(n):
    answer = ''
    translator = {1: "1", 2: "2", 0: "4"}
    while n >= 1:
        answer += translator[n%3]
        if n%3 == 0:
            n = n//3 - 1
        else:
            n = n//3
    return answer[::-1]

if __name__ == "__main__":
    example_n = [1, 2, 3, 4, 9, 10]
    example_result = ["1", "2", "4", "11", "24", "41"]
    
    my_result = [solution(example_n[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")