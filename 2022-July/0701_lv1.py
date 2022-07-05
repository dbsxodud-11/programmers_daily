# 카카오 인턴 - 키패드 누르기

def get_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def solution(numbers, hand):
    pos_dict = {0: (1, 0), 1: (0, 3), 2: (1, 3), 3: (2, 3), 4: (0, 2),
                5: (1, 2), 6: (2, 2), 7: (0, 1), 8: (1, 1), 9: (2, 1)}
    pos_left = (0, 0)
    pos_right = (2, 0)
    
    answer = []
    for num in numbers:
        if num in [1, 4, 7]:
            answer.append("L")
            pos_left = pos_dict[num]
        elif num in [3, 6, 9]:
            answer.append("R")
            pos_right = pos_dict[num]
        else:
            left_distance = get_distance(pos_left, pos_dict[num])
            right_distance = get_distance(pos_right, pos_dict[num])
            if (left_distance < right_distance):
                answer.append("L")
                pos_left = pos_dict[num]
            elif (left_distance > right_distance):
                answer.append("R")
                pos_right = pos_dict[num]
            else:
                if hand == "left":
                    answer.append("L")
                    pos_left = pos_dict[num]
                else:
                    answer.append("R")
                    pos_right = pos_dict[num]
    return "".join(answer)


if __name__ == "__main__":
    example_numbers = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    example_hand = ["right", "left", "right"]
    example_result = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]
    
    my_result = [solution(example_numbers[i], example_hand[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")