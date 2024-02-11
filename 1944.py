# 1944 복제 로봇

import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

def BFS(start, graph_v):
    
    # 4방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 큐 생성
    queue = deque([start])
    
    # 시작지점
    start_r, start_c = start
    
    # 시작지점 처리
    graph_v[start_r][start_c] = 0
    
    # 큐가 빌 때까지 반복
    while queue:
        
        cur_r, cur_c = queue.popleft()
        
        # 4방향
        for i in range(4):
            
            move_r, move_c = cur_r + dr[i], cur_c + dc[i]
            
            # 주어진 영역을 벗어나지 않을 때
            if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                
                # 벽이 아닐 때 각 지점까지의 최소거리를 구합니다.
                if graph_v[move_r][move_c] == 'S' or graph_v[move_r][move_c] == '0' or graph_v[move_r][move_c] == 'K':
                    
                    graph_v[move_r][move_c] = graph_v[cur_r][cur_c] + 1
                    
                    # 큐에 추가
                    queue.append([move_r, move_c])

def prim(start):
    
    # 전체비용
    total = 0
    
    # 간선의 수
    edge = 0
    
    # 우선순위 큐
    q = []
    
    # MST
    mst = set()
    
    # 시작노드 처리
    mst.add(start)
    
    # 시작노드와 이어진 간선을 후보군에 넣는다.
    for neighbor in graph[start]:
        
        heappush(q, (neighbor[1], neighbor[0]))
    
    # 큐가 빌 때까지 반복
    while q:
        
        cost, cur = heappop(q)
        
        # 사이클을 형성하는 조건
        if cur in mst:
            
            continue
        
        else:
            
            # 비용 누적
            total += cost
            
            # 간선 누적
            edge += 1
            
            # 간선의 수가 MST를 만족하면 break
            if edge == M:
                
                break
            
            # MST에 추가
            mst.add(cur)
            
            # cur와 이어진 간선
            for neighbor in graph[cur]:
                
                if neighbor[0] not in mst:
                    
                    heappush(q, (neighbor[1], neighbor[0]))

    # 전체비용 출력
    if edge == M:
        
        print(total)
    
    else:
        
        print(-1)
             
# 미로의 크기 N과 열쇠의 개수 M이 주어진다.
N, M = map(int, sys.stdin.readline().split())

# 그래프 (출발위치 S와 열쇠의 개수M, 총 M+1개)
graph = [[] for _ in range(M+1)]

# 미로 초기화
maze = []

# 미로의 정보가 주어진다.
for _ in range(N):
    
    maze.append(list(sys.stdin.readline().rstrip()))

# 로봇의 출발 위치와 열쇠의 위치를 찾습니다.
locs = []
for i in range(N):
    
    for j in range(N):
        
        if maze[i][j] == 'S' or maze[i][j] == 'K':
            
            locs.append([i,j])

# 모든 위치에 대하여 거리를 계산합니다.
for i in range(len(locs)):
    
    # 원본 미로 복사    
    maze_copy = deepcopy(maze)
    
    # BFS Algorithm
    BFS(locs[i], maze_copy)
    
    # 각 지점까지의 거리를 계산하여 그래프에 반영합니다.
    for j in range(len(locs)):
        
        # 두 좌표가 같지 않을 때만
        if i != j:
            
            r, c = locs[j]
            
            if type(maze_copy[r][c]) == int:
                
                # 두 점 사이의 거리
                graph[i].append((j, maze_copy[r][c]))
            
            else:
                
                continue

# Prim Algorithm
prim(0)