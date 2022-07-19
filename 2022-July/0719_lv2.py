# 연습문제 - 타겟넘버
# 재귀함수를 사용하여 가능한 경우의 수를 계산할 수 있습니다

def solution(numbers, target):
    return dfs(numbers, 0, 0, target)

def dfs(numbers, node, result, target):
    if node == len(numbers):
        return 1 if result == target else 0
    else:
        return dfs(numbers, node+1, result+numbers[node], target) + dfs(numbers, node+1, result-numbers[node], target)
    
    
if __name__ == "__main__":
    example_numbers = [[1, 1, 1, 1, 1], [4, 1, 2, 1]]
    example_target = [3, 4]
    example_result = [5, 2]
    
    my_result = [solution(example_numbers[i], example_target[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")