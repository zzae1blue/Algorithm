# 16234 인구 이동
import sys
from math import floor
from collections import deque
from copy import deepcopy

# 너비우선탐색 알고리즘
def BFS(graph, s):
            
    # 연합이 형성되는지 여부
    is_union = False
    
    # 연합의 인구수
    human = 0
    
    # 연합의 개수
    union = 0
    
    # 연합의 좌표 모음
    union_coord = []

    # 시작좌표
    cur_r, cur_c = s
    union_coord.append(s)
    
    human += graph[cur_r][cur_c]
    union += 1
    
    # 시작좌표 방문처리
    graph[cur_r][cur_c] = 'v'
    
    # 큐 선언
    q = deque([s])
    
    # 큐가 빌 때까지 반복
    while q:
        
        # 현재좌표를 큐에서 꺼냅니다.
        cur_r, cur_c = q.popleft()
        
        # 판단
        for val in diff[cur_r][cur_c]:
            
            k, tf = val
            
            move_r, move_c = cur_r + dr[k], cur_c + dc[k]
            
            if tf == 'Y':
                
                if type(graph[move_r][move_c]) == int:
                    
                    human += graph[move_r][move_c]
                    union += 1
                    
                    # 방문처리
                    graph[move_r][move_c] = 'v'
                    
                    # 큐에 추가
                    q.append([move_r, move_c])
                    
                    # 좌표 추가
                    union_coord.append([move_r, move_c])
                
                else:
                    
                    continue
                
            elif tf == 'N':
                
                continue

    # 1보다 크면 연합이 형성됨
    if union > 1:
        
        is_union = True
        
    return is_union, human, union, union_coord

# N, L, R이 주어진다.
N, L, R = map(int, sys.stdin.readline().split())

# N x N 땅
A = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N개의 줄에 각 나라의 인구수가 주어진다.
for _ in range(N):
    
    A.append(list(map(int, sys.stdin.readline().split())))

# 인구이동이 걸리는 시간
day = 0

# 인구 이동이 없을 때까지 반복
while True:

    diff = [[[] for _ in range(N)] for _ in range(N)]
    
    # 이웃 지점과의 인구수 차를 다 구해봅니다.
    for r in range(N):
        
        for c in range(N):
            
            for k in range(4):
                
                move_r, move_c = r + dr[k], c + dc[k]
                
                # 인구수 차이가 L이상 R이하라면
                if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                    
                    if L <= abs(A[r][c] - A[move_r][move_c]) <= R:
                    
                        diff[r][c].append([k, 'Y'])
                    
                    else:
                        
                        diff[r][c].append([k, 'N'])
                        
    # 원본리스트 복사
    temp = deepcopy(A)
    
    # 인구 이동 여부
    is_moving = False
    
    # 모든 지점을 살펴보자
    for i in range(N):
        
        for j in range(N):
            
            if type(temp[i][j]) == int:
                
                is_union, human, union, union_coord = BFS(temp, [i,j])
                
                # 연합이 형성되었을 때
                if is_union:
                    
                    is_moving = True

                    # 연합 구성원 수 / 연합 수, 소수점 이하는 버린다.
                    update = floor(human / union)
                    
                    for coord in union_coord:
                        
                        r, c = coord
                        
                        A[r][c] = update
                        
                # 연합이 형성되지 않았을 때  
                else:
                    
                    continue

    # 인구 이동이 없어지면 종료합니다.
    if is_moving == False:
        
        break
    
    # 인구 이동이 이루어진 후 날짜를 하루 증가합니다.
    else:
        
        day += 1
    
# 인구 이동이 며칠 동안 발생하는지 출력
print(day)