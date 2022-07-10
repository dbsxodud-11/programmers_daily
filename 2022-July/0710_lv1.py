# 2018 KAKAO BLIND RECRUITMENT - [1차]다트 게임
def solution(dartResult):
    answer = []
    bonus = ["S", "D", "T"]
    option = ["*", "#"]
    score = ""
    for i in range(len(dartResult)):
        if dartResult[i] not in bonus and dartResult[i] not in option:
            score += dartResult[i]
        else:
            symbol = dartResult[i]
            if symbol in bonus:
                score = int(score)
                if symbol == "S":
                    answer.append(score)
                elif symbol == "D":
                    answer.append(pow(score, 2))
                else:
                    answer.append(pow(score, 3))
                score = ""
            if symbol in option:
                if symbol == "*":
                    answer[-1] *= 2
                    if len(answer) >= 2:
                        answer[-2] *= 2
                else:
                    answer[-1] *= -1
    return sum(answer)


if __name__ == "__main__":
    example_dartResult = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
    example_result = [37, 9, 3, 23, 5, -4, 59]
    
    my_result = [solution(example_dartResult[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")