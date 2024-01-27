# 20057 마법사 상어와 토네이도

import sys

# 토네이도 함수

def tornado(t_cur, t_dir):
    
    # 전역변수
    global sand_out_of_grid
    
    # 토네이도의 현재좌표
    cur_r, cur_c = t_cur
    
    # 토네이도 방향이 서쪽일 때
    if t_dir == 1:
    
        move_r, move_c = cur_r, cur_c - 1
        
        scatter_dr = [-1, 1, -2, 2, -1, 1, -1, 1, 0]
        scatter_dc = [1, 1, 0, 0, 0, 0, -1, -1, -2]
        
        scattered = 0
        
        for i in range(9):
            
            # 1%
            if i <= 1:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.01))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.01))
                    
            # 2%
            elif i <= 3:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.02))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.02))
                
            # 7%
            elif i <= 5:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.07))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.07))
            # 10%
            elif i <= 7:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.1))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.1))
                
            # 5%
            else:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.05))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.05))
        
        # 남은모래가 이동할 위치
        remain_r, remain_c = move_r, move_c -1
        
        if 0 <= remain_r <= N-1 and 0 <= remain_c <= N-1:
            
            # 남은모래가 이동
            grid[remain_r][remain_c] += (grid[move_r][move_c]-scattered)
        
        else:
            
            sand_out_of_grid += (grid[move_r][move_c]-scattered)
        
        # 모래가 있던 곳은 0으로 초기화
        grid[move_r][move_c] = 0
                
    # 토네이도 방향이 남쪽일 때    
    elif t_dir == 2:

        move_r, move_c = cur_r + 1, cur_c

        scatter_dr = [-1, -1, 0, 0, 0, 0, 1, 1, 2]
        scatter_dc = [-1, 1, -2, 2, -1, 1, -1, 1, 0]
        
        scattered = 0
        
        for i in range(9):
            
            # 1%
            if i <= 1:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.01))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.01))
                    
            # 2%
            elif i <= 3:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.02))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.02))
                
            # 7%
            elif i <= 5:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.07))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.07))
            # 10%
            elif i <= 7:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.1))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.1))
                
            # 5%
            else:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.05))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.05))
        
        # 남은모래가 이동할 위치
        remain_r, remain_c = move_r + 1, move_c
        
        if 0 <= remain_r <= N-1 and 0 <= remain_c <= N-1:
            
            # 남은모래가 이동
            grid[remain_r][remain_c] += (grid[move_r][move_c]-scattered)
        
        else:
            
            sand_out_of_grid += (grid[move_r][move_c]-scattered)
        
        # 모래가 있던 곳은 0으로 초기화
        grid[move_r][move_c] = 0
        
    # 토네이도 방향이 동쪽일 때
    elif t_dir == 3:
        
        move_r, move_c = cur_r, cur_c + 1

        scatter_dr = [-1, 1, -2, 2, -1, 1, -1, 1, 0]
        scatter_dc = [-1, -1, 0, 0, 0, 0, 1, 1, 2]
        
        scattered = 0
        
        for i in range(9):
            
            # 1%
            if i <= 1:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.01))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.01))
                    
            # 2%
            elif i <= 3:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.02))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.02))
                
            # 7%
            elif i <= 5:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.07))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.07))
            # 10%
            elif i <= 7:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.1))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.1))
                
            # 5%
            else:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.05))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.05))
        
        # 남은모래가 이동할 위치
        remain_r, remain_c = move_r, move_c +1
        
        if 0 <= remain_r <= N-1 and 0 <= remain_c <= N-1:
            
            # 남은모래가 이동
            grid[remain_r][remain_c] += (grid[move_r][move_c]-scattered)
        
        else:
            
            sand_out_of_grid += (grid[move_r][move_c]-scattered)
        
        # 모래가 있던 곳은 0으로 초기화
        grid[move_r][move_c] = 0
        
    # 토네이도 방향이 북쪽일 때
    elif t_dir == 4:
    
        move_r, move_c = cur_r - 1, cur_c

        scatter_dr = [1, 1, 0, 0, 0, 0, -1, -1, -2]
        scatter_dc = [-1, 1, -2, 2, -1, 1, -1, 1, 0]
        
        scattered = 0
        
        for i in range(9):
            
            # 1%
            if i <= 1:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.01))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.01))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.01))
                    
            # 2%
            elif i <= 3:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.02))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.02))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.02))
                
            # 7%
            elif i <= 5:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.07))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.07))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.07))
            # 10%
            elif i <= 7:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]
                
                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.1))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.1))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.1))
                
            # 5%
            else:
                
                scatter_r, scatter_c = move_r + scatter_dr[i], move_c + scatter_dc[i]

                if 0 <= scatter_r <= N-1 and 0 <= scatter_c <= N-1:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    grid[scatter_r][scatter_c] += (int(grid[move_r][move_c] * 0.05))
                
                else:
                    
                    scattered += (int(grid[move_r][move_c] * 0.05))
                    sand_out_of_grid += (int(grid[move_r][move_c] * 0.05))

        # 남은모래가 이동할 위치
        remain_r, remain_c = move_r - 1, move_c
        
        if 0 <= remain_r <= N-1 and 0 <= remain_c <= N-1:
            
            # 남은모래가 이동
            grid[remain_r][remain_c] += (grid[move_r][move_c]-scattered)
        
        else:
            
            sand_out_of_grid += (grid[move_r][move_c]-scattered)
        
        # 모래가 있던 곳은 0으로 초기화
        grid[move_r][move_c] = 0
    
    # 토네이도의 이동한 위치
    t_move = [move_r, move_c]
    
    return t_move

# 격자의 크기 N이 주어집니다. N은 홀수
N = int(sys.stdin.readline().rstrip())

# 격자 밖으로 나간 모래의 양
sand_out_of_grid = 0

# 격자
grid = []

# N개의 줄에 격자의 각 칸에 있는 모래가 주어진다.
for _ in range(N):
    
    grid.append(list(map(int, sys.stdin.readline().split())))

cnt = 0

# 시작지점 초기화
cur = [N // 2, N // 2]

# q방향 반복횟수
k = 1

# 방향 : 1(서쪽), 2(남쪽), 3(동쪽), 4(북쪽)
moving = 1

breaken = False

# 토네이도 함수 반복 호출
while True:
    
    if cnt == 2:
        
        k += 1
        cnt = 0
    
    for t in range(k):
        
        # 토네이도 함수
        cur = tornado(cur, moving)
        
        cur_r, cur_c = cur
        
        # [0,0]까지 이동하면 소멸
        if cur_r == 0 and cur_c == 0:
            
            breaken = True
            break
    
    if breaken == True:
        
        break
    
    moving += 1
    
    # 북쪽 다음은 서쪽
    if moving == 5:
        
        moving = 1
    
    # 토네이도 이동 후 cnt 1증가
    cnt += 1

# 답안 출력
print(sand_out_of_grid)