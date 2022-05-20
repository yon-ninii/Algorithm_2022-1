import sys

INF = sys.maxsize # 간선이 없는 경로 무한대 설정

weight = [ # 6x6 리스트
    [INF, INF, INF, INF, INF, INF],
    [INF, 0, 1, INF, 1, 5],
    [INF, 9, 0, 3, 2, INF],
    [INF, INF, INF, 0, 4, INF],
    [INF, INF, INF, 2, 0, 3],
    [INF, 3, INF, INF, INF, 0]
] # 쉬운 index 설정을 위해 0번째 행과 열은 무한대로 설정

N = 5 # 노드의 개수

def print_pretty(l): # 5x5로 출력해주는 함수
    for line in l:
        if line != l[0]:
            print(line[1:])

def floyd(w, n): # 플로이드 알고리즘 함수
    p_list = [[INF] * (n + 1) for _ in range(n + 1)] # 노드 간 거리 받는 리스트 초기화
    index = [[0] * (n + 1) for _ in range(n + 1)] # 경로 받는 리스트 초기화

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            p_list[i][j] = w[i][j] # 거리 받는 리스트에 간선 가중치 입력

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if p_list[i][j] > p_list[i][k] + p_list[k][j]: # 지나갈 수 있을 때
                    p_list[i][j] = p_list[i][k] + p_list[k][j] # 더 낮은 값으로 재입력
                    index[i][j] = k # 경로 입력

    return p_list, index

def path(index, q, r): # 경로 출력 함수
    if(index[q][r] != 0):
        path(index, q, index[q][r])
        print('v%d'% index[q][r], '->', end = ' ')
        path(index, index[q][r], r)

P, I = floyd(weight, N)
print('12171786 박용민')
print('D[i][j] is')
print_pretty(P)
print('P[i][j] is')
print_pretty(I)

print('The shortest path(5, 3) is v5 -> ', end = '')
path(I, 5, 3)
print('v3')
print('The shortest path(1, 3) is v1 -> ', end = '')
path(I, 1, 3)
print('v3')
print('The shortest path(2, 5) is v2 -> ', end = '')
path(I, 2, 5)
print('v5')

