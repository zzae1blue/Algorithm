# 5373 큐빙

import sys
from copy import deepcopy

# 큐브 초기화 : 순서대로 위(0), 아래(1), 앞(2), 뒤(3), 왼(4), 오(5)

# 큐브를 회전시키는 함수
def rotate(cmd):
    
    # 면
    surface = cmd[0]
    
    # 방향
    direction = cmd[1]
    
    # 윗면을 돌릴 때
    if surface == 'U':
        
        # 시계방향 90도 회전
        if direction == '+':
            
            cube[0] = clockwise(cube[0])
            
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[2][0][i])
                temp2.append(cube[4][0][i])
                temp3.append(cube[3][0][i])
                temp4.append(cube[5][0][i])
            
            for i in range(3):
                
                cube[2][0][i] = temp4[i]
                cube[4][0][i] = temp1[i]
                cube[3][0][i] = temp2[i]
                cube[5][0][i] = temp3[i]
                
        # 반시계방향 90도 회전
        elif direction == '-':
            
            cube[0] = counter_clockwise(cube[0])

            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[2][0][i])
                temp2.append(cube[4][0][i])
                temp3.append(cube[3][0][i])
                temp4.append(cube[5][0][i])
            
            for i in range(3):
                
                cube[2][0][i] = temp2[i]
                cube[4][0][i] = temp3[i]
                cube[3][0][i] = temp4[i]
                cube[5][0][i] = temp1[i]
                
    # 아랫면을 돌릴 때
    elif surface == 'D':

        # 시계방향 90도 회전
        if direction == '+':
            
            cube[1] = clockwise(cube[1])
            
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[2][2][i])
                temp2.append(cube[4][2][i])
                temp3.append(cube[3][2][i])
                temp4.append(cube[5][2][i])
            
            for i in range(3):
                
                cube[2][2][i] = temp2[i]
                cube[4][2][i] = temp3[i]
                cube[3][2][i] = temp4[i]
                cube[5][2][i] = temp1[i]
            
        # 반시계방향 90도 회전
        elif direction == '-':
            
            cube[1] = counter_clockwise(cube[1])
            
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[2][2][i])
                temp2.append(cube[4][2][i])
                temp3.append(cube[3][2][i])
                temp4.append(cube[5][2][i])
            
            for i in range(3):
                
                cube[2][2][i] = temp4[i]
                cube[4][2][i] = temp1[i]
                cube[3][2][i] = temp2[i]
                cube[5][2][i] = temp3[i]
                
    # 앞면을 돌릴 때 
    elif surface == 'F':

        # 시계방향 90도 회전
        if direction == '+':
            
            cube[2] = clockwise(cube[2])
            
            temp2 = []
            temp4 = []
            
            temp1 = deepcopy(cube[0][2])
            temp3 = deepcopy(cube[1][2])
            
            for i in range(3):
                
                temp2.append(cube[5][i][0])
                cube[5][i][0] = temp1[i]
                
                temp4.append(cube[4][2-i][2])
                cube[4][2-i][2] = temp3[i]

            cube[0][2] = temp4
            cube[1][2] = temp2
            
        # 반시계방향 90도 회전
        elif direction == '-':
            
            cube[2] = counter_clockwise(cube[2])
            
            temp2 = []
            temp4 = []
            
            temp1 = deepcopy(cube[0][2])
            temp3 = deepcopy(cube[1][2])
            
            for i in range(3):
                
                temp2.append(cube[5][i][0])
                cube[5][i][0] = temp3[i]
                
                temp4.append(cube[4][2-i][2])
                cube[4][2-i][2] = temp1[i]

            cube[0][2] = temp2
            cube[1][2] = temp4
                
    # 뒷면을 돌릴 때
    elif surface == 'B':

        # 시계방향 90도 회전
        if direction == '+':
            
            cube[3] = clockwise(cube[3])

            temp2 = []
            temp4 = []
            
            temp1 = deepcopy(cube[0][0])
            temp3 = deepcopy(cube[1][0])
            
            for i in range(3):
                
                temp2.append(cube[5][i][2])
                cube[5][i][2] = temp3[i]
                
                temp4.append(cube[4][2-i][0])
                cube[4][2-i][0] = temp1[i]

            cube[0][0] = temp2
            cube[1][0] = temp4
            
        # 반시계방향 90도 회전
        elif direction == '-':
            
            cube[3] = counter_clockwise(cube[3])

            temp2 = []
            temp4 = []
            
            temp1 = deepcopy(cube[0][0])
            temp3 = deepcopy(cube[1][0])
            
            for i in range(3):
                
                temp2.append(cube[5][i][2])
                cube[5][i][2] = temp1[i]
                
                temp4.append(cube[4][2-i][0])
                cube[4][2-i][0] = temp3[i]

            cube[0][0] = temp4
            cube[1][0] = temp2
            
    # 왼쪽면을 돌릴 때    
    elif surface == 'L':

        # 시계방향 90도 회전
        if direction == '+':
            
            cube[4] = clockwise(cube[4])
            
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[0][i][0])
                temp2.append(cube[2][i][0])
                temp3.append(cube[1][2-i][2])
                temp4.append(cube[3][2-i][2])
            
            for i in range(3):
                
                cube[0][i][0] = temp4[i]
                cube[2][i][0] = temp1[i]
                cube[1][2-i][2] = temp2[i]
                cube[3][2-i][2] = temp3[i]
                
        # 반시계방향 90도 회전
        elif direction == '-':
            
            cube[4] = counter_clockwise(cube[4])

            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[0][i][0])
                temp2.append(cube[2][i][0])
                temp3.append(cube[1][2-i][2])
                temp4.append(cube[3][2-i][2])
            
            for i in range(3):
                
                cube[0][i][0] = temp2[i]
                cube[2][i][0] = temp3[i]
                cube[1][2-i][2] = temp4[i]
                cube[3][2-i][2] = temp1[i]
            
    # 오른쪽면을 돌릴 때
    elif surface == 'R':

        # 시계방향 90도 회전
        if direction == '+':
            
            cube[5] = clockwise(cube[5])
            
            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[0][2-i][2])
                temp2.append(cube[3][i][0])
                temp3.append(cube[1][i][0])
                temp4.append(cube[2][2-i][2])
            
            for i in range(3):
                
                cube[0][2-i][2] = temp4[i]
                cube[3][i][0] = temp1[i]
                cube[1][i][0] = temp2[i]
                cube[2][2-i][2] = temp3[i]
            
        # 반시계방향 90도 회전
        elif direction == '-':

            cube[5] = counter_clockwise(cube[5])

            temp1 = []
            temp2 = []
            temp3 = []
            temp4 = []
            
            for i in range(3):
                
                temp1.append(cube[0][2-i][2])
                temp2.append(cube[3][i][0])
                temp3.append(cube[1][i][0])
                temp4.append(cube[2][2-i][2])
            
            for i in range(3):
                
                cube[0][2-i][2] = temp2[i]
                cube[3][i][0] = temp3[i]
                cube[1][i][0] = temp4[i]
                cube[2][2-i][2] = temp1[i]
            
# 시계방향 회전
def clockwise(array):
    
    temp = [[0] * 3 for _ in range(3)]
    
    for i in range(3):
        
        for j in range(3):
            
            temp[j][2-i] = array[i][j]
    
    return temp
    
# 반시계방향 회전
def counter_clockwise(array):
    
    temp = [[0] * 3 for _ in range(3)]
    
    for i in range(3):
        
        for j in range(3):
            
            temp[2-j][i] = array[i][j]
    
    return temp    
    
# 테스트 케이스가 주어집니다.
T = int(sys.stdin.readline().rstrip())

# 각 테스트케이스에 대해서 진행
for _ in range(T):

    cube = [[['w','w','w'], ['w','w','w'], ['w','w','w']], [['y','y','y'],['y','y','y'],['y','y','y']], [['r','r','r'],['r','r','r'],['r','r','r']], [['o','o','o'],['o','o','o'],['o','o','o']], [['g','g','g'],['g','g','g'],['g','g','g']], [['b','b','b'],['b','b','b'],['b','b','b']]]
    
    # 큐브를 돌린 횟수 n
    n = int(sys.stdin.readline().rstrip())
    
    # 큐브를 돌리는 방법이 주어집니다.
    seq = list(map(str, sys.stdin.readline().split()))
    
    for command in seq:
        
        # 명령에 따라 회전시킨다.
        rotate(command)
    
    # 가장 윗면의 색상을 출력한다.
    for k in range(3):
        
        p = ''.join(cube[0][k])
        print(p)