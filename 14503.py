# 14503 로봇 청소기

import sys

# 방의 크기 N,M이 주어집니다.
N, M = map(int, sys.stdin.readline().split())

# 로봇 청소기가 있는 좌표 (r,c)와 바라보는 방향 d가 주어집니다.
r, c, d = map(int, sys.stdin.readline().split())

# 방 초기화
room = []

# 각 장소의 상태가 주어집니다.
for _ in range(N):

    room.append(list(map(int, sys.stdin.readline().split())))

# 청소하는 칸의 개수 초기화
clean = 0

# 구현, 로봇청소기가 멈출 때까지 계속 반복합니다.
while True:

    # 현재 칸이 청소되지 않은 경우 청소합니다.
    if room[r][c] == 0:

        # 청소
        room[r][c] = 'c'

        # 칸의 개수 추가
        clean += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if room[r+1][c] != 0 and room[r-1][c] != 0 and room[r][c+1] != 0 and room[r][c-1] != 0:

        # 바라보는 방향이 북쪽일 때
        if d == 0:
            
            # 한 칸 후진할 수 있다면(벽이 아닐 때)
            if room[r+1][c] != 1:

                r += 1
                continue
            
            # 후진할 수 없다면 작동을 멈춘다
            else:

                break
                
        # 바라보는 방향이 동쪽일 때
        elif d == 1:

            # 한 칸 후진할 수 있다면(벽이 아닐 때)
            if room[r][c-1] != 1:

                c -= 1
                continue

            # 후진할 수 없다면 작동을 멈춘다
            else:

                break

        # 바라보는 방향이 남쪽일 때
        elif d == 2:

            # 한 칸 후진할 수 있다면(벽이 아닐 때)
            if room[r-1][c] != 1:

                r -= 1
                continue

            # 후진할 수 없다면 작동을 멈춘다
            else:

                break

        # 바라보는 방향이 서쪽일 때
        else:
            
            # 한 칸 후진할 수 있다면(벽이 아닐 때)
            if room[r][c+1] != 1:

                c += 1
                continue

            # 후진할 수 없다면 작동을 멈춘다
            else:

                break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    elif room[r+1][c] == 0 or room[r-1][c] == 0 or room[r][c+1] == 0 or room[r][c-1] == 0:

        # 현재 바라보는 방향이 북쪽일 때
        if d == 0:

            # 반시계 방향으로 90도 회전 후 앞쪽 칸(서쪽)이 청소되지 않은 칸이면 전진
            if room[r][c-1] == 0:

                # 전진
                c -= 1

                # 방향은 서쪽
                d = 3
            
            # 청소된 칸이거나 벽인경우
            else:

                # 반시계 방향으로만 90도 회전
                d = 3
        
        # 현재 바라보는 방향이 동쪽일 때
        elif d == 1:

            # 반시계 방향으로 90도 회전 후 앞쪽 칸(북쪽)이 청소되지 않은 칸이면 전진
            if room[r-1][c] == 0:

                # 전진
                r -= 1

                # 방향은 북쪽
                d = 0

            else:

                d = 0
    
        # 현재 바라보는 방향이 남쪽일 때
        elif d == 2:

            # 반시계 방향으로 90도 회전 후 앞쪽 칸(동쪽)이 청소되지 않은 칸이면 전진
            if room[r][c+1] == 0:

                # 전진
                c += 1

                # 방향은 동쪽
                d = 1
            
            else:

                d = 1
        
        # 현재 바라보는 방향이 서쪽일 때
        else:

            # 반시계 방향으로 90도 회전 후 앞쪽 칸(남쪽)이 청소되지 않은 칸이면 전진
            if room[r+1][c] == 0:

                # 전진
                r += 1

                # 방향은 남쪽
                d = 2
            
            else:

                d = 2

# 답안 출력
print(clean)        