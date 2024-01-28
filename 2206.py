# 2206 벽 부수고 이동하기

import sys
from collections import deque

# 최단경로를 찾는 알고리즘
def BFS(start):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    queue = deque([[0, start]])
    
    # 시작지점은 초기화
    visited[0][0][0] = 1
    visited[1][0][0] = 1
        
    while queue:
        
        wall, cur = queue.popleft()
        
        cur_r, cur_c = cur
        
        for i in range(4):
            
            move_r, move_c = cur_r + dr[i], cur_c + dc[i]
            
            if 0 <= move_r <= N-1 and 0 <= move_c <= M-1 and visited[wall][move_r][move_c] == 0:

                # 이동가능할 때
                if graph[move_r][move_c] == 0:
                    
                    visited[wall][move_r][move_c] = visited[wall][cur_r][cur_c] + 1
                    queue.append([wall, [move_r, move_c]])
                    
                # 벽일 때
                elif graph[move_r][move_c] == '*':
                    
                    # 기존에 부순 벽이 없다면
                    if wall == 0:
                        
                        visited[wall+1][move_r][move_c] = visited[wall][cur_r][cur_c] + 1
                        queue.append([wall+1, [move_r, move_c]])
                    
                    # 기존에 부순 벽이 있다면
                    else:
                        
                        continue
                    
N, M = map(int, sys.stdin.readline().split())

graph = []

# 벽을 안부수고 이동, 부수고 이동한 것을 구분
# visited[0][r][c] = 벽을 안부수고 이동했을 때 [r][c]의 최솟값
# visited[1][r][c] = 벽을 부수고 이동했을 때 [r][c]의 최솟값
visited = []

for _ in range(2):
    
    temp = [[0] * M for _ in range(N)]
    
    visited.append(temp)
    
for _ in range(N):
    
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(N):
    
    for j in range(M):
        
        if graph[i][j] == 1:
            
            graph[i][j] = '*'

# 시작지점
s = [0,0]

# BFS Algorithm 실행
BFS(s)

if visited[0][N-1][M-1] > 0 and visited[1][N-1][M-1]:
    
    print(min(visited[0][N-1][M-1], visited[1][N-1][M-1]))

elif visited[0][N-1][M-1] == 0 and visited[1][N-1][M-1] == 0:
    
    print(-1)

else:
        
    print(max(visited[0][N-1][M-1], visited[1][N-1][M-1]))