# 2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기

from collections import defaultdict

def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    
    idx2num = defaultdict(int)
    idx2target = defaultdict(list)
    report = list(set(report))
    for r in report:
        source, target = r.split(" ")
        idx2num[target] += 1
        idx2target[source].append(target)
    
    for i, idx in enumerate(id_list):
        for target in idx2target[idx]:
            if idx2num[target] >= k:
                answer[i] += 1
    
    return answer


if __name__ == "__main__":
    example_id_list = [["muzi", "frodo", "apeach", "neo"], ["con", "ryan"]]
    example_report = [["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 
                      ["ryan con", "ryan con", "ryan con", "ryan con"]]
    example_k = [2, 3]
    example_result = [[2, 1, 1, 0], [0, 0]]
    
    my_result = [solution(example_id_list[i], example_report[i], example_k[i]) for i in range(2)]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")