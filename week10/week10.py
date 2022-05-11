import copy
arr = [ # 8 x 9 list
    [3, 4, 9, -2, 2, 51, -23, 2, -1],
    [223, 7, 8, -11, 5, -99, 2, 3, -4],
    [2, 51, -23, -23, 6, 3, 2, 4, 5],
    [5, -99, 2, -1, 32, 2, 5, -99, 2],
    [6, 3, 3, -4, 2, -1, 6, 3, 3],
    [32, 2, 4, 5, 3, -4, 2, -1, 4],
    [4, 4, 23, 6, 2, -1, 3, -4, 34],
    [78, 32, 1, 7, 3, -4, -23, -23, 6]
]

sum_list = copy.deepcopy(arr[0]) # 더해주는 객체 리스트 생성 (0번째 행만 복사)
idx_list = list(map(str, range(9))) # 인덱스를 저장해줄 스트링 리스트 생성

def sum_result(arr, s_list, i, width, i_list): # 최댓값을 더해주는 함수
    for j in range(width):
        if j == 0 : # 가장 왼쪽 열일 때
            if arr[i + 1][j] > arr[i + 1][j + 1] : # 왼쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j]
                i_list[j] = i_list[j] + ', ' + str(j)
            else : # 오른쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j + 1]
                i_list[j] = i_list[j] + ', ' + str(j + 1)
        elif j == width - 1 : # 가장 오른쪽 열일 때
            if arr[i + 1][j - 1] > arr[i + 1][j] : # 왼쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j - 1]
                i_list[j] = i_list[j] + ', ' + str(j - 1)
            else : # 오른쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j]
                i_list[j] = i_list[j] + ', ' + str(j)
        else :
            if arr[i + 1][j - 1] > arr[i + 1][j] & arr[i + 1][j - 1] > arr[i + 1][j + 1] : # 왼쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j - 1]
                i_list[j] = i_list[j] + ', ' + str(j - 1)
            elif arr[i + 1][j] > arr[i + 1][j - 1] & arr[i + 1][j] > arr[i + 1][j + 1] : # 가운데가 클 때
                s_list[j] = s_list[j] + arr[i + 1][j]
                i_list[j] = i_list[j] + ', ' + str(j)
            else : # 오른쪽이 클 때
                s_list[j] = s_list[j] + arr[i + 1][j + 1]
                i_list[j] = i_list[j] + ', ' + str(j + 1)

for i in range(7): # 모든 행에 대해서 실행
    sum_result(arr, sum_list, i, 9, idx_list)

max_sum = max(sum_list) # 최댓값
print('경로의 최대 합 : ', max_sum)
print('경로의 인덱스 : ', idx_list[sum_list.index(max_sum)])
print('선택한 값')
idx = idx_list[sum_list.index(max_sum)].split(', ')

for i in range(8) : # 각 경로에서의 수 출력
    j = int(idx[i])
    print(arr[i][j])