# 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임

# Stack은 LIFO policy에 의해 동작하기 때문에, push와 pop의 time complexity가 O(1)입니다. 제일 마지막에 넣은 element만 확인하고 싶다면
# Stack 데이터 구조를 추천합니다

from collections import deque

def solution(board, moves):
    answer = 0
    basket = deque()
    
    for move in moves:
        pos_x = move-1
        for pos_y in range(len(board)):
            if board[pos_y][pos_x] != 0:
                if len(basket) == 0:
                    basket.append(board[pos_y][pos_x])
                    board[pos_y][pos_x] = 0
                    break
                last_elem = basket[-1]
                cur_elem = board[pos_y][pos_x]
                if last_elem == cur_elem:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[pos_y][pos_x])
                board[pos_y][pos_x] = 0
                break
    
    return answer


if __name__ == "__main__":
    example_board = [[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]]
    example_moves = [[1,5,3,5,1,2,1,4]]
    example_result = [4]
    
    my_result = [solution(example_board[i], example_moves[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")