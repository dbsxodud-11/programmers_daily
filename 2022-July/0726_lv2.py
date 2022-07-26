# 2018 KAKAO BLIND RECUITMENT - [1차]뉴스 클러스터링
from collections import defaultdict

def solution(str1, str2):
    # 1. lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 2. make set
    str1set = defaultdict(int)
    for i in range(len(str1)-1):
        token = str1[i:i+2]
        if token.isalpha():
            str1set[token] += 1
    
    str2set = defaultdict(int)
    for i in range(len(str2)-1):
        token = str2[i:i+2]
        if token.isalpha():
            str2set[token] += 1

    # 3. caculate similarity
    nume = 0
    deno = 0
    for k, v in str1set.items():
        if k in str2set:
            nume += min(v, str2set[k])
            deno += max(v, str2set[k])
        else:
            deno += v
            
    for k, v in str2set.items():
        if k not in str1set:
            deno += v

    return int(nume / deno * 65536) if deno > 0 else 65536


if __name__ == "__main__":
    test_cases = [["FRANCE", "french", 16384],
                  ["handshake", "shake hands", 65536],
                  ["aa1+aa2", "AAAA12", 43690],
                  ["E=M*C^2", "e=m*c^2", 65536]]

    for test_case in test_cases:
        if solution(test_case[0], test_case[1]) != test_case[-1]:
            print("FAILED")
    print("SUCCESS")