# 14888 연산자 끼워넣기

import sys
from itertools import permutations

# 수의 개수 N이 주어집니다.
N = int(sys.stdin.readline().rstrip())

# A1, A2, A3,,, An이 주어집니다.
seq = list(map(int, sys.stdin.readline().split()))

# 사칙연산 각 부호의 개수가 주어집니다. 순서대로 +, -, x, /
sign = list(map(int, sys.stdin.readline().split()))

# Strategy
# 1. sign에 따라 연산자의 부호를 list에 저장한다.
# 2. 부호의 순열을 구해준다. 이후 중복된 순열을 제거해준다.(중요)
# 3. Seq에 대해서 앞에서 부터 연산을 수행한다.

# 연산자의 부호를 list에 저장합니다.
sign_list = []

for i in range(4):

    # '+' 일때
    if i == 0:
        
        for k in range(sign[i]):

            sign_list.append('+')
    
    # '-' 일때
    elif i == 1:

        for k in range(sign[i]):

            sign_list.append('-')
    
    # 'x' 일때
    elif i == 2:

        for k in range(sign[i]):

            sign_list.append('x')
    
    # '/' 일때
    else:

        for k in range(sign[i]):

            sign_list.append('/')

# 부호의 순열을 구해줍니다. 부호의 개수는 N-1개
sign_perm = list(permutations(sign_list, N-1))

# 중복을 제거해줍니다.
sign_perm = list(set(sign_perm))

# Seq에 대해서 연산을 수행하고 결과를 저장합니다.
seq_cal = []

# 부호의 순열에 대해서
for perm in sign_perm:

    cal = 0

    for i in range(1, N):

        # 처음 계산일 때
        if i == 1:

            # 부호가 무엇인지에 따라 다른 연산결과를 제공합니다.
            if perm[i-1] == '+':

                cal += (seq[i-1] + seq[i])
            
            elif perm[i-1] == '-':

                cal += (seq[i-1] - seq[i])
            
            elif perm[i-1] == 'x':

                cal += (seq[i-1] * seq[i])

            else: # perm[i-1] == '/'

                cal = seq[i-1] // seq[i]
        
        else: # 이후 계산

            # 부호가 무엇인지에 따라 다른 연산결과를 제공합니다.
            if perm[i-1] == '+':

                cal += seq[i]
            
            elif perm[i-1] == '-':

                cal -= seq[i]
            
            elif perm[i-1] == 'x':

                cal *= seq[i]

            else: # perm[i-1] == '/'
                
                # cal이 0보다 작을 때
                if cal < 0:
                    
                    # cal을 양수로 취한 뒤 나눗셈 연산 후 그 몫을 다시 음수를 취한다.
                    cal = - (-cal // seq[i])
                
                # cal이 0보다 클 때
                else:

                    cal = cal // seq[i]

    seq_cal.append(cal)

# 답안출력
print(max(seq_cal))
print(min(seq_cal))