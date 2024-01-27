# 15683 감시

import sys
from itertools import product
from copy import deepcopy

# 사무실의 세로 크기 N과 가로 크기 M이 주어집니다.
N, M = map(int, sys.stdin.readline().split())

# 사무실
office = []

# N개의 줄에 사무실 각 칸의 정보가 주어진다. 0 : 빈칸, 6 : 벽, 1 ~ 5 : CCTV
for _ in range(N):
    
    office.append(list(map(int, sys.stdin.readline().split())))

# 사각지대의 최소 크기를 구한다.

# CCTV의 위치를 구한다 : (CCTV 번호, 위치, 방향개수에 따른 리스트)
cctvs = []
directions = []

for i in range(N):
    
    for j in range(M):
        
        if 1 <= office[i][j] <= 5:
            
            if office[i][j] == 1:
                
                cctvs.append([office[i][j], [i,j]])
                directions.append([1,2,3,4])
            
            elif office[i][j] == 2:
                
                cctvs.append([office[i][j], [i,j]])
                directions.append([1,2])
            
            elif office[i][j] == 3:
                
                cctvs.append([office[i][j], [i,j]])
                directions.append([1,2,3,4])
            
            elif office[i][j] == 4:
                
                cctvs.append([office[i][j], [i,j]])
                directions.append([1,2,3,4])
            
            else: # office[i][j] == 5
                
                cctvs.append([office[i][j], [i,j]])
                directions.append([1])

# 모든 케이스를 구합니다.
cases = list(product(*directions))

# 최소 사각지대 변수 초기화
min_blind_spot = int(1e10)

# 모든 케이스에 따라 계산하여 최소 사각지대를 구합니다.
for each in cases:
    
    # 사무실 리스트 복사
    copied = deepcopy(office)
    
    for i in range(len(each)):
        
        # cctv를 가져옵니다.
        cctv_num, coord = cctvs[i]
        
        # 방향을 가져옵니다.
        direction = each[i]
        
        # 1번 cctv일 때
        if cctv_num == 1:
            
            # 방향이 북쪽일 때
            if direction == 1:
                
                cur_r, cur_c = coord
                
                move_r, move_c = cur_r, cur_c
                
                while True:
                    
                    move_r, move_c = move_r - 1, move_c
                    
                    if 0 <= move_r <= N-1 and 0 <= move_c <= M-1:
                        
                        if copied[move_r][move_c] == 0:
                            
                            copied[move_r][move_c] = '#'
                            continue
                        
                        elif copied[move_r][move_c] == 6:
                            
                            break
                        
                        else: # 1 <= copied[move_r][move_c] <= 5 or copied[move_r][move_c] == '#'
                            
                            continue
                                         
                    else:
                        
                        break
            
            # 방향이 동쪽일 때
            elif direction == 2:
                
                cur_r, cur_c = coord
                
                move_r, move_c = cur_r, cur_c
                
                while True:
                    
                    move_r, move_c = move_r, move_c + 1
                    
                    if 0 <= move_r <= N-1 and 0 <= move_c <= M-1:
                        
                        if copied[move_r][move_c] == 0:
                            
                            copied[move_r][move_c] = '#'
                            continue
                        
                        elif copied[move_r][move_c] == 6:
                            
                            break
                        
                        else: # 1 <= copied[move_r][move_c] <= 5 or copied[move_r][move_c] == '#'
                            
                            continue
                                         
                    else:
                        
                        break
            
            # 방향이 남쪽일 때
            elif direction == 3:

                cur_r, cur_c = coord
                
                move_r, move_c = cur_r, cur_c
                
                while True:
                    
                    move_r, move_c = move_r + 1, move_c
                    
                    if 0 <= move_r <= N-1 and 0 <= move_c <= M-1:
                        
                        if copied[move_r][move_c] == 0:
                            
                            copied[move_r][move_c] = '#'
                            continue
                        
                        elif copied[move_r][move_c] == 6:
                            
                            break
                        
                        else: # 1 <= copied[move_r][move_c] <= 5 or copied[move_r][move_c] == '#'
                            
                            continue
                                         
                    else:
                        
                        break
            
            # 방향이 서쪽일 때
            elif direction == 4:
                
                cur_r, cur_c = coord
                
                move_r, move_c = cur_r, cur_c
                
                while True:
                    
                    move_r, move_c = move_r, move_c - 1
                    
                    if 0 <= move_r <= N-1 and 0 <= move_c <= M-1:
                        
                        if copied[move_r][move_c] == 0:
                            
                            copied[move_r][move_c] = '#'
                            continue
                        
                        elif copied[move_r][move_c] == 6:
                            
                            break
                        
                        else: # 1 <= copied[move_r][move_c] <= 5 or copied[move_r][move_c] == '#'
                            
                            continue
                                         
                    else:
                        
                        break
        
        # 2번 CCTV일 때
        elif cctv_num == 2:
            
            # ←, →
            if direction == 1:
            
                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 - 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2, move_c_2 + 1
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ↑, ↓    
            elif direction == 2:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1 - 1, move_c_1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 + 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
                        
        elif cctv_num == 3:

            # ↑, →
            if direction == 1:
                
                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1 - 1, move_c_1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2, move_c_2 + 1
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # →, ↓
            elif direction == 2:
                
                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 + 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 + 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ↓, ←
            elif direction == 3:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1 + 1, move_c_1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2, move_c_2 - 1
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ←, ↑
            elif direction == 4:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 - 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 - 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
                    
        elif cctv_num == 4:

            # ←, ↑, →
            if direction == 1:
                
                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                move_r_3, move_c_3 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1 - 1, move_c_1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2, move_c_2 + 1
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_3, move_c_3 = move_r_3, move_c_3 - 1
                    
                    if 0 <= move_r_3 <= N-1 and 0 <= move_c_3 <= M-1:
                        
                        if copied[move_r_3][move_c_3] == 0:
                            
                            copied[move_r_3][move_c_3] = '#'
                            continue
                        
                        elif copied[move_r_3][move_c_3] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ↑, →, ↓
            elif direction == 2:
                
                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                move_r_3, move_c_3 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 + 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 + 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_3, move_c_3 = move_r_3 - 1, move_c_3
                    
                    if 0 <= move_r_3 <= N-1 and 0 <= move_c_3 <= M-1:
                        
                        if copied[move_r_3][move_c_3] == 0:
                            
                            copied[move_r_3][move_c_3] = '#'
                            continue
                        
                        elif copied[move_r_3][move_c_3] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ↓, ←, →
            elif direction == 3:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                move_r_3, move_c_3 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1 + 1, move_c_1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2, move_c_2 - 1
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_3, move_c_3 = move_r_3, move_c_3 + 1
                    
                    if 0 <= move_r_3 <= N-1 and 0 <= move_c_3 <= M-1:
                        
                        if copied[move_r_3][move_c_3] == 0:
                            
                            copied[move_r_3][move_c_3] = '#'
                            continue
                        
                        elif copied[move_r_3][move_c_3] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
            
            # ←, ↑, ↓
            elif direction == 4:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                move_r_3, move_c_3 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 - 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 - 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_3, move_c_3 = move_r_3 + 1, move_c_3
                    
                    if 0 <= move_r_3 <= N-1 and 0 <= move_c_3 <= M-1:
                        
                        if copied[move_r_3][move_c_3] == 0:
                            
                            copied[move_r_3][move_c_3] = '#'
                            continue
                        
                        elif copied[move_r_3][move_c_3] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
                    
        elif cctv_num == 5:

                cur_r, cur_c = coord
                
                move_r_1, move_c_1 = cur_r, cur_c
                move_r_2, move_c_2 = cur_r, cur_c
                move_r_3, move_c_3 = cur_r, cur_c
                move_r_4, move_c_4 = cur_r, cur_c
                
                while True:
                    
                    move_r_1, move_c_1 = move_r_1, move_c_1 - 1
                    
                    if 0 <= move_r_1 <= N-1 and 0 <= move_c_1 <= M-1:
                        
                        if copied[move_r_1][move_c_1] == 0:
                            
                            copied[move_r_1][move_c_1] = '#'
                            continue
                        
                        elif copied[move_r_1][move_c_1] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_2, move_c_2 = move_r_2 - 1, move_c_2
                    
                    if 0 <= move_r_2 <= N-1 and 0 <= move_c_2 <= M-1:
                        
                        if copied[move_r_2][move_c_2] == 0:
                            
                            copied[move_r_2][move_c_2] = '#'
                            continue
                        
                        elif copied[move_r_2][move_c_2] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break

                while True:
                    
                    move_r_3, move_c_3 = move_r_3 + 1, move_c_3
                    
                    if 0 <= move_r_3 <= N-1 and 0 <= move_c_3 <= M-1:
                        
                        if copied[move_r_3][move_c_3] == 0:
                            
                            copied[move_r_3][move_c_3] = '#'
                            continue
                        
                        elif copied[move_r_3][move_c_3] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
                
                while True:
                    
                    move_r_4, move_c_4 = move_r_4, move_c_4 + 1
                    
                    if 0 <= move_r_4 <= N-1 and 0 <= move_c_4 <= M-1:
                        
                        if copied[move_r_4][move_c_4] == 0:
                            
                            copied[move_r_4][move_c_4] = '#'
                            continue
                        
                        elif copied[move_r_4][move_c_4] == 6:
                            
                            break
                        
                        else:
                            
                            continue
                    
                    else:
                        
                        break
    
    # 사각지대
    blind_spot = 0
    
    for i in range(N):
        
        for j in range(M):
            
            if copied[i][j] == 0:
                
                blind_spot += 1
    
    # 최솟값 갱신
    min_blind_spot = min(min_blind_spot, blind_spot)

# 답안 출력
print(min_blind_spot)