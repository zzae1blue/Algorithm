# 21610 마법사 상어와 비바라기

import sys

# 이동하는 함수
def move(di, si):
    
    global grid
    
    # 구름의 집함
    clouds = []
    
    # 구름이 있는지 확인하는 리스트
    exist = [[False] * N for _ in range(N)]
    
    for i in range(N):
        
        for j in range(N):
            
            if grid[i][j] == 'C':
                
                clouds.append([i,j])
    
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    move_clouds = []
    
    if di == 1:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dc = si % N
            
            move_r = cur_r
            move_c = cur_c
            
            if cur_c - dc >= 0:
                
                move_c = cur_c - dc
            
            else:
                
                move_c = cur_c - dc + N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
            
    elif di == 2:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr, dc = si % N, si % N
            
            move_r, move_c = cur_r, cur_c
            
            if cur_r - dr >= 0:
                
                move_r = cur_r - dr
            
            else:
                
                move_r = cur_r - dr + N
            
            if cur_c - dc >= 0:
                
                move_c = cur_c - dc
            
            else:
                
                move_c = cur_c - dc + N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True            
            move_clouds.append([move_r, move_c])
            
    elif di == 3:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr = si % N
            
            move_r = cur_r
            move_c = cur_c
            
            if cur_r - dr >= 0:
                
                move_r = cur_r - dr
                
            else:
                
                move_r = cur_r - dr + N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
            
    elif di == 4:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr, dc = si % N, si % N
            
            move_r, move_c = cur_r, cur_c
            
            if cur_r - dr >= 0:
                
                move_r = cur_r - dr
            
            else:
                
                move_r = cur_r - dr + N
            
            if cur_c + dc <= N-1:
                
                move_c = cur_c + dc
            
            else:
                
                move_c = cur_c + dc - N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
            
    elif di == 5:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dc = si % N
            
            move_r = cur_r
            move_c = cur_c

            if cur_c + dc <= N-1:
                
                move_c = cur_c + dc
            
            else:
                
                move_c = cur_c + dc - N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
            
    elif di == 6:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr, dc = si % N, si % N
            
            move_r, move_c = cur_r, cur_c

            if cur_r + dr <= N-1:
                
                move_r = cur_r + dr
            
            else:
                
                move_r = cur_r + dr - N
            
            if cur_c + dc <= N-1:
                
                move_c = cur_c + dc
            
            else:
                
                move_c = cur_c + dc - N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
            
    elif di == 7:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr = si % N
            
            move_r = cur_r
            move_c = cur_c

            if cur_r + dr <= N-1:
                
                move_r = cur_r + dr
            
            else:
                
                move_r = cur_r + dr - N
                
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c]) 
            
    elif di == 8:
        
        for cloud in clouds:
            
            # 구름의 현재위치
            cur_r, cur_c = cloud
            
            dr, dc = si % N, si % N
            
            move_r, move_c = cur_r, cur_c

            if cur_r + dr <= N-1:
                
                move_r = cur_r + dr
            
            else:
                
                move_r = cur_r + dr - N
            
            if cur_c - dc >= 0:
                
                move_c = cur_c - dc
            
            else:
                
                move_c = cur_c - dc + N
            
            A[move_r][move_c] += 1
            exist[move_r][move_c] = True
            move_clouds.append([move_r, move_c])
    
    diag_r = [-1, -1, 1, 1]
    diag_c = [-1, 1, -1, 1]
    
    # 4. 물복사버그 마법 시전, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r,c)에 있는 바구니의 물의 양이 증가
    for move in move_clouds:
        
        r, c = move
        
        diag_water = 0
        
        for t in range(4):
            
            move_r, move_c = r + diag_r[t], c + diag_c[t]
            
            # 주어진 범위를 벗어나지 않을 때만 카운트한다.
            if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                
                # 물이 있다면 카운트한다.
                if A[move_r][move_c] > 0:
                    
                    diag_water += 1
        
        # [r,c]에 있는 바구니의 물의 양이 증가한다.
        A[r][c] += diag_water
    
    # 구름이 모두 사라진다.
    grid = [[0] * N for _ in range(N)]

    # 5. 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(N):
        
        for j in range(N):
            
            if A[i][j] >= 2 and not exist[i][j]:
                
                grid[i][j] = 'C'
                
                A[i][j] -= 2

# N, M이 주어진다.
N, M = map(int, sys.stdin.readline().split())

# 격자 초기화
grid = [[0] * N  for _ in range(N)]

# A : 바구니에 저장되어 있는 물의 양
A = []

# N개의 줄에 N개의 정수가 주어진다.
for _ in range(N):
    
    A.append(list(map(int, sys.stdin.readline().split())))

# 이동 명령
order = []

# M개의 줄에 di, si가 주어진다.
for _ in range(M):
    
    d, s = map(int, sys.stdin.readline().split())
    
    order.append([d, s])

# 비바라기 시전
grid[N-1][0] = 'C'
grid[N-1][1] = 'C'
grid[N-2][0] = 'C'
grid[N-2][1] = 'C'

# M개의 이동 명령
for i in range(M):
    
    # i번째 d, s를 가져온다.
    d, s = order[i]
    
    # 이동함수 실행
    move(d, s)

# 바구니에 들어있는 물의 양의 합 출력
water = 0

for i in range(N):
    
    for j in range(N):
        
        water += A[i][j]

# 답안 출력
print(water)