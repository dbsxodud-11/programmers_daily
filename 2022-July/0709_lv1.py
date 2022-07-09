# 2018 KAKAO BLIND RECRUITMENT - [1차]비밀지도

def solution(n, arr1, arr2):
    answer = [[" " for _ in range(n)] for _ in range(n)]
    for i, num in enumerate(arr1):
        for j in range(n):
            if num % 2 == 1:
                answer[i][n-j-1] = "#"
            num = num // 2
    for i, num in enumerate(arr2):
        for j in range(n):
            if num % 2 == 1:
                answer[i][n-j-1] = "#"
            num = num // 2
    return ["".join(a) for a in answer]


if __name__ == "__main__":
    example_n = [5, 6]
    example_arr1 = [[9, 20, 28, 18, 11], [46, 33, 33 ,22, 31, 50]]
    example_arr2 = [[30, 1, 21, 17, 28], [27 ,56, 19, 14, 14, 10]]
    example_result = [["#####", "# # #", "### #", "#  ##", "#####"], ["######", "###  #", "##  ##", " #### ", " #####", "### # "]]
    
    my_result = [solution(example_n[i], example_arr1[i], example_arr2[i]) for i in range(len(example_result))]
    if my_result == example_result:
        print("SUCCESS")
    else:
        print("FAILED")