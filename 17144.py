# 17144 미세먼지 안녕!
import sys
from math import floor

# R, C, T가 주어집니다.
R, C, T = map(int, sys.stdin.readline().split())

# 집
home = []

# R개의 줄에 A_r,c가 주어진다.
for _ in range(R):
    
    home.append(list(map(int, sys.stdin.readline().split())))

# 미세먼지가 설치된 곳을 찾는다.
air_cleaner = []

for i in range(R):
    
    for j in range(C):
        
        if home[i][j] == -1:
            
            air_cleaner.append([i,j])

# 4방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# T초 동안 반복합니다.
while T > 0:
    
    dust = []
    
    # 1초 감소
    T -= 1
    
    # 미세먼지가 있는 곳을 파악, 미세먼지의 양과 같이 저장
    for i in range(R):
        
        for j in range(C):
            
            if home[i][j] > 0:
                
                dust.append([i,j, home[i][j]])
    
    # 미세먼지 확산
    for k in range(len(dust)):
        
        # 미세먼지가 있는 좌표, 미세먼지 값
        r, c, val = dust[k]
        
        # 몇 개의 방향으로 퍼졌는지 확인
        cnt = 0
        
        # 4방향 확산
        for t in range(4):
            
            new_r, new_c = r + dr[t], c + dc[t]
            
            # 공기 청정기가 없는 위치이고 주어진 범위를 벗어나지않을때, 방향을 카운트하고 미세먼지를 전파한다.
            if 0 <= new_r <= R-1 and 0 <= new_c <= C-1 and home[new_r][new_c] != -1:
                
                home[new_r][new_c] += floor(val/5)

                cnt += 1

            # 공기 청정기가 있는 위치라면 방향을 카운트하지 않는다. 미세먼지도 전파하지 않는다.
        
        # 전파 후 현재 위치의 남은 미세먼지 양 
        home[r][c] -= (floor(val/5) * cnt)
    
    # 공기 청정기 작동
    for i in range(2):
        
        # 위쪽 공기청정기 : 반시계방향으로 순환한다.
        if i == 0:
            
            # 공기 청정기의 좌표
            r, c = air_cleaner[i]
            
            # 위쪽 공기청정기의 위치가 첫번째 열일 때
            if r == 0:
                
                for m in range(C-1, 0, -1):
                    
                    if m == 1:
                        
                        home[r][m] = 0
                    
                    else:
                        
                        home[r][m] = home[r][m-1]
                                    
            elif r > 0:
                
                values = [home[r][C-1], home[0][C-1], home[0][0]]
                
                for m in range(C-1, 0, -1):
                    
                    if m == 1:
                        
                        home[r][m] = 0
                    
                    else:
                        
                        home[r][m] = home[r][m-1]
                
                for m in range(0, r):
                    
                    home[m][C-1] = home[m+1][C-1]
                
                home[r-1][C-1] = values[0]
                
                for m in range(0, C-1):
                    
                    home[0][m] = home[0][m+1]
                
                home[0][C-2] = values[1]
                
                for m in range(r-1, 0, -1):
                    
                    home[m][0] = home[m-1][0]
                
                home[1][0] = values[2]
                
        # 아래쪽 공기청정기 : 시계방향으로 순환한다.    
        if i == 1:
            
            # 공기 청정기의 좌표
            r, c = air_cleaner[i]
            
            # 아래쪽 공기청정기의 위치가 마지막 열일 때
            if c == R-1:
                
                for m in range(C-1, 0, -1):
                    
                    if m == 1:
                        
                        home[r][m] = 0
                    
                    else:
                        
                        home[r][m] = home[r][m-1]
                                       
            elif c < R-1:
                
                values = [home[r][C-1], home[R-1][C-1], home[R-1][0]]
                
                for m in range(C-1, 0, -1):
                    
                    if m == 1:
                        
                        home[r][m] = 0
                    
                    else:
                        
                        home[r][m] = home[r][m-1]

                for m in range(R-1, r, -1):
                    
                    home[m][C-1] = home[m-1][C-1]
                
                home[r+1][C-1] = values[0]
                
                for m in range(0, C-1):
                    
                    home[R-1][m] = home[R-1][m+1]
                
                home[R-1][C-2] = values[1]
                
                for m in range(r+1, R-1):
                    
                    home[m][0] = home[m+1][0]
                
                home[R-2][0] = values[2]

ans = 0

for i in range(R):
    
    for j in range(C):
        
        if home[i][j] > 0:
            
            ans += home[i][j]
            
print(ans)          