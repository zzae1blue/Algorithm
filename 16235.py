# 16235 나무 재테크

import sys

# N, M, K가 주어진다.
N, M, K = map(int, sys.stdin.readline().split())

# N X N 땅의 양분 : 처음에는 모든 칸에 5만큼 들어있다.
energy = [[5] * N for _ in range(N)]

# 8개 방향
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# N개의 줄에 A배열의 값이 주어진다.
A = []

for _ in range(N):
    
    A.append(list(map(int, sys.stdin.readline().split())))

# M개의 줄에 상도가 심은 나무의 정보를 나타내는 세 정수 x,y,z가 주어진다.
# 처음 두 개의 정수는 나무의 위치 (x,y), 마지막 정수는 그 나무의 나이 z
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    
    x, y, z = map(int, sys.stdin.readline().split())
    
    x -= 1
    y -= 1
    
    tree[x][y].append(z)

# K년이 지난 후 살아남은 나무의 수를 출력
# K년 동안 반복
while K > 0:
    
    for i in range(N):
        
        for j in range(N):
            
            # 증가하는 에너지양
            inc = 0
            
            # 어린 나무 순으로 정렬
            tree[i][j].sort()
            
            # 죽은 나무 개수
            death = 0
            
            for k in range(len(tree[i][j])):
                
                # 봄일 때
                # 나이만큼 양분을 먹는다.
                if tree[i][j][k] <= energy[i][j]:
                    
                    energy[i][j] -= tree[i][j][k]
                    
                    # 나이를 한살 먹는다.
                    tree[i][j][k] += 1
                
                # 여름일 때, 에너지가 부족하면 나무가 죽는다. 죽은 나무는 양분이 된다.
                else:
                    
                    # 양분 전환
                    inc += (tree[i][j][k] // 2)
                    
                    death += 1
                
            for _ in range(death):
                
                # 해당 나무는 제거
                del tree[i][j][-1]
            
            energy[i][j] += inc
    
    # 가을일 때
    # 나무가 번식한다
    for i in range(N):
        
        for j in range(N):
        
            for k in range(len(tree[i][j])):
                
                # 5의 배수면 인접한 8개의 칸에 나무가 1인 나무가 생긴다.
                if tree[i][j][k] % 5 == 0:
                    
                    for t in range(8):
                        
                        move_r, move_c = i + dr[t], j + dc[t]
                        
                        # 주어진 범위를 벗어나지 않을 때
                        if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                            
                            tree[move_r][move_c].append(1)
                            
    # 겨울일 때
    for i in range(N):
        
        for j in range(N):
            
            energy[i][j] += A[i][j]
            
    # 1년 경과
    K -= 1

# 살아있는 나무의 개수를 구합니다.
cnt = 0
for i in range(N):
    
    for j in range(N):
        
        cnt += len(tree[i][j])

# 답안 출력
print(cnt)