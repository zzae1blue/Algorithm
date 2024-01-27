# 20056 마법사 상어와 파이어볼

import sys
from collections import deque
from math import floor

# 파이어볼 이동하는 함수
def move(c):
    
    # 모든 파이어볼이 이동한다.
    for cd in c:
        
        # 파이어볼이 있는 좌표
        i, j, length = cd
         
        for t in range(length):
            
            fire_ball = grid[i][j].popleft()
            
            ball_m, ball_s, ball_dir = fire_ball
            
            # 이동양을 결정한다.
            ball_s = ball_s % N
            
            # 가로 움직임
            move_c = j + ball_s * dc[ball_dir]

            if move_c > N-1:
                
                move_c -= N
            
            elif move_c < 0:
                
                move_c = j + (N-ball_s)
            
            # 세로 움직임
            move_r = i + ball_s * dr[ball_dir]
            
            if move_r > N-1:
                
                move_r -= N
            
            elif move_r < 0:
                
                move_r = i + (N-ball_s)
                
            grid[move_r][move_c].append(fire_ball)
    
    # 2개 이상의 파이어볼이 있는 칸을 조사한다.
    for i in range(N):
        
        for j in range(N):
            
            if len(grid[i][j]) >= 2:
                
                total_m = 0
                total_s = 0
                total_dir = []
                
                for fire_ball in grid[i][j]:
                    
                    ball_m, ball_s, ball_dir = fire_ball
                    
                    total_m += ball_m
                    total_s += ball_s
                    total_dir.append(ball_dir)
                
                m = floor(total_m/5)
                s = floor(total_s/len(grid[i][j]))
                
                # 방향이 홀수일 때
                odd = 0
                
                # 방향이 짝수일 때
                even = 0
                
                for k in range(len(total_dir)):
                    
                    if total_dir[k] % 2 == 1:
                        
                        odd += 1
                    
                    elif total_dir[k] % 2 == 0:
                        
                        even += 1
                
                # 모두 홀수이거나 모두 짝수면
                if (odd == len(total_dir)) or (even == len(total_dir)):
                    
                    total_dir = [0, 2, 4, 6]
                
                else:
                    
                    total_dir = [1, 3, 5, 7]

                # 질량이 0인 파이어볼은 소멸되어 없어진다.
                if m == 0:
                    
                    grid[i][j] = deque()
                
                # 질량이 0보다 클 때
                else:
                    
                    grid[i][j] = deque()
                    
                    # 4개의 파이어볼 추가
                    for t in range(4):
                        
                        grid[i][j].append((m, s, total_dir[t]))
                        
# N, M, K가 주어진다.
N, M, K = map(int, sys.stdin.readline().split())

# 격자
grid = [[deque() for _ in range(N)] for _ in range(N)]

# 8개 방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 파이어볼의 정보가 하나씩 주어진다.
for _ in range(M):
    
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    
    r -= 1
    c -= 1
    
    # 격자에 파이어볼을 추가한다.
    grid[r][c].append((m, s, d))

# K번 명령한다.
for _ in range(K):
    
    coord = []
    
    for i in range(N):
        
        for j in range(N):
            
            if grid[i][j]:
                
                coord.append((i,j, len(grid[i][j])))
                    
    move(coord)

ans = 0

# 남아있는 파이어볼의 질량의 합을 구한다.
for i in range(N):
    
    for j in range(N):
        
        if grid[i][j]:
            
            for t in range(len(grid[i][j])):
                
                m, s, d = grid[i][j][t]
                
                ans += m

# 답 출력
print(ans)