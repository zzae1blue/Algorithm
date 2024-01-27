# 14499 주사위 굴리기

import sys

# 지도의 크기, 주사위를 놓은 좌표, 명령의 개수가 주어집니다.
N, M, x, y, K = map(int, sys.stdin.readline().split())

# 지도 초기화
board = []

# 주사위 초기화, 순서대로 [위, 아래, 동, 서, 남, 북]
dice = [0] * 6

# 지도 정보가 주어집니다.
for _ in range(N):

    board.append(list(map(int, sys.stdin.readline().split())))

# 주사위를 이동시키는 명령이 주어집니다.
command = list(map(int, sys.stdin.readline().split()))

# 이동명령에 대해 계산합니다.
for i in range(len(command)):

    # 동쪽 이동
    if command[i] == 1:

        # 주어진 범위내에서 움직일 때
        if 0 <= x <= N-1 and 0 <= y+1 <= M-1:

            y += 1

            # 주사위 굴리기
            dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]

            if board[x][y] == 0:
                
                # 주사위의 바닥면이 지도에 쓰이게 된다.
                board[x][y] = dice[1]
                
                # 윗면 출력
                print(dice[0])

            else: # board[x][y] != 0

                dice[1] = board[x][y]
                board[x][y] = 0

                print(dice[0])

        # 주어진 범위를 벗어나면 skip
        else:

            continue

    # 서쪽 이동
    elif command[i] == 2:
        
        # 주어진 범위내에서 움직일 때
        if 0 <= x <= N-1 and 0 <= y-1 <= M-1:

            y -= 1

            # 주사위 굴리기
            dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]

            if board[x][y] == 0:
                
                # 주사위의 바닥면이 지도에 쓰이게 된다.
                board[x][y] = dice[1]
                
                # 윗면 출력
                print(dice[0])

            else: # board[x][y] != 0

                dice[1] = board[x][y]
                board[x][y] = 0

                print(dice[0])

        # 주어진 범위를 벗어나면 skip
        else:

            continue

    # 북쪽 이동
    elif command[i] == 3:

        # 주어진 범위내에서 움직일 때
        if 0 <= x-1 <= N-1 and 0 <= y <= M-1:

            x -= 1

            # 주사위 굴리기
            dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]

            if board[x][y] == 0:
                
                # 주사위의 바닥면이 지도에 쓰이게 된다.
                board[x][y] = dice[1]
                
                # 윗면 출력
                print(dice[0])

            else: # board[x][y] != 0

                dice[1] = board[x][y]
                board[x][y] = 0

                print(dice[0])

        # 주어진 범위를 벗어나면 skip
        else:

            continue
    
    # 남쪽 이동
    else: # command[i] == 4

        # 주어진 범위내에서 움직일 때
        if 0 <= x+1 <= N-1 and 0 <= y <= M-1:
                
            x += 1
            
            # 주사위 굴리기
            dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]

            if board[x][y] == 0:
                
                # 주사위의 바닥면이 지도에 쓰이게 된다.
                board[x][y] = dice[1]
                
                # 윗면 출력
                print(dice[0])

            else: # board[x][y] != 0

                dice[1] = board[x][y]
                board[x][y] = 0

                print(dice[0])

        # 주어진 범위를 벗어나면 skip
        else:

            continue