# 2019 KAKAO BLIND RECUITMENT - 오픈채팅방

def solution(record):
    answer = []
    userid2nickname = {}
    for r in record:
        action = r.split(" ")[0]
        if action == "Enter":
            userid, nickname = r.split(" ")[1:]
            answer.append((userid, action))
            userid2nickname[userid] = nickname
        elif action == "Leave":
            userid = r.split(" ")[1]
            answer.append((userid, action))
        else:
            userid, nickname = r.split(" ")[1:]
            userid2nickname[userid] = nickname
    for i, a in enumerate(answer):
        if a[1] == "Enter":
            answer[i] = userid2nickname[a[0]] + "님이 들어왔습니다."
        elif a[1] == "Leave":
            answer[i] = userid2nickname[a[0]] + "님이 나갔습니다."
    return answer


if __name__ == "__main__":
    example_record = [["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234","Enter uid1234 Prodo", "Change uid4567 Ryan"]]
    example_result = [["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]
    
    my_result = [solution(example_record[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")