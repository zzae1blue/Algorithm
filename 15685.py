# 15685 드래곤 커브

import sys

# 드래곤 커브의 개수 N이 주어진다.
N = int(sys.stdin.readline().rstrip())

# N개의 줄에 드래곤 커브의 정보가 주어진다.
curves = []

# 격자 초기화
grid = [[0] * 101 for _ in range(101)]

for _ in range(N):
    
    # x, y는 드래곤 커브의 시작 지점, d는 시작 방향, g는 세대
    # 방향 : 0(→), 1(↑), 2(←), 3(↓)
    x, y, d, g = map(int, sys.stdin.readline().split())
    
    curves.append([x,y,d,g])

# 각 드래곤 커브를 격자위에 그린다.
for curve in curves:
    
    # 커브 정보를 가져온다.
    x, y, d, g = curve
    
    r = y
    c = x
    # 드래곤 커브의 점
    points = [[r,c]]
    
    # 시작점 반영
    grid[r][c] = 1
    
    # 방향에 따라 반영
    # →
    if d == 0:
        
       grid[r][c+1] = 1
       points.append([r,c+1])
       end_p = [r,c+1]
       
    # ↑
    elif d == 1:
        
        grid[r-1][c] = 1
        points.append([r-1,c])
        end_p = [r-1, c]
        
    # ← 
    elif d == 2:
        
        grid[r][c-1] = 1
        points.append([r,c-1])
        end_p = [r,c-1]
        
    # ↓  
    elif d == 3:
        
        grid[r+1][c] = 1
        points.append([r+1,c])
        end_p = [r+1, c]
                
    # g세대 만큼 반복한다.
    for _ in range(g):
        
        # 끝점을 가져옵니다.
        end_r, end_c = end_p
        
        # 끝점을 빼고 나머지는 끝점을 기준으로 시계방향으로 회전시킨다.
        for i in range(len(points)):
            
            if [end_r, end_c] == points[i]:
                
                continue
            
            cur_r, cur_c = points[i]
            
            new_r = (cur_c-end_c) + end_r
            new_c = -(cur_r-end_r) + end_c
                 
            if i == 0:
                
                end_p = [new_r, new_c]
            
            points.append([new_r, new_c])
            
            grid[new_r][new_c] = 1

square = 0
# 사각형의 개수를 셉니다
for i in range(100):
    
    for j in range(100):
        
        if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
            
            square += 1

# 답안 출력
print(square)