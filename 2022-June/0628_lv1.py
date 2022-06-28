# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = [0 for _ in range(2)]
    
    zero_count = len(list(filter(lambda x: x==0, lottos)))
        
    min_hit = set(lottos).intersection(set(win_nums))
    min_hit = len(min_hit)
    max_hit = min_hit + zero_count
    
    if (max_hit <= 1):
        answer[0] = 6
    else:
        answer[0] = 7 - max_hit
        
    if (min_hit <= 1):
        answer[1] = 6
    else:
        answer[1] = 7 - min_hit
    return answer

if __name__ == "__main__":
    example_lottos = [ [44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
    example_win_nums = [[31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35]]
    example_result = [[3, 5], [1, 6], [1, 1]]
    
    my_result = [solution(example_lottos[i], example_win_nums[i]) for i in range(3)]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")