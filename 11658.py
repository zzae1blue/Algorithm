# 11658 구간 합 구하기 3

import sys
from copy import deepcopy

# N, M이 주어집니다.
N, M = map(int, sys.stdin.readline().split())

# 배열
array = []

# 수가 주어집니다.
for _ in range(N):

    array.append(list(map(int, sys.stdin.readline().split())))

# 구간 합 배열
array_sum = deepcopy(array)

for i in range(N):

    for j in range(1, N):

        array_sum[i][j] += array_sum[i][j-1]

# 정수가 주어집니다.
for _ in range(M):

    temp = list(map(int, sys.stdin.readline().split()))

    if len(temp) == 5:

        w, x1, y1, x2, y2 = temp

        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # 누적 합
        ans = 0

        for i in range(x1, x2+1):

            if y1 == 0:
                
                ans += array_sum[i][y2]
            
            else: # y1 != 0
                
                ans += (array_sum[i][y2]-array_sum[i][y1-1])
        
        print(ans)
    
    else: # len(temp) == 4

        w, x, y, c = temp

        x -= 1
        y -= 1

        diff = c - array[x][y]

        array[x][y] = c
        
        for i in range(y,N):

            array_sum[x][i] += diff

        