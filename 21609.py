# 21609 상어 중학교

import sys
from collections import deque
from copy import deepcopy

# 블록 그룹을 찾는 함수
def BFS(graph, s):
    
    # 큐 선언
    q = deque([s])
    
    start_r, start_c = s
    
    # 시작 블록 값
    block_val = graph[start_r][start_c]
    
    # 시작지점 방문처리
    graph[start_r][start_c] = 'v'
    
    # 블록의 개수
    cnt = 1
    
    # 기준 블록 후보군
    std_block_candidate = [s]

    # 무지개 블록
    rainbow_block = 0
    
    # 큐가 빌 때까지 반복
    while q:
        
        cur_r, cur_c = q.popleft()
        
        # 상하좌우 범위
        for t in range(4):
            
            move_r, move_c = cur_r + dr[t], cur_c + dc[t]
            
            # 주어진 범위를 벗어나지 않을 떄
            if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                
                # 인접블록 : 일반블록
                if graph[move_r][move_c] == block_val:

                    # 블록 개수 누적
                    cnt += 1
                    
                    # 방문처리
                    graph[move_r][move_c] = 'v'
                    
                    # 큐에 추가
                    q.append([move_r, move_c])
                    
                    # 기준 블록 후보군에 좌표를 추가한다.
                    std_block_candidate.append([move_r, move_c])
                
                # 인접블록 : 무지개블록 
                elif graph[move_r][move_c] == 0:
                    
                    # 블록 개수 누적
                    cnt += 1
                    
                    # 방문처리
                    graph[move_r][move_c] = 'v'
                    
                    # 큐에 추가
                    q.append([move_r, move_c])
                    
                    # 무지개 블록 추가
                    rainbow_block += 1

    # 기준 블록 선별 : 행 번호가 가장 작은, 이후 열 번호가 가장 작은
    std_block_candidate.sort(key=lambda x:(x[0],x[1]))
    
    # 덩어리에 포함된 블록 개수 반환
    return cnt, rainbow_block, std_block_candidate[0]

# 전체 점수
score = 0

# 상하좌우 : 인접한 칸
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# N, M이 주어진다.
N, M = map(int, sys.stdin.readline().split())

# 격자
grid = []

# N개의 줄에 블록의 정보가 주어진다.
for _ in range(N):
    
    # 검은색 : -1, 무지개 : 0, 일반 블록 : M이하의 자연수
    grid.append(list(map(int, sys.stdin.readline().split())))
    
# 오토 플레이 반복
while True:
    
    blocks = []
    
    # 모든 블록 그룹을 찾는다.
    for i in range(N):
        
        for j in range(N):
            
            if grid[i][j] == 'v':
                
                continue
            
            # 일반 블록
            elif 1 <= grid[i][j] <= M:
                
                # 격자 복사
                temp = deepcopy(grid)
                
                # 덩어리를 찾는다.
                cnt, rb_block, std_block = BFS(temp, [i,j])
                
                # 블록의 개수가 2보다 크거나 같을 때
                if cnt >= 2:
                    
                    blocks.append([cnt, rb_block, std_block])
    
    # 블록 크기 순, 무지개 블록 수, 좌표 위치 순으로 정렬
    blocks.sort(key = lambda x:(-x[0], -x[1], (-x[2][0], -x[2][1])))

    # 가장 큰 블록의 크기가 1이거나 블록이 없으면 오토플레이 종료
    if len(blocks) == 0:
        
        break
    
    # 가장 큰 블록 제거를 시작하기 위한 작업
    temp = deepcopy(grid)
    
    cnt, rb_block, std_block = BFS(temp, blocks[0][2])
    
    # 모든 블록을 제거
    for i in range(N):
        
        for j in range(N):
            
            if temp[i][j] == 'v':
                
                grid[i][j] = 'v'
    
    # 점수 획득
    score += (cnt**2)
    
    # 격자에 중력이 작용한다.(1)
    while True:
        
        # 밑으로 떨어진 블록 개수
        drop = 0
        
        for i in range(N):
            
            for j in range(N):
                
                # 일반블록, 무지개블록이면서 범위를 벗어나지 않을 때
                if type(grid[i][j]) == int and grid[i][j] >= 0 and i+1 <= N-1:
                    
                    if grid[i+1][j] == 'v':
                        
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = 'v'
                        
                        drop += 1
        
        # 떨어질게 더 이상 없으면 종료
        if drop == 0:
            
            break                 
                            
    # 격자가 90도 반시계 방향으로 회전한다.
    temp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        
        for j in range(N):
            
            temp[N-1-j][i] = grid[i][j]

    grid = deepcopy(temp)
    
    # 격자에 중력이 작용한다.(2)
    while True:
        
        # 밑으로 떨어진 블록 개수
        drop = 0
        
        for i in range(N):
            
            for j in range(N):
                
                # 일반블록, 무지개블록이면서 범위를 벗어나지 않을 때
                if type(grid[i][j]) == int and grid[i][j] >= 0 and i+1 <= N-1:
                    
                    if grid[i+1][j] == 'v':
                        
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = 'v'
                        
                        drop += 1
        
        # 떨어질게 더 이상 없으면 종료
        if drop == 0:
            
            break
              
# 획득한 점수의 합 출력
print(score)