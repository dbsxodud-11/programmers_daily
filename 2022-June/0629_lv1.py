# 2021 KAKAO BLIND RECRUITMENT - 신규 아이디 추천

import re

def solution(new_id):
    answer = ''
    
    # 1. to lowercase
    new_id = new_id.lower()

    # 2. -,_,.를 제외한 특수문자 제거
    new_id = re.sub(r"[^a-z0-9\-_.]", "", new_id)
    
    # 3. 마침표 2번 이상 -> 하나의 마침표로
    n = len(new_id)
    if n > 0:
        prev_char = new_id[0]
        for i in range(1, n):
            if prev_char == '.' and new_id[i] == prev_char:
                new_id = new_id[:i-1] + '?' + new_id[i:]
            prev_char = new_id[i]

    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)

    # 4. 마침표가 처음이나 끝에 위치
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    # 5. 빈 문자열
    if len(new_id) == 0:
        new_id = "a"
    
    # 6. 16자 이상
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7. 2자 이하
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    
    return new_id

if __name__ == "__main__":
    example_new_id = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    example_result = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]
    
    my_result = [solution(example_new_id[i]) for i in range(len(example_new_id))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")