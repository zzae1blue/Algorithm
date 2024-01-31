# 2887 행성 터널

import sys
from heapq import heappush, heappop

def prim(start):

    # MST 비용
    total = 0

    # 간선 선택 횟수
    edge = 0

    # 우선순위 큐
    q = []

    # 포함된 행성 리스트
    mst = set()

    # 시작노드 처리
    mst.add(start)

    # 시작노드와 붙어있는 간선을 큐에 추가 (비용, 노드)
    for neighbor in planet[start]:

        heappush(q, (neighbor[1], neighbor[0]))
    
    # 큐가 빌 때까지 반복
    while q:

        # 비용과 행성꺼내기
        cost, cur = heappop(q)

        # 리스트에 이미 포함되어있으면 skip
        if cur in mst:

            continue
        
        else:

            # 전체 비용에 누적
            total += cost

            # 간선 선택 1회 추가
            edge += 1

            # MST에 노드 추가
            mst.add(cur)

            # N-1개의 간선이 획득되면 최소 스패닝 트리 만족, 종료
            if edge == N-1:

                break

            # cur의 이웃들을 살펴봅니다.
            for neighbor in planet[cur]:
                
                # mst 구성되지 않은 노드는 후보에 추가
                if neighbor[0] not in mst:

                    heappush(q, (neighbor[1], neighbor[0]))

    # 전체 간선 비용
    print(total)

# 행성의 개수 N이 주어집니다.
N = int(sys.stdin.readline().rstrip())

# 행성 좌표 셋
planet_loc = []

# 행성 (0번 ~ N-1번)
planet = [[] for _ in range(N)]

# 각 행성의 x, y, z좌표가 주어진다.
for i in range(N):

    x, y, z = map(int, sys.stdin.readline().split())

    planet_loc.append([x,y,z,i])

# x,y,z좌표에 대한 오름차순 정렬
planet_loc_x_sort = sorted(planet_loc, key=lambda t:t[0])
planet_loc_y_sort = sorted(planet_loc, key=lambda t:t[1])
planet_loc_z_sort = sorted(planet_loc, key=lambda t:t[2])

# 간선 추가(x좌표 인접 기준)
for i in range(N-1):

    x_cost = abs(planet_loc_x_sort[i+1][0]-planet_loc_x_sort[i][0])
    
    n1, m1 = planet_loc_x_sort[i+1][-1], planet_loc_x_sort[i][-1]

    planet[n1].append((m1, x_cost))
    planet[m1].append((n1, x_cost))

    y_cost = abs(planet_loc_y_sort[i+1][1]-planet_loc_y_sort[i][1])

    n2, m2 = planet_loc_y_sort[i+1][-1], planet_loc_y_sort[i][-1]

    planet[n2].append((m2, y_cost))
    planet[m2].append((n2, y_cost))

    z_cost = abs(planet_loc_z_sort[i+1][2]-planet_loc_z_sort[i][2])

    n3, m3 = planet_loc_z_sort[i+1][-1], planet_loc_z_sort[i][-1]

    planet[n3].append((m3, z_cost))
    planet[m3].append((n3, z_cost))

# Prim Algorithm Execute
prim(0)