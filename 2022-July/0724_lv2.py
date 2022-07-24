# 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼
# itertools package의 combinations라는 함수는 n개 중 순서를 고려하지 않고 중복 없이 r개를 뽑는 모든 경우의 수를 알려줍니다.
# itertools에는 combinations뿐만 아니라 permutations, combinations_with_replacement 등의 함수도 있습니다

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for n in course:
        comb2num = defaultdict(int)
        for order in orders:
            order = sorted(order)
            combs = list(map(lambda x: "".join(x), combinations(order, n)))
            for comb in combs:
                comb2num[comb] += 1
        comb2num = list(filter(lambda x: x[1]>=2, [(k, v) for k, v in comb2num.items()]))
        if len(comb2num) == 0:
            continue
        else:
            num2comb = defaultdict(list)
            for comb, num in comb2num:
                num2comb[num].append(comb)

            max_value = max(comb2num, key=lambda x: x[1])[1]
            answer += num2comb[max_value]

    return list(sorted(answer))

if __name__ == "__main__":
    example_orders = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
    example_course = [[2, 3, 4], [2, 3, 5], [2, 3, 4]]
    example_result = [["AC", "ACDE", "BCFG", "CDE"], ["ACD", "AD", "ADE", "CD", "XYZ"], ["WX", "XY"]]

    my_result = [solution(example_orders[i], example_course[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")