# Summer/Winter Coding - 멀쩡한 사각형
# 다른 사람들의 풀이를 참고하였음(최대공약수 활용) 
# 내 solution도 합리적이라고 생각하지만 input이 1억 이상의 숫자라 오류가 생기는 것으로 보임

import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))

def my_solution(x, h):
    return w * h - min(w, h) * math.ceil(max(w, h) / min(w, h))


if __name__ == "__main__":
    example_w = [8]
    example_h = [12]
    example_result = [80]
    
    my_result = [solution(example_w[i], example_h[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")