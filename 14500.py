# 14500 테트로미노
# 2024-02-04

import sys

# N, M이 주어진다.
N, M = map(int, sys.stdin.readline().split())

# 격자
grid = []

# N개의 줄에 종이에 쓰여 있는 수가 주어진다.
for _ in range(N):
    
    grid.append(list(map(int, sys.stdin.readline().split())))

# 최댓값 변수
max_sum = -1

# 1번 테트로미노
for r in range(N):
    
    for c in range(M):
        
        # 기준 좌표
        std_r = r
        std_c = c
        
        coords_1 = [[r,c], [r, c+1], [r, c+2], [r, c+3]]
        coords_2 = [[r,c], [r+1,c], [r+2,c], [r+3,c]]
        
        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_1:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_1:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        possible = True
        
        for coord in coords_2:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_2:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

# 2번 테트로미노
for r in range(N):
    
    for c in range(M):
        
        std_r = r
        std_c = c
        
        coords_1 = [[r,c], [r, c+1], [r+1, c], [r+1, c+1]]
        
        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_1:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_1:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

# 3번 테트로미노
for r in range(N):
    
    for c in range(M):
        
        std_r = r
        std_c = c
        
        coords_1 = [[r,c], [r+1, c], [r+2, c], [r+2, c+1]]
        coords_2 = [[r,c], [r,c+1], [r,c+2], [r+1,c]]
        coords_3 = [[r,c], [r,c+1], [r+1,c+1], [r+2,c+1]]
        coords_4 = [[r,c], [r,c+1], [r,c+2], [r-1,c+2]]
        coords_5 = [[r,c], [r+1,c], [r+2,c], [r+2,c-1]]
        coords_6 = [[r,c], [r+1,c], [r+1,c+1], [r+1,c+2]]
        coords_7 = [[r,c], [r,c-1], [r+1, c-1], [r+2, c-1]]
        coords_8 = [[r,c], [r,c+1], [r,c+2], [r+1,c+2]]
        
        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_1:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_1:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_2:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_2:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_3:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_3:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_4:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_4:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_5:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_5:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_6:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_6:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_7:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_7:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_8:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_8:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

# 4번 테트로미노
for r in range(N):
    
    for c in range(M):
        
        std_r = r
        std_c = c
        
        coords_1 = [[r,c], [r+1,c], [r+1,c+1], [r+2,c+1]]
        coords_2 = [[r,c], [r,c+1], [r-1,c+1], [r-1,c+2]]
        coords_3 = [[r,c], [r+1,c], [r+1,c-1], [r+2,c-1]]
        coords_4 = [[r,c], [r,c+1], [r+1,c+1], [r+1,c+2]]
        
        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_1:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_1:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_2:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_2:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_3:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_3:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_4:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_4:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

# 5번 테트로미노
# 4번 테트로미노
for r in range(N):
    
    for c in range(M):
        
        std_r = r
        std_c = c
        
        coords_1 = [[r,c], [r+1, c-1], [r+1,c], [r+1,c+1]]
        coords_2 = [[r,c], [r,c-1], [r-1,c-1], [r+1,c-1]]
        coords_3 = [[r,c], [r,c-1], [r,c+1], [r+1,c]]
        coords_4 = [[r,c], [r,c+1], [r-1, c+1], [r+1,c+1]]
        
        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_1:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_1:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_2:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_2:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_3:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_3:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

        # 계산가능한 좌표인지 여부
        possible = True
        
        for coord in coords_4:
            
            i, j = coord
            
            # 주어진 범위를 벗어나지 않을 때
            if 0 <= i <= N-1 and 0 <= j <= M-1:
                
                continue
            
            else:
                
                possible = False
                break
        
        # 점수 계산이 가능할 때
        sum_val = 0
        
        if possible:
            
            for coord in coords_4:
                
                i, j = coord
                
                sum_val += grid[i][j]
        
        # 최댓값 갱신
        max_sum = max(max_sum, sum_val)

# 답안 출력
print(max_sum)