# 2021 카카오 채용연계형 인턴쉽 - 숫자 문자열과 영단어

def solution(s):
    answer = []
    
    str_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    while len(s) > 0:
        for i in range(len(str_list)):
            if s.startswith(str(i)):
                s = s[1:]
                answer.append(i)
                break

        for i in range(len(str_list)):
            if s.startswith(str_list[i]):
                s = s[len(str_list[i]):]
                answer.append(i)
                break
    # print(answer)
    return int("".join(list(map(str, answer))))

if __name__ == "__main__":
    example_s = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    example_result = [1478, 234567, 234567, 123]
    
    my_result = [solution(example_s[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")