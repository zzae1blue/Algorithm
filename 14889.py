# 14889 스타트와 링크

# Strategy
# 1. 일단 스타트와 링크 팀 두개로 나눠야한다.
# 2. 각 팀에서 S_ij + S_ji를 계산해야한다.

import sys
from itertools import combinations

# N이 주어집니다.
N = int(sys.stdin.readline().rstrip())

# 1 ~ N번까지의 사람입니다.
num = [i for i in range(1,N+1)]

# N/2를 구합니다.
half = N // 2

# S를 초기화합니다.
S = []

# N개의 줄에 따라 S가 주어집니다.
for _ in range(N):

    S.append(list(map(int, sys.stdin.readline().split())))

# 스타트와 링크 팀을 구성합니다.
team_start = list(combinations(num, half))
team_link = []

for team in team_start:

    num_temp = [i for i in range(1,N+1)]

    for k in range(half):

        if team[k] in num_temp:

            num_temp.remove(team[k])
    
    team_link.append(tuple(num_temp))

# 능력치 차이의 최솟값
min_diff_stats = 999999999

# 각 팀의 능력치를 계산합니다.
for i in range(len(team_start)):

    num_pair_start = list(combinations(team_start[i], 2))
    num_pair_link = list(combinations(team_link[i], 2))

    sum_pair_start = 0
    sum_pair_link = 0

    for pair in num_pair_start:

        m, n = pair
        sum_pair_start += (S[m-1][n-1]+S[n-1][m-1])
    
    for pair in num_pair_link:

        m, n =pair
        sum_pair_link += (S[m-1][n-1]+S[n-1][m-1])
    
    min_diff_stats = min(min_diff_stats, abs(sum_pair_start-sum_pair_link))

print(min_diff_stats)