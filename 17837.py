# 17837 새로운 게임 2

import sys

# 게임을 진행하는 함수
def playing(num, coord, moving):
    
    global finish
    
    # num = 말의 번호
    
    # 말의 현재좌표
    cur_r, cur_c = coord

    # 이동방향이 동쪽일 때
    if moving == 1:
        
        move_r, move_c = cur_r, cur_c + 1
        
        # 영역을 벗어나지 않을 때
        if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
            
            # 흰색일 때
            if color[move_r][move_c] == 0:
                
                index = board[cur_r][cur_c].index(num)
                
                # 이동하려는 칸 위에 쌓는다.
                for val in board[cur_r][cur_c][index:]:
                    
                    board[move_r][move_c].append(val)
                    
                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]
                
                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]
                
                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True   
                
            # 빨간색일 때
            elif color[move_r][move_c] == 1:
                
                index = board[cur_r][cur_c].index(num)
                
                # 뒤집는다.
                temp = board[cur_r][cur_c][index:][::-1]
                
                # 이동하려는 칸에 추가한다.
                for val in temp:
                    
                    board[move_r][move_c].append(val)

                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]

                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
            
            # 파란색일 때
            elif color[move_r][move_c] == 2:
                
                # 방향을 바꾼다.
                
                # 동쪽일 때
                if moving == 1:
                    
                    # 서쪽으로 변경
                    moving = 2
                    
                    move_r, move_c = cur_r, cur_c - 1
                
                # 서쪽일 때
                elif moving == 2:
                    
                    # 동쪽으로 변경
                    moving  = 1
                    
                    move_r, move_c = cur_r, cur_c + 1
                
                # 북쪽일 때 
                elif moving == 3:
                    
                    # 남쪽으로 변경
                    moving = 4
                    
                    move_r, move_c = cur_r + 1, cur_c
                
                # 남쪽일 때
                elif moving == 4:
                    
                    # 북쪽으로 변경
                    moving = 3
                    
                    move_r, move_c = cur_r - 1, cur_c

                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
                if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
                
                    index = board[cur_r][cur_c].index(num)
                    
                    # 반대방향이 흰색
                    if color[move_r][move_c] == 0:
                        
                        # 이동하려는 칸 위에 쌓는다.
                        for val in board[cur_r][cur_c][index:]:
                            
                            board[move_r][move_c].append(val)
                            
                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                        
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True
                        
                    # 반대방향이 빨간색
                    elif color[move_r][move_c] == 1:
                        
                        index = board[cur_r][cur_c].index(num)
                        
                        # 뒤집는다.
                        temp = board[cur_r][cur_c][index:][::-1]
                        
                        # 이동하려는 칸에 추가한다.
                        for val in temp:
                            
                            board[move_r][move_c].append(val)

                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                            
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True
                    
                else:
                    
                    # 해당말의 방향만 바꾼다. 이동은 없다.
                    pieces[num-1][2] = moving
                    
        # 영역을 벗어나면 파란색일 때와 똑같이 처리한다. 
        else:

            # 방향을 바꾼다.
            # 동쪽일 때
            if moving == 1:
                
                # 서쪽으로 변경
                moving = 2
                
                move_r, move_c = cur_r, cur_c - 1
            
            # 서쪽일 때
            elif moving == 2:
                
                # 동쪽으로 변경
                moving  = 1
                
                move_r, move_c = cur_r, cur_c + 1
            
            # 북쪽일 때 
            elif moving == 3:
                
                # 남쪽으로 변경
                moving = 4
                
                move_r, move_c = cur_r + 1, cur_c
            
            # 남쪽일 때
            elif moving == 4:
                
                # 북쪽으로 변경
                moving = 3
                
                move_r, move_c = cur_r - 1, cur_c

            index = board[cur_r][cur_c].index(num)
            
            # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
            if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
            
                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 흰색
                if color[move_r][move_c] == 0:
                    
                    # 이동하려는 칸 위에 쌓는다.
                    for val in board[cur_r][cur_c][index:]:
                        
                        board[move_r][move_c].append(val)
                        
                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                    
                # 반대방향이 빨간색
                elif color[move_r][move_c] == 1:
                    
                    index = board[cur_r][cur_c].index(num)
                    
                    # 뒤집는다.
                    temp = board[cur_r][cur_c][index:][::-1]
                    
                    # 이동하려는 칸에 추가한다.
                    for val in temp:
                        
                        board[move_r][move_c].append(val)

                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True
            else:
                
                # 해당말의 방향만 바꾼다. 이동은 없다.
                pieces[num-1][2] = moving
            
    # 이동방향이 서쪽일 때
    elif moving == 2:
        
        move_r, move_c = cur_r, cur_c - 1

        # 영역을 벗어나지 않을 때
        if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
            
            # 흰색일 때
            if color[move_r][move_c] == 0:
                
                index = board[cur_r][cur_c].index(num)
                
                # 이동하려는 칸 위에 쌓는다.
                for val in board[cur_r][cur_c][index:]:
                    
                    board[move_r][move_c].append(val)
                    
                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]
                
                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
                
            # 빨간색일 때
            elif color[move_r][move_c] == 1:
                
                index = board[cur_r][cur_c].index(num)
                
                # 뒤집는다.
                temp = board[cur_r][cur_c][index:][::-1]
                
                # 이동하려는 칸에 추가한다.
                for val in temp:
                    
                    board[move_r][move_c].append(val)

                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]

                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
            
            # 파란색일 때
            elif color[move_r][move_c] == 2:
                
                # 방향을 바꾼다.
                
                # 동쪽일 때
                if moving == 1:
                    
                    # 서쪽으로 변경
                    moving = 2
                    
                    move_r, move_c = cur_r, cur_c - 1
                
                # 서쪽일 때
                elif moving == 2:
                    
                    # 동쪽으로 변경
                    moving  = 1
                    
                    move_r, move_c = cur_r, cur_c + 1
                
                # 북쪽일 때 
                elif moving == 3:
                    
                    # 남쪽으로 변경
                    moving = 4
                    
                    move_r, move_c = cur_r + 1, cur_c
                
                # 남쪽일 때
                elif moving == 4:
                    
                    # 북쪽으로 변경
                    moving = 3
                    
                    move_r, move_c = cur_r - 1, cur_c

                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
                if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
                
                    index = board[cur_r][cur_c].index(num)
                    
                    # 반대방향이 흰색
                    if color[move_r][move_c] == 0:
                        
                        # 이동하려는 칸 위에 쌓는다.
                        for val in board[cur_r][cur_c][index:]:
                            
                            board[move_r][move_c].append(val)
                            
                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                        
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True
                        
                    # 반대방향이 빨간색
                    elif color[move_r][move_c] == 1:
                        
                        index = board[cur_r][cur_c].index(num)
                        
                        # 뒤집는다.
                        temp = board[cur_r][cur_c][index:][::-1]
                        
                        # 이동하려는 칸에 추가한다.
                        for val in temp:
                            
                            board[move_r][move_c].append(val)

                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                            
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True 
                    
                else:
                    
                    # 해당말의 방향만 바꾼다. 이동은 없다.
                    pieces[num-1][2] = moving
                    
        # 영역을 벗어나면 파란색일 때와 똑같이 처리한다. 
        else:

            # 방향을 바꾼다.
            # 동쪽일 때
            if moving == 1:
                
                # 서쪽으로 변경
                moving = 2
                
                move_r, move_c = cur_r, cur_c - 1
            
            # 서쪽일 때
            elif moving == 2:
                
                # 동쪽으로 변경
                moving  = 1
                
                move_r, move_c = cur_r, cur_c + 1
            
            # 북쪽일 때 
            elif moving == 3:
                
                # 남쪽으로 변경
                moving = 4
                
                move_r, move_c = cur_r + 1, cur_c
            
            # 남쪽일 때
            elif moving == 4:
                
                # 북쪽으로 변경
                moving = 3
                
                move_r, move_c = cur_r - 1, cur_c

            index = board[cur_r][cur_c].index(num)
            
            # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
            if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
            
                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 흰색
                if color[move_r][move_c] == 0:
                    
                    # 이동하려는 칸 위에 쌓는다.
                    for val in board[cur_r][cur_c][index:]:
                        
                        board[move_r][move_c].append(val)
                        
                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                    
                # 반대방향이 빨간색
                elif color[move_r][move_c] == 1:
                    
                    index = board[cur_r][cur_c].index(num)
                    
                    # 뒤집는다.
                    temp = board[cur_r][cur_c][index:][::-1]
                    
                    # 이동하려는 칸에 추가한다.
                    for val in temp:
                        
                        board[move_r][move_c].append(val)

                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving
                    
                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                
            else:
                
                # 해당말의 방향만 바꾼다. 이동은 없다.
                pieces[num-1][2] = moving
                
    # 이동방향이 북쪽일 때
    elif moving == 3:
        
        move_r, move_c = cur_r - 1, cur_c

        # 영역을 벗어나지 않을 때
        if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
            
            # 흰색일 때
            if color[move_r][move_c] == 0:
                
                index = board[cur_r][cur_c].index(num)
                
                # 이동하려는 칸 위에 쌓는다.
                for val in board[cur_r][cur_c][index:]:
                    
                    board[move_r][move_c].append(val)
                    
                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]
                
                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
                
            # 빨간색일 때
            elif color[move_r][move_c] == 1:
                
                index = board[cur_r][cur_c].index(num)
                
                # 뒤집는다.
                temp = board[cur_r][cur_c][index:][::-1]
                
                # 이동하려는 칸에 추가한다.
                for val in temp:
                    
                    board[move_r][move_c].append(val)

                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]

                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
            
            # 파란색일 때
            elif color[move_r][move_c] == 2:
                
                # 방향을 바꾼다.
                
                # 동쪽일 때
                if moving == 1:
                    
                    # 서쪽으로 변경
                    moving = 2
                    
                    move_r, move_c = cur_r, cur_c - 1
                
                # 서쪽일 때
                elif moving == 2:
                    
                    # 동쪽으로 변경
                    moving  = 1
                    
                    move_r, move_c = cur_r, cur_c + 1
                
                # 북쪽일 때 
                elif moving == 3:
                    
                    # 남쪽으로 변경
                    moving = 4
                    
                    move_r, move_c = cur_r + 1, cur_c
                
                # 남쪽일 때
                elif moving == 4:
                    
                    # 북쪽으로 변경
                    moving = 3
                    
                    move_r, move_c = cur_r - 1, cur_c

                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
                if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
                
                    index = board[cur_r][cur_c].index(num)
                    
                    # 반대방향이 흰색
                    if color[move_r][move_c] == 0:
                        
                        # 이동하려는 칸 위에 쌓는다.
                        for val in board[cur_r][cur_c][index:]:
                            
                            board[move_r][move_c].append(val)
                            
                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                        
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True 
                        
                    # 반대방향이 빨간색
                    elif color[move_r][move_c] == 1:
                        
                        index = board[cur_r][cur_c].index(num)
                        
                        # 뒤집는다.
                        temp = board[cur_r][cur_c][index:][::-1]
                        
                        # 이동하려는 칸에 추가한다.
                        for val in temp:
                            
                            board[move_r][move_c].append(val)

                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                            
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True 
                    
                else:
                    
                    # 해당말의 방향만 바꾼다. 이동은 없다.
                    pieces[num-1][2] = moving
                    
        # 영역을 벗어나면 파란색일 때와 똑같이 처리한다. 
        else:

            # 방향을 바꾼다.
            # 동쪽일 때
            if moving == 1:
                
                # 서쪽으로 변경
                moving = 2
                
                move_r, move_c = cur_r, cur_c - 1
            
            # 서쪽일 때
            elif moving == 2:
                
                # 동쪽으로 변경
                moving  = 1
                
                move_r, move_c = cur_r, cur_c + 1
            
            # 북쪽일 때 
            elif moving == 3:
                
                # 남쪽으로 변경
                moving = 4
                
                move_r, move_c = cur_r + 1, cur_c
            
            # 남쪽일 때
            elif moving == 4:
                
                # 북쪽으로 변경
                moving = 3
                
                move_r, move_c = cur_r - 1, cur_c

            index = board[cur_r][cur_c].index(num)
            
            # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
            if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
            
                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 흰색
                if color[move_r][move_c] == 0:
                    
                    # 이동하려는 칸 위에 쌓는다.
                    for val in board[cur_r][cur_c][index:]:
                        
                        board[move_r][move_c].append(val)
                        
                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                    
                # 반대방향이 빨간색
                elif color[move_r][move_c] == 1:
                    
                    index = board[cur_r][cur_c].index(num)
                    
                    # 뒤집는다.
                    temp = board[cur_r][cur_c][index:][::-1]
                    
                    # 이동하려는 칸에 추가한다.
                    for val in temp:
                        
                        board[move_r][move_c].append(val)

                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                
            else:
                
                # 해당말의 방향만 바꾼다. 이동은 없다.
                pieces[num-1][2] = moving
        
    # 이동방향이 남쪽일 때
    elif moving == 4:
        
        move_r, move_c = cur_r + 1, cur_c

        # 영역을 벗어나지 않을 때
        if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
            
            # 흰색일 때
            if color[move_r][move_c] == 0:
                
                index = board[cur_r][cur_c].index(num)
                
                # 이동하려는 칸 위에 쌓는다.
                for val in board[cur_r][cur_c][index:]:
                    
                    board[move_r][move_c].append(val)
                    
                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]
                
                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
                
            # 빨간색일 때
            elif color[move_r][move_c] == 1:
                
                index = board[cur_r][cur_c].index(num)
                
                # 뒤집는다.
                temp = board[cur_r][cur_c][index:][::-1]
                
                # 이동하려는 칸에 추가한다.
                for val in temp:
                    
                    board[move_r][move_c].append(val)

                    # 조각의 위치를 갱신해준다.
                    pieces[val-1][1] = [move_r, move_c]

                # 원래있던 위치에 말을 지운다.
                for _ in range(len(board[cur_r][cur_c][index:])):
                    
                    del board[cur_r][cur_c][-1]

                # 말이 4개 이상되면 게임이 종료된다.
                if len(board[move_r][move_c]) >= 4:
                    
                    finish = True 
            
            # 파란색일 때
            elif color[move_r][move_c] == 2:
                
                # 방향을 바꾼다.
                
                # 동쪽일 때
                if moving == 1:
                    
                    # 서쪽으로 변경
                    moving = 2
                    
                    move_r, move_c = cur_r, cur_c - 1
                
                # 서쪽일 때
                elif moving == 2:
                    
                    # 동쪽으로 변경
                    moving  = 1
                    
                    move_r, move_c = cur_r, cur_c + 1
                
                # 북쪽일 때 
                elif moving == 3:
                    
                    # 남쪽으로 변경
                    moving = 4
                    
                    move_r, move_c = cur_r + 1, cur_c
                
                # 남쪽일 때
                elif moving == 4:
                    
                    # 북쪽으로 변경
                    moving = 3
                    
                    move_r, move_c = cur_r - 1, cur_c

                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
                if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
                
                    index = board[cur_r][cur_c].index(num)
                    
                    # 반대방향이 흰색
                    if color[move_r][move_c] == 0:
                        
                        # 이동하려는 칸 위에 쌓는다.
                        for val in board[cur_r][cur_c][index:]:
                            
                            board[move_r][move_c].append(val)
                            
                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                        
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving

                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True 
                        
                    # 반대방향이 빨간색
                    elif color[move_r][move_c] == 1:
                        
                        index = board[cur_r][cur_c].index(num)
                        
                        # 뒤집는다.
                        temp = board[cur_r][cur_c][index:][::-1]
                        
                        # 이동하려는 칸에 추가한다.
                        for val in temp:
                            
                            board[move_r][move_c].append(val)

                            # 조각의 위치를 갱신해준다.
                            pieces[val-1][1] = [move_r, move_c]

                        # 원래있던 위치에 말을 지운다.
                        for _ in range(len(board[cur_r][cur_c][index:])):
                            
                            del board[cur_r][cur_c][-1]
                            
                        # 해당말의 방향을 바꾼다.
                        pieces[num-1][2] = moving
    
                        # 말이 4개 이상되면 게임이 종료된다.
                        if len(board[move_r][move_c]) >= 4:
                            
                            finish = True 
                    
                else:
                    
                    # 해당말의 방향만 바꾼다. 이동은 없다.
                    pieces[num-1][2] = moving
                    
        # 영역을 벗어나면 파란색일 때와 똑같이 처리한다. 
        else:

            # 방향을 바꾼다.
            # 동쪽일 때
            if moving == 1:
                
                # 서쪽으로 변경
                moving = 2
                
                move_r, move_c = cur_r, cur_c - 1
            
            # 서쪽일 때
            elif moving == 2:
                
                # 동쪽으로 변경
                moving  = 1
                
                move_r, move_c = cur_r, cur_c + 1
            
            # 북쪽일 때 
            elif moving == 3:
                
                # 남쪽으로 변경
                moving = 4
                
                move_r, move_c = cur_r + 1, cur_c
            
            # 남쪽일 때
            elif moving == 4:
                
                # 북쪽으로 변경
                moving = 3
                
                move_r, move_c = cur_r - 1, cur_c

            index = board[cur_r][cur_c].index(num)
            
            # 반대방향이 주어진 영역을 벗어나지 않고 파란색이 아닐 때 이동한다.
            if (0 <= move_r <= N-1 and 0 <= move_c <= N-1) and color[move_r][move_c] != 2:
            
                index = board[cur_r][cur_c].index(num)
                
                # 반대방향이 흰색
                if color[move_r][move_c] == 0:
                    
                    # 이동하려는 칸 위에 쌓는다.
                    for val in board[cur_r][cur_c][index:]:
                        
                        board[move_r][move_c].append(val)
                        
                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                    
                # 반대방향이 빨간색
                elif color[move_r][move_c] == 1:
                    
                    index = board[cur_r][cur_c].index(num)
                    
                    # 뒤집는다.
                    temp = board[cur_r][cur_c][index:][::-1]
                    
                    # 이동하려는 칸에 추가한다.
                    for val in temp:
                        
                        board[move_r][move_c].append(val)

                        # 조각의 위치를 갱신해준다.
                        pieces[val-1][1] = [move_r, move_c]

                    # 원래있던 위치에 말을 지운다.
                    for _ in range(len(board[cur_r][cur_c][index:])):
                        
                        del board[cur_r][cur_c][-1]
                    
                    # 해당말의 방향을 바꾼다.
                    pieces[num-1][2] = moving

                    # 말이 4개 이상되면 게임이 종료된다.
                    if len(board[move_r][move_c]) >= 4:
                        
                        finish = True 
                
            else:
                
                # 해당말의 방향만 바꾼다. 이동은 없다.
                pieces[num-1][2] = moving


# 게임 종료 조건
finish = False
breaken = False

# 체스판의 크기 N과 말의 개수 K가 주어진다.
N, K = map(int, sys.stdin.readline().split())

# 체스판의 색
color = []

# 보드판
board = [[[] for _ in range(N)] for _ in range(N)]

# 턴의 번호
turn = 0

# 체스판의 정보가 주어진다.
# 0은 흰색, 1은 빨간색, 2는 파란색
for _ in range(N):
    
    color.append(list(map(int, sys.stdin.readline().split())))

# 말
pieces = []

# K개의 줄에 말의 정보가 주어진다.
for i in range(1, K+1):
    
    r, c, moving = map(int, sys.stdin.readline().split())

    r -= 1
    c -= 1
    
    board[r][c].append(i)
    
    pieces.append([i, [r,c], moving])

# 게임을 반복한다.
while turn <= 1000:
    
    # 턴 추가
    turn += 1
    
    for piece in pieces:
        
        # 말의 번호
        p_num = piece[0]
        
        # 좌표
        p_coord = piece[1]
        
        # 이동방향
        p_moving = piece[2]
        
        playing(p_num, p_coord, p_moving)
        
        if finish == True:
            
            breaken = True
            break
    
    if breaken == True:
        
        break

# 게임이 종료되는 턴의 번호를 입력한다.
if turn > 1000:
    
    print(-1)

else:
    
    print(turn)