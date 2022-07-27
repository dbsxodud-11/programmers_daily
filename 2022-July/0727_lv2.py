# 2021 카카오 채용연계형 인턴쉽 - 거리두기 확인하기

def check_constraint(board, person):
    for i in range(len(person)):
        for j in range(i+1, len(person)):
            distance = abs(person[i][0] - person[j][0]) + abs(person[i][1] - person[j][1])
            if distance == 1:
                return 0
            elif distance == 2:
                person_i_x, person_i_y = person[i]
                person_j_x, person_j_y = person[j]
                if person_i_x == person_j_x:
                    if person_i_y < person_j_y and board[person_i_x][person_i_y + 1] == "O":
                        return 0
                    if person_i_y > person_j_y and board[person_i_x][person_i_y - 1] == "O":
                        return 0
                if person_i_y == person_j_y:
                    if person_i_x < person_j_x and board[person_i_x + 1][person_i_y] == "O":
                        return 0
                    if person_i_x > person_j_x and board[person_i_x - 1][person_i_y] == "O":
                        return 0
                if person_i_x + 1 == person_j_x:
                    if person_i_y + 1 == person_j_y:
                        if board[person_i_x+1][person_i_y] == "O" or board[person_i_x][person_i_y+1] == "O":
                            return 0
                    else:
                        if board[person_i_x+1][person_i_y] == "O" or board[person_i_x][person_i_y-1] == "O":
                            return 0
                if person_i_x - 1 == person_j_x:
                    if person_i_y + 1 == person_j_y:
                        if board[person_i_x-1][person_i_y] == "O" or board[person_i_x][person_i_y+1] == "O":
                            return 0
                    else:
                        if board[person_i_x-1][person_i_y] == "O" or board[person_i_x][person_i_y-1] == "O":
                            return 0

    return 1

def solution(places):
    answer = []
    for place in places:
        board = [list(row) for row in place]
        person = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == "P":
                    person.append((i, j))
        if len(person) == 0:
            answer.append(1)
        else:
            answer.append(check_constraint(board, person))
    return answer


if __name__ == "__main__":
    test_cases = [[[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
                    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]], [1, 0, 1, 1, 1]]]

    for test_case in test_cases:
        if solution(test_case[0]) != test_case[-1]:
            print("FAILED")
    print("SUCCESS")