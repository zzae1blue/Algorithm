# 20058 마법사 상어와 파이어스톰

import sys
from collections import deque

# 얼음 덩어리를 계산하자.
def BFS(s):
    
    # 시작노드 방문처리
    start_r, start_c = s
    grid[start_r][start_c] = '*'
    
    # 덩어리 추가
    cnt = 1
    
    q = deque([s])
    
    # 4방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 큐가 빌 때까지 반복
    while q:
        
        cur_r, cur_c = q.popleft()
        
        for t in range(4):
            
            move_r = cur_r + dr[t]
            move_c = cur_c + dc[t]
            
            # 주어진 영역을 벗어나지 않을 때
            if 0 <= move_r <= 2**N-1 and 0 <= move_c <= 2**N-1:
                
                # 이미 방문한 지점이 아니고 0보다 클 때 덩어리를 구성
                if grid[move_r][move_c] != '*' and grid[move_r][move_c] > 0:
                    
                    cnt += 1
                    
                    # 방문처리
                    grid[move_r][move_c] = '*'
                    q.append([move_r, move_c])

    return cnt

# N, Q가 주어진다.
N, Q = map(int, sys.stdin.readline().split())

# 격자
grid = []

# 얼음의 양이 주어진다.
for _ in range(2**N):
    
    grid.append(list(map(int, sys.stdin.readline().split())))

# 마법사 상어가 시전한 단계 L이 순서대로 주어진다.
stage_L = list(map(int, sys.stdin.readline().split()))

# 상하좌우 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# L에 따라서 회전시킨다.
for L in stage_L:
    
    index = [n*(2**L) for n in range(2**(N-L))]
    
    for i in index:
        
        for j in index:
            
            temp1 = [[0] * (2**L) for _ in range(2**L)]
            
            for r in range(i, i+(2**L)):
                
                for c in range(j, j+(2**L)):
                    
                    temp1[r-i][c-j] = grid[r][c]
            
            temp2 = [[0] * (2**L) for _ in range(2**L)]
            
            for r in range(2**L):
                
                for c in range(2**L):
                    
                    temp2[c][(2**L)-1-r] = temp1[r][c]
                    
            for r in range(i, i+(2**L)):
                
                for c in range(j, j+(2**L)):
                    
                    grid[r][c] = temp2[r-i][c-j]

    # 녹아야하는 좌표
    melt = []
    
    for r in range(2**N):
        
        for c in range(2**N):
            
            # 녹을 얼음이 없으면 skip한다.
            if grid[r][c] == 0:
                
                continue
            
            # 인접하지 않은 칸 개수
            cnt = 0
            
            for k in range(4):
                
                move_r = r + dr[k]
                move_c = c + dc[k]
                
                if 0 <= move_r <= 2**N-1 and 0 <= move_c <= 2**N-1:
                    
                    if grid[move_r][move_c] == 0:
                        
                        cnt += 1
                else:
                    
                    cnt += 1
            
            if cnt >= 2:
                
                melt.append([r,c])
    
    for coord in melt:
        
        r, c = coord
        
        grid[r][c] -= 1
                
# 남아있는 얼음 A[r][c]의 합
remain_ice = 0

for i in range(2**N):
    
    for j in range(2**N):
        
        remain_ice += grid[i][j]
        
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
max_ice = -1

# BFS Algorithm을 사용하여 덩어리를 계산
for i in range(2**N):
    
    for j in range(2**N):
        
        if grid[i][j] != '*' and grid[i][j] > 0:
            
            max_ice = max(BFS([i,j]), max_ice)

# 답 출력
print(remain_ice)

if max_ice < 0:
    
    print(0)

else:
    
    print(max_ice)