# 14501 퇴사

import sys

# 최대 수익을 위한 백트래킹 함수
max_benefit = -1

def backtracking(b, k):

    global max_benefit
    
    if N == 1:
        
        t, p = consult[0]
        
        if t > 1:
            
            max_benefit = 0
            return
        
        else:
            
            max_benefit = p
            return
            
    if k == len(consult) - 1:
        
        max_benefit = max(max_benefit, b)
        return
    
    for i in range(len(consult)):
        
        if k == 0 and not visited[i]:
            
            t, p = consult[i]
            
            # 종료 조건
            if i + t > N:
                
                max_benefit = max(max_benefit, b)
                continue
            
            else:
                
                for m in range(i, i+t):
                    
                    visited[m] = True
            
                # 재귀호출
                backtracking(b + p, m)
            
            # 풀어준다.
            for m in range(i, i+t):
                
                visited[m] = False
                   
        elif k < i and not visited[i]:
            
            t, p = consult[i]
            
            # 종료 조건
            if i + t > N:
                
                max_benefit = max(max_benefit, b)
                continue
            
            for m in range(i, i+t):
                
                visited[m] = True
            
            # 재귀호출
            backtracking(b + p, m)
            
            # 풀어준다.
            for m in range(i, i+t):
                
                visited[m] = False
    
# N이 주어진다.
N = int(sys.stdin.readline().rstrip())

# 방문여부 리스트
visited = [False] * N

# 상담 리스트
consult = []

# N개의 줄에 Ti, Pi가 주어진다.
for _ in range(N):
    
    ti, pi = map(int, sys.stdin.readline().split())

    consult.append((ti, pi))

# 백트래킹 함수
backtracking(0, 0)

# 답안 출력
print(max_benefit)