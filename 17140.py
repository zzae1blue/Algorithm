# 17140 이차열 배열과 연산

import sys

# r, c, k가 주어집니다.
r, c, k = map(int, sys.stdin.readline().split())

# 가능여부
impossible = False

# 인덱싱
r -= 1
c -= 1

# A 초기화
A = []

# A가 주어진다.
for _ in range(3):
    
    A.append(list(map(int, sys.stdin.readline().split())))

# 시간
time = 0

# A[r][c] = k가 될 때까지 반복합니다.
while True:

    # 행, 열의 개수를 파악합니다.
    rows = len(A)
    cols = len(A[0])
       
    if 0 <= r <= rows-1 and 0 <= c <= cols-1:
        
        if A[r][c] == k:
            
            break
    
    # 시간 증가
    time += 1
    
    if time > 100:
        
        impossible = True
        break
    
    # 행이 열보다 크거나 같을 때 R연산
    if rows >= cols:
        
        # 모든 행에 대해서 연산
        for i in range(rows):
            
            # 행을 가져온다.
            array = A[i]
            
            # 각 요소가 몇개 있는지 알아보기 위해 중복을 제거한다.
            array = list(set(array))

            # 0이 있으면 제거
            if 0 in array:
                
                array.remove(0)
                
            # 임시 리스트
            temp = []
            
            for val in array:
                
                temp.append((val, A[i].count(val)))
            
            temp.sort(key = lambda x:(x[1],x[0]))
            
            temp2 = []
            
            for pair in temp:
                
                for t in range(2):
                    
                    temp2.append(pair[t])
                
            A[i] = temp2
        
        # 가장 큰 행의 크기에 맞춘다.
        max_size_row = -1
        
        for i in range(rows):
            
            max_size_row = max(max_size_row, len(A[i]))
        
        if max_size_row > 100:
            
            max_size_row = 100
            
        for i in range(rows):
            
            row_size = len(A[i])
            
            if row_size > 100:
                
                for _ in range(row_size-max_size_row):
                    
                    del A[i][-1]
                    
            else:
                
                for _ in range(max_size_row-row_size):
                    
                    A[i].append(0)

    # 행이 열보다 작을 때 C연산
    else:
        
        B = []
        
        # 열을 가져온다.
        for i in range(cols):
            
            array = []
            
            for j in range(rows):
                
                array.append(A[j][i])

            array2 = array.copy()
            
            # 모든 열에 대해서 연산
            array = list(set(array))
            
            # 0이 있으면 제거
            if 0 in array:
                
                array.remove(0)
            
            # 임시 리스트
            temp = []
            
            for val in array:
                
                temp.append((val, array2.count(val)))
            
            temp.sort(key = lambda x:(x[1],x[0]))
            
            temp2 = []
            
            for pair in temp:
                
                for t in range(2):
                    
                    temp2.append(pair[t])

            B.append(temp2)

        # 가장 큰 행의 크기에 맞춘다.
        max_size_row = -1
        
        for i in range(cols):
            
            max_size_row = max(max_size_row, len(B[i]))

        if max_size_row > 100:
            
            max_size_row = 100
            
        for i in range(cols):
            
            row_size = len(B[i])
            
            if row_size > 100:
                
                for _ in range(row_size-max_size_row):
                        
                    del A[i][-1]
                    
            else:
                
                for _ in range(max_size_row-row_size):
                    
                    B[i].append(0)
        
        # 전치
        A = [list(row) for row in zip(*B)]

# 답안 출력
if impossible == True:
    
    print(-1)

else:
    
    print(time)