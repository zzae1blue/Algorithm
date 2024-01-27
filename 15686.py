# 15686 치킨 배달

import sys
from itertools import combinations

# N과 M이 주어집니다.
N, M = map(int, sys.stdin.readline().split())

# 도시 초기화
city = []

# N개의 줄에 도시의 정보가 주어집니다.
for _ in range(N):

    city.append(list(map(int, sys.stdin.readline().split())))

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
# 도시의 치킨거리는 모든 집의 치킨거리의 합이다.

# Strategy
# 1. 치킨집을 최대 M개 고르자. 조합(Combination)을 통해 구하자.
# 2. 도시의 치킨거리를 구하고 최솟값을 얻을 때 까지 계속 갱신한다.

# 집과 치킨집의 좌표
chicken_loc = []
home_loc = []

# 집과 치킨집의 좌표를 전부 찾습니다.
for i in range(N):

    for j in range(N):

        if city[i][j] == 2:

            loc = [i,j]
            chicken_loc.append(loc)

        elif city[i][j] == 1:

            loc = [i,j]
            home_loc.append(loc)

# M개의 치킨집 조합을 구합니다.
chicken_comb = list(combinations(chicken_loc, M))

# 도시의 치킨거리의 최소값
city_d = 99999

# 각 조합에 대해서 도시의 치킨거리를 구합니다.
for comb in chicken_comb:
    
    # 각 조합에 대해서 치킨 거리의 총합
    comb_d = 0

    # 각 집에서 치킨집과의 거리 최솟값을 구합니다.
    for home in home_loc:

        home_chicken_d = 99999
        home_r, home_c = home

        for chicken in comb:

            chicken_r, chicken_c = chicken

            # 각 집의 치킨거리를 구합니다.
            dist = abs(home_r-chicken_r) + abs(home_c-chicken_c)
            
            home_chicken_d = min(home_chicken_d, dist)
        
        comb_d += home_chicken_d
    
    city_d = min(city_d, comb_d)

# 답안 출력
print(city_d)