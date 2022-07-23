# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    
    board = [[(i+1) + columns * (j) for i in range(columns)] for j in range(rows)]
    for query in queries:
        r1, c1, r2, c2 = query
        edges = []
        edges += [(r1, c) for c in range(c1, c2)]
        edges += [(r, c2) for r in range(r1, r2)]
        edges += [(r2, c) for c in range(c2, c1, -1)]
        edges += [(r, c1) for r in range(r2, r1, -1)]
        
        elements = [board[r-1][c-1] for r, c in edges]
        answer.append(min(elements))
        elements_rotate = [board[edges[-1][0]-1][edges[-1][1]-1]] + [board[r-1][c-1] for r, c in edges[:-1]]
        
        for edge, element_rotate in zip(edges, elements_rotate):
            board[edge[0]-1][edge[1]-1] = element_rotate
        
    return answer


if __name__ == "__main__":
    example_rows = [6, 3, 100]
    example_columns = [6, 3, 97]
    example_queries = [[[2,2,5,4],[3,3,6,6],[5,1,6,3]], [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]], [[1,1,100,97]]]
    example_result = [[8, 10, 25], [1, 1, 5, 3], [1]]

    my_result = [solution(example_rows[i], example_columns[i], example_queries[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")