# 17143 낚시왕
# 2024-02-07

import sys
from copy import deepcopy

# 상어의 이동 함수
def moving(grid):
    
    # 새로운 격자
    new_grid = [[[] for _ in range(C)] for _ in range(R)]
    
    # 상어가 있을 때 이동한다.
    for r in range(R):
        
        for c in range(C):
            
            if grid[r][c]:
                
                # 속력, 이동 방향, 크기를 꺼낸다.
                s, d, z = grid[r][c][0]
                
                t = s
                
                # 위쪽 방향
                if d == 0:
                    
                    # 현재 위치
                    cur_r = r
                    cur_c = c    

                    # 1초에 s만큼 움직인다.                        
                    while t:
                        
                        move_r = cur_r + dr[d]
                        move_c = cur_c + dc[d]
                        
                        # 주어진 영역 안에 있을 때
                        if 0 <= move_r <= R-1 and 0 <= move_c <= C-1:
                            
                            cur_r = move_r
                            cur_c = move_c
                            
                        # 주어진 영역 밖에 있으면 방향을 바꿉니다.
                        else:
                            
                            # 위쪽이면 아래로 바꾼다.
                            if d == 0:
                                
                                d = 1
                            
                            # 아래쪽이면 위로 바꾼다.
                            elif d == 1:
                                
                                d = 0
                            
                            # 현재위치에서 거꾸로 한칸 갑니다.
                            cur_r = cur_r + dr[d]
                            cur_c = cur_c + dc[d]
                        
                        # 감소
                        t -= 1
                    
                    # 원래 상어의 위치를 지운다.
                    grid[r][c] = []
                    
                    # 새로운 위치에 상어를 추가한다.
                    new_grid[cur_r][cur_c].append((s,d,z))
                
                # 아래쪽 방향 
                elif d == 1:

                    # 현재 위치
                    cur_r = r
                    cur_c = c    

                    # 1초에 s만큼 움직인다.                        
                    while t:
                        
                        move_r = cur_r + dr[d]
                        move_c = cur_c + dc[d]
                        
                        # 주어진 영역 안에 있을 때
                        if 0 <= move_r <= R-1 and 0 <= move_c <= C-1:
                            
                            cur_r = move_r
                            cur_c = move_c
                            
                        # 주어진 영역 밖에 있으면 방향을 바꿉니다.
                        else:
                            
                            # 위쪽이면 아래로 바꾼다.
                            if d == 0:
                                
                                d = 1
                            
                            # 아래쪽이면 위로 바꾼다.
                            elif d == 1:
                                
                                d = 0
                            
                            # 현재위치에서 거꾸로 한칸 갑니다.
                            cur_r = cur_r + dr[d]
                            cur_c = cur_c + dc[d]
                        
                        # 감소
                        t -= 1
                    
                    # 원래 상어의 위치를 지운다.
                    grid[r][c] = []
                    
                    # 새로운 위치에 상어를 추가한다.
                    new_grid[cur_r][cur_c].append((s,d,z))

                # 오른쪽일 때
                elif d == 2:

                    # 현재 위치
                    cur_r = r
                    cur_c = c    

                    # 1초에 s만큼 움직인다.                        
                    while t:
                        
                        move_r = cur_r + dr[d]
                        move_c = cur_c + dc[d]
                        
                        # 주어진 영역 안에 있을 때
                        if 0 <= move_r <= R-1 and 0 <= move_c <= C-1:
                            
                            cur_r = move_r
                            cur_c = move_c
                            
                        # 주어진 영역 밖에 있으면 방향을 바꿉니다.
                        else:
                            
                            # 위쪽이면 아래로 바꾼다.
                            if d == 2:
                                
                                d = 3
                            
                            # 아래쪽이면 위로 바꾼다.
                            elif d == 3:
                                
                                d = 2
                            
                            # 현재위치에서 거꾸로 한칸 갑니다.
                            cur_r = cur_r + dr[d]
                            cur_c = cur_c + dc[d]
                        
                        # 감소
                        t -= 1
                    
                    # 원래 상어의 위치를 지운다.
                    grid[r][c] = []
                    
                    # 새로운 위치에 상어를 추가한다.
                    new_grid[cur_r][cur_c].append((s,d,z))
                    
                elif d == 3:

                    # 현재 위치
                    cur_r = r
                    cur_c = c    

                    # 1초에 s만큼 움직인다.                        
                    while t:
                        
                        move_r = cur_r + dr[d]
                        move_c = cur_c + dc[d]
                        
                        # 주어진 영역 안에 있을 때
                        if 0 <= move_r <= R-1 and 0 <= move_c <= C-1:
                            
                            cur_r = move_r
                            cur_c = move_c
                            
                        # 주어진 영역 밖에 있으면 방향을 바꿉니다.
                        else:
                            
                            # 위쪽이면 아래로 바꾼다.
                            if d == 2:
                                
                                d = 3
                            
                            # 아래쪽이면 위로 바꾼다.
                            elif d == 3:
                                
                                d = 2
                            
                            # 현재위치에서 거꾸로 한칸 갑니다.
                            cur_r = cur_r + dr[d]
                            cur_c = cur_c + dc[d]
                        
                        # 감소
                        t -= 1
                    
                    # 원래 상어의 위치를 지운다.
                    grid[r][c] = []
                    
                    # 새로운 위치에 상어를 추가한다.
                    new_grid[cur_r][cur_c].append((s,d,z))

    # 이동한 후에 크기가 큰 상어가 크기가 작은 상어를 잡아먹는다.
    for r in range(R):
        
        for c in range(C):
            
            # 한 칸에 상어가 2마리 이상 있으면 제일 큰 상어가 나머지를 다 잡아먹는다.
            if len(new_grid[r][c]) > 1:
                
                # 크기가 큰 순으로 정렬
                new_grid[r][c].sort(key = lambda x:-x[2])
                
                # 큰 상어를 제외하고 삭제
                new_grid[r][c]  = [new_grid[r][c][0]]
    
    # 복사
    return new_grid
                
# R, C, M이 주어집니다.
R, C, M = map(int, sys.stdin.readline().split())

# 격자
grid = [[[] for _ in range(C)] for _ in range(R)]

# 이동방향
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 상어의 정보가 주어진다.
for _ in range(M):
    
    # (r,c)는 상어위치, s는 속력, d는 이동 방향, z는 크기
    # 이동방향 1,2,3,4 : 위쪽, 아래쪽, 오른쪽, 왼쪽
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    
    # 위치 조정
    r -= 1
    c -= 1
    
    # 방향 조정
    d -= 1
    
    # (속력, 방향, 크기)
    grid[r][c].append((s, d, z))

# 가장 오른쪽 열로 이동하면 이동을 멈춘다.

# 낚시왕의 위치 초기화
cur_loc = 0

# 낚시왕이 잡은 상어의 크기
ans = 0

# 진행
for _ in range(C):
    
    for i in range(R):
        
        # 상어가 있을 때
        if grid[i][cur_loc]:
            
            s, d, z = grid[i][cur_loc][0]
            
            ans += z
            # 땅과 제일 가까운 상어이므로 잡고 종료
            grid[i][cur_loc] = []
            
            break
    
    # 상어가 이동한다.
    grid = moving(grid)
    
    # 낚시왕의 위치 증가
    cur_loc += 1

# 상어 크기의 합을 출력
print(ans)