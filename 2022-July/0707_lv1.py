# 월간 코드 챌린지 시즌3 - 없는 숫자 더하기
def solution(numbers):
    number_set = set([i for i in range(10)])
    missing_set = number_set - set(numbers)
    return sum(missing_set)

if __name__ == "__main__":
    example_numbers = [[1,2,3,4,6,7,8,0], [5,8,4,0,6,7,9]]
    example_result = [14, 6]
    
    my_result = [solution(example_numbers[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")