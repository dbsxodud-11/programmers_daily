# 2020 KAKAO BLIND RECRUITMENT - 문자열 압축

from collections import defaultdict

def solution(s):
    comp_s_length = [len(s)]
    for unit_length in range(1, len(s)//2+1):
        comp_s = defaultdict(lambda: 1)
        length = 0

        prev_s = s[0:unit_length]
        for i in range(unit_length, len(s), unit_length):
            curr_s = s[i: i+unit_length]
            # print(prev_s, curr_s)
            if prev_s == curr_s:
                comp_s[prev_s] += 1
            else:
                comp_s[curr_s] = 1
                if comp_s[prev_s] == 1:
                    length += len(prev_s)
                else:
                    length += len(prev_s) + len(str(comp_s[prev_s]))
            prev_s = curr_s
        if comp_s[prev_s] == 1:
            length += len(prev_s)
        else:
            length += len(prev_s) + len(str(comp_s[prev_s]))
        comp_s_length.append(length)
    return min(comp_s_length)


if __name__ == "__main__":
    example_s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    example_result = [7, 9, 8, 14, 17]
    
    my_result = [solution(example_s[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")