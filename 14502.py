# 14502 연구소

# Strategy
# 1. 모든 빈칸 중에 3개를 선택해서 벽을 세우는 케이스를 구한다. (조합)
# 2. 벽을 세워보고 BFS 알고리즘을 수행하여 바이러스를 전파시킨다.
# 3. 안전영역의 개수를 세고 최대값을 구할 때 까지 갱신한다.

import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

def BFS(cur):
    
    # 상하좌우를 나타냅니다.
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # Queue를 생성합니다.
    queue = deque([cur])

    # Queue가 빌 때까지 반복합니다.
    while queue:

        # Queue에서 바이러스의 좌표를 뽑습니다.
        cur_r, cur_c = queue.popleft()

        # 4방향에 대해서 조사합니다.
        for i in range(4):

            move_r = cur_r + dr[i]
            move_c = cur_c + dc[i]

            # 지도의 범위를 벗어나지 않으면서, 이동하려는 칸이 빈칸일 때
            if 0 <= move_r <= N-1 and 0 <= move_c <= M-1:
                if area_temp[move_r][move_c] == 0:
                    
                    # 바이러스를 전파시킵니다.
                    area_temp[move_r][move_c] = 2
                    new_loc = [move_r, move_c]
                    queue.append(new_loc)

# 지도의 세로크기 N과 가로크기 M이 주어집니다.
N, M = map(int, sys.stdin.readline().split())


# 지도를 초기화합니다.
area = []

# N개의 줄에 지도의 모양이 주어집니다. 0은 빈칸, 1은 벽, 2는 바이러스
for _ in range(N):

    area.append(list(map(int, sys.stdin.readline().split())))

# 빈 공간의 좌표를 담는 List
empty_space = []

# 바이러스가 있는 좌표
virus_space = []

# 지도를 순회하면서 빈 영역과 바이러스가 있는 곳을 찾아냅니다.
for i in range(N):

    for j in range(M):

        if area[i][j] == 0:

            loc = [i,j]
            empty_space.append(loc)

        elif area[i][j] == 2:

            loc = [i,j]
            virus_space.append(loc)

# 벽을 세우는 case를 모두 구합니다. 빈칸의개수_C_3
wall_comb = list(combinations(empty_space, 3))

# 안전영역의 최대값을 초기화
max_safe_zone_count = -1

# 각각의 케이스에 대해서 벽을 세우고 바이러스를 전파합니다.
for wall in wall_comb:

    safe_zone_count = 0

    # 지도를 복사합니다.
    area_temp = deepcopy(area)

    # 벽 3개를 세웁니다. 0을 1로 변경
    for i in range(3):

        r, c = wall[i]

        area_temp[r][c] = 1
    
    # 벽을 세운 후 바이러스 전파
    for loc in virus_space:
        
        BFS(loc)
    
    for i in range(N):

        for j in range(M):

            if area_temp[i][j] == 0:

                safe_zone_count += 1
    
    max_safe_zone_count = max(max_safe_zone_count, safe_zone_count)

# 답안 출력
print(max_safe_zone_count)