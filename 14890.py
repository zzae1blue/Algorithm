# 14890 경사로
# 2024-02-11

import sys

# 지나갈 수 있는 길인지 판단하는 함수
def cross(array):
    
    # 모든 높이가 같으면 지날 수 있습니다.
    if len(list(set(array))) == 1:
        
        return 1
    
    # 높이차가 2 이상일 때 지나갈 수 없습니다.
    for i in range(N-1):
    
        if abs(array[i] - array[i+1]) >= 2:
            
            return 0
    
    # 이웃한 지면끼리 높이차가 2미만일 때
    # 경사로를 놓을 수 있는지 조사합니다.
    
    temp = [0] * N
    
    # 처음 유효칸 1
    temp[0] = 1
    
    for i in range(N-1):
        
        cur = array[i]
        nxt = array[i+1]
        
        # 이웃한 것이 같으면 유효칸 1 증가
        if cur == nxt:
            
            temp[i+1] = temp[i] + 1
        
        # 다음 계단이 더 높을 때
        elif cur < nxt:
            
            # 경사로 쌓을 수 있을 때
            if temp[i] >= L:
                
                # 유효칸 1로 초기화 후 계속 진행
                temp[i+1] = 1
                
                continue
            
            # 경사로 쌓을 수 없을 때
            else: # low < L
                
                # 종료
                return 0
        
        # 다음 계단이 더 낮을 때
        elif cur > nxt:
            
            if temp[i] < 0:
                
                return 0
            
            else:
            
                temp[i+1] = 1-L
                continue
    
    # array의 마지막 원소가 0보다 크거나 같다면 길 생성 가능
    if temp[-1] >= 0:
        
        return 1
    
    else:
        
        return 0
    
# N, L이 주어집니다.
N, L = map(int, sys.stdin.readline().split())

# 지도
grid = []

# N개의 줄에 지도가 주어집니다.
for _ in range(N):
    
    grid.append(list(map(int, sys.stdin.readline().split())))

# 지나갈 수 있는 길의 개수
ans = 0

# 행을 살펴봅니다.
for i in range(N):
    
    road = grid[i]
    
    # 건널 수 있는 길인지 판단합니다.
    ans += cross(road)
    
# 열을 살펴봅니다.
for i in range(N):
    
    road = []
    
    for j in range(N):
        
        road.append(grid[j][i])
    
    # 건널 수 있는 길인지 판단합니다.
    ans += cross(road)
    
# 지나갈 수 있는 길의 개수를 출력한다.
print(ans)