# 17822 원판 돌리기

import sys
from collections import deque

# 회전 함수
def rotate(v):
    
    # xi, di, ki를 가져온다.
    x, d, k = v
    
    # x의 배수인 원판
    for t in range(x, N+1, x):
        
        # 시계방향 회전
        if d == 0:
            
            for _ in range(k):
                
                disc[t-1].rotate()
        
        # 반시계방향 회전
        elif d == 1:
            
            for _ in range(k):
                
                disc[t-1].rotate(-1)
    
    # 삭제해야할 좌표
    remove = []
    
    # 인접하면서 수가 같은 것을 모두 찾는다.
    for i in range(N):
        
        # Rule 1
        if disc[i][0] == disc[i][1] and (disc[i][0] > 0 and disc[i][1] > 0):
            
            remove.append([i,0])
            remove.append([i,1])
        
        # Rule 1  
        if disc[i][0] == disc[i][M-1] and (disc[i][0] > 0 and disc[i][M-1] > 0):
            
            remove.append([i,0])
            remove.append([i,M-1])
        
        # Rule 2
        if disc[i][M-1] == disc[i][M-2] and (disc[i][M-1] > 0 and disc[i][M-2] > 0):
            
            remove.append([i,M-1])
            remove.append([i,M-2])
        
        # Rule 2
        if disc[i][M-1] == disc[i][0] and (disc[i][M-1] > 0 and disc[i][0] > 0):
            
            remove.append([i,M-1])
            remove.append([i,0])
        
        for j in range(M):
            
            # Rule 3
            if 1 <= j <= M-2:
                
                if disc[i][j] == disc[i][j-1] and (disc[i][j] > 0 and disc[i][j-1] > 0):
                    
                    remove.append([i,j])
                    remove.append([i,j-1])
                
                if disc[i][j] == disc[i][j+1] and (disc[i][j] > 0 and disc[i][j+1] > 0):
                    
                    remove.append([i,j])
                    remove.append([i,j+1])

            # Rule 4
            if i == 0:
                
                if disc[0][j] == disc[1][j] and (disc[0][j] > 0 and disc[1][j] > 0):
                    
                    remove.append([0,j])
                    remove.append([1,j])
            
            # Rule 5
            if i == N-1:
                
                if disc[N-1][j] == disc[N-2][j] and (disc[N-1][j] > 0 and disc[N-2][j] > 0):
                    
                    remove.append([N-1,j])
                    remove.append([N-2,j])
            
            # Rule 6
            if 1 <= i <= N-2:
                
                if disc[i][j] == disc[i-1][j] and (disc[i][j] > 0 and disc[i-1][j] > 0):
                    
                    remove.append([i,j])
                    remove.append([i-1,j])
                
                if disc[i][j] == disc[i+1][j] and (disc[i][j] > 0 and disc[i+1][j] > 0):
                    
                    remove.append([i,j])
                    remove.append([i+1,j])

    # 지울 대상이 있을 때 지운다.
    if len(remove) > 0:
        
        for coord in remove:
            
            r, c = coord
            
            disc[r][c] = 0
    
    # 지울 대상이 없을 때
    else:
        
        # 평균을 구한다.
        total = 0
        cnt = 0
        
        for i in range(N):
            
            for j in range(M):
                
                if disc[i][j] > 0:
                    
                    total += disc[i][j]
                    cnt += 1
        
        if cnt == 0:
            
            return
        
        avg = total / cnt
        
        for i in range(N):
            
            for j in range(M):
                
                if disc[i][j] > 0:
                    
                    if disc[i][j] > avg:
                        
                        disc[i][j] -= 1
                    
                    elif disc[i][j] < avg:
                        
                        disc[i][j] += 1
        
# N, M, T가 주어진다.
N, M, T = map(int, sys.stdin.readline().split())

# 원판
disc = []

# N개의 줄에 원판에 적힌 수가 주어진다.
for _ in range(N):
    
    disc.append(deque(list(map(int, sys.stdin.readline().split()))))

# T개의 줄에 xi, di, ki가 주어진다.
var = []
for _ in range(T):
    
    x, d, k = list(map(int, sys.stdin.readline().split()))
    
    var.append((x,d,k))

# 원판을 T번 회전시킨다.
for i in range(T):
    
    # 회전 함수
    rotate(var[i])

# 적힌 수의 합을 출력한다.
total = 0

for i in range(N):
    
    for j in range(M):
        
        total += disc[i][j]
        
print(total)