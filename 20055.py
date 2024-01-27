# 20055 컨베이어 벨트 위의 로봇

import sys
from collections import deque

# N, K가 주어진다.
N, K = map(int, sys.stdin.readline().split())

# A1, A2,, A2n이 주어진다.
Ai = list(map(int, sys.stdin.readline().split()))

# 큐로 변경
Ai = deque(Ai)

# 단계
stage = 0

# 라인
line = [0] * N

# 큐로 변경
line = deque(line)

# 로봇을 옮긴다.
while True:
    
    # 단계 증가
    stage += 1
    
    # 벨트가 로봇과 함께 회전한다.
    line.pop()
    line.appendleft(0)
    
    # 내구도 이동
    temp = Ai.pop()
    Ai.appendleft(temp)
    
    # 벨트가 회전하는 방향으로 한 칸 이동할 수 있으면 이동한다. 이동할 수 없으면 가만히 있는다.
    for i in range(N-1, -1, -1):
        
        # 로봇일 때
        if line[i] == 1:
            
            # 내리는 위치일 때
            if i == N-1:
                
                # 내린다.
                line[i] = 0
                
            else:
                
                # 이동하려는 칸에 로봇이 없고 내구도가 남아있을 때
                if line[i+1] == 0 and Ai[i+1] > 0:
                    
                    # 로봇을 한 칸 이동시킨다.
                    line[i+1] = 1
                    line[i] = 0
                
                    # 칸 내구도 감소
                    Ai[i+1] -= 1
        
        # 로봇이 아닐 때
        else:
            
            continue
        
    # 로봇을 올릴 수 있으면 올린다.(내구도가 남아있을 때)
    if Ai[0] > 0:
        
        line[0] += 1
        
        # 내구도 감소
        Ai[0] -= 1
    
    # 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료한다. 아니면 반복
    cnt = 0
    
    for i in range(2*N):
        
        if Ai[i] == 0:
            
            cnt += 1
    
    if cnt >= K:
        
        break

# 몇 번째 단계가 진행중이었는지 출력
print(stage)