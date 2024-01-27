# 14891 톱니바퀴

import sys
from collections import deque

# 기어 회전함수
def Rotation(gear, d):

    # 시계방향 회전
    if d == 1:
        
        gear.appendleft(gear.pop())
    
    # 반시계방향 회전
    elif d == -1:

        gear.append(gear.popleft())

# 회전시키는 함수 (톱니번호, 방향)
def func(n, d):
    
    # 1번 톱니 회전일 때
    if n == 0:
        
        array = []
        
        if gears[0][2] == gears[1][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[1][2] == gears[2][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[2][2] == gears[3][6]:
            
            array.append('N')
            
        else:
            
            array.append('Y')

        # 1번 톱니 회전
        Rotation(gears[0], d)
        
        # 2번 톱니 회전
        if array[0] == 'Y':
            
            Rotation(gears[1], -d)
            
            # 3번 톱니 회전
            if array[1] == 'Y':
                
                Rotation(gears[2], d)

                # 4번 톱니 회전
                if array[2] == 'Y':
                    
                    Rotation(gears[3], -d)
                    
    # 2번 톱니 회전일 때
    elif n == 1:
      
        array = []
        
        if gears[0][2] == gears[1][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[1][2] == gears[2][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[2][2] == gears[3][6]:
            
            array.append('N')
            
        else:
            
            array.append('Y')
        
        # 2번 톱니 회전
        Rotation(gears[1], d)
        
        # 1번 톱니 회전
        if array[0] == 'Y':
        
            Rotation(gears[0], -d)

        # 3번 톱니 회전
        if array[1] == 'Y':
            
            Rotation(gears[2], -d)
            
            # 4번 톱니 회전
            if array[2] == 'Y':
                
                Rotation(gears[3], d)

    # 3번 톱니 회전일 때  
    elif n == 2:

        array = []
        
        if gears[0][2] == gears[1][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[1][2] == gears[2][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[2][2] == gears[3][6]:
            
            array.append('N')
            
        else:
            
            array.append('Y')
        
        # 3번 톱니 회전
        Rotation(gears[2], d)
        
        # 4번톱니 회전
        if array[2] == 'Y':
            
            Rotation(gears[3], -d)
        
        # 2번 톱니 회전
        if array[1] == 'Y':
            
            Rotation(gears[1], -d)
            
            # 1번 톱니 회전
            if array[0] == 'Y':
                
                Rotation(gears[0], d)
                
    # 4번 톱니 회전일 때
    elif n == 3:
        
        array = []
        
        if gears[0][2] == gears[1][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[1][2] == gears[2][6]:
            
            array.append('N')
        
        else:
            
            array.append('Y')
        
        if gears[2][2] == gears[3][6]:
            
            array.append('N')
            
        else:
            
            array.append('Y')
        
        # 4번 톱니 회전
        Rotation(gears[3], d)
        
        # 3번 톱니 회전
        if array[2] == 'Y':
            
            Rotation(gears[2], -d)
            
            # 2번 톱니 회전
            if array[1] == 'Y':
                
                Rotation(gears[1], d)
                
                # 1번 톱니 회전
                if array[0] == 'Y':
                    
                    Rotation(gears[0], -d) 

# 톱니바퀴 리스트
gears = []

# 4개의 톱니바퀴 상태가 주어진다.
for _ in range(4):
    
    gears.append(deque(list(map(int, sys.stdin.readline().rstrip()))))

# 회전 횟수 K가 주어진다.
K = int(sys.stdin.readline().rstrip())

# 회전시킨 방법이 주어진다.
for _ in range(K):
    
    # 1은 시계방향, -1은 반시계방향
    num, direction = list(map(int, sys.stdin.readline().split()))
    
    num -= 1
    
    # 함수 실행
    func(num, direction)

# 점수 총합
score = 0

# 네 톱니바퀴의 점수 합을 계산
for i in range(4):
    
    if i == 0:
        
        if gears[i][0] == 1:
            
            score += 1
            
    elif i == 1:
        
        if gears[i][0] == 1:
            
            score += 2
        
    elif i == 2:
        
        if gears[i][0] == 1:
            
            score += 4
        
    elif i == 3:
        
        if gears[i][0] == 1:
            
            score += 8

# 출력
print(score)