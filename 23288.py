# 23288 주사위 굴리기 2

import sys
from collections import deque
from copy import deepcopy

def BFS(graph_v, start_v, row_len, col_len):

    # 4방향
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 큐 생성
    queue = deque([start_v])

    # 시작 좌표
    start_r, start_c = start_v
    
    # 시작 좌표 값
    val = graph_v[start_r][start_c]

    # 시작좌표 방문처리
    graph_v[start_r][start_c] = 'v'

    # 시작 좌표 값과 같은 개수
    cnt = 1

    # 큐가 빌 때까지 반복
    while queue:

        cur_r, cur_c = queue.popleft()

        for i in range(4):

            move_r, move_c = cur_r + dr[i], cur_c + dc[i]

            if 0 <= move_r <= row_len-1 and 0 <= move_c <= col_len-1:
                if graph_v[move_r][move_c] == val:

                    # 방문 처리
                    graph_v[move_r][move_c] = 'v'

                    # 큐에 추가
                    queue.append([move_r, move_c])

                    # 개수 추가
                    cnt += 1
    
    # 점수 리턴
    return val * cnt

# 지도의 크기, 이동하는 횟수가 주어집니다.
N, M, K = map(int, sys.stdin.readline().split())

# 지도 초기화
board = []

# 주사위 초기화, 순서대로 [위, 아래, 동, 서, 남, 북]
dice = [1, 6, 3, 4, 5, 2]

# 지도 정보가 주어집니다.
for _ in range(N):

    board.append(list(map(int, sys.stdin.readline().split())))

# 주사위의 초기 위치
r, c = 0, 0

# 총합 점수
score = 0

# K번 동안 주사위가 이동합니다.
for i in range(K):

    # 처음에는 동쪽으로 이동합니다.
    if i == 0:

        c += 1
        
        # 지도 복사
        copy = deepcopy(board)

        # BFS 실행
        score += BFS(copy, [r,c], N, M)

        # 주사위 동쪽으로 한 칸 굴리기
        dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]

        # 주사위의 아랫면과 보드의 숫자를 비교합니다.
        if dice[1] > board[r][c]:

            # 이동방향은 남쪽입니다.
            command = 4
        
        elif dice[1] < board[r][c]:

            # 이동방향은 북쪽입니다.
            command = 3
        
        else: # dice[1] == board[r][c]

            # 이동방향은 동쪽 유지
            command = 1

    # 2번째 이동부터는 아래 else 문을 따릅니다.
    else:

        # 이동방향이 동쪽일 때
        if command == 1:

            # 이동 가능할 때
            if 0 <= r <= N-1 and 0 <= c+1 <= M-1:
                
                c += 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 남쪽입니다.
                    command = 4
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 북쪽입니다.
                    command = 3
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 동쪽 유지
                    command = 1

            # 이동 불가능할 때 반대로 갑니다.(서쪽)
            else:

                c -= 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 북쪽입니다.
                    command = 3
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 남쪽입니다.
                    command = 4
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 서쪽 유지
                    command = 2
        
        # 이동 방향이 서쪽일 때
        elif command == 2:

            # 이동 가능할 때
            if 0 <= r <= N-1 and 0 <= c-1 <= M-1:
                
                c -= 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                # 서쪽으로 한 칸 굴리기
                dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 북쪽입니다.
                    command = 3
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 남쪽입니다.
                    command = 4
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 서쪽 유지
                    command = 2

            # 이동 불가능할 때 반대로 갑니다.(동쪽)
            else:

                c += 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 남쪽입니다.
                    command = 4
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 북쪽입니다.
                    command = 3
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 동쪽 유지
                    command = 1

        # 이동 방향이 북쪽일 때
        elif command == 3:
            
            # 이동가능 할 때
            if 0 <= r-1 <= N-1 and 0 <= c <= M-1:

                r -= 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                # 북쪽으로 한 칸 굴리기
                dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 동쪽입니다.
                    command = 1
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 서쪽입니다.
                    command = 2
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 북쪽 유지
                    command = 3

            # 이동 불가능할 때 반대로 갑니다.(남쪽)
            else:

                r += 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 서쪽입니다.
                    command = 2
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 동쪽입니다.
                    command = 1
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 동쪽 유지
                    command = 4

        else: # 이동방향이 남쪽일 때 command == 4

            # 이동 가능할 때
            if 0 <= r+1 <= N-1 and 0 <= c <= M-1:

                r += 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 서쪽입니다.
                    command = 2
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 동쪽입니다.
                    command = 1
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 남쪽 유지
                    command = 4
            
            else: # 이동 불가할 때 북쪽으로 이동

                r -= 1

                copy = deepcopy(board)

                score += BFS(copy, [r,c], N, M)

                # 북쪽으로 한 칸 굴리기
                dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]

                # 주사위의 아랫면과 보드의 숫자를 비교합니다.
                if dice[1] > board[r][c]:

                    # 이동방향은 동쪽입니다.
                    command = 1
                
                elif dice[1] < board[r][c]:

                    # 이동방향은 서쪽입니다.
                    command = 2
                
                else: # dice[1] == board[r][c]

                    # 이동방향은 북쪽 유지
                    command = 3

# 점수 출력
print(score)