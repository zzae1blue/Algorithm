# 21608 상어 초등학교

import sys
        
# 자리를 채우는 함수
def fill(std):
    
    # 학생 정보와, 좋아하는 학생을 꺼내옵니다.
    std_info = std[0]
    std_like = set(std[1:])
    
    # Rule 1,2,3을 각각 만족하는 정보를 담은 리스트
    rule_1 = []
    rule_2 = []
    rule_3 = []
    
    # Rule 1
    for r in range(N):
        
        for c in range(N):
            
            # 비어있는 칸 조사
            if grid[r][c] == 0:
                
                # [r,c] 상하좌우에 좋아하는 사람이 몇명 분포해 있는지 조사
                cnt = 0
                
                # 4방향 탐색
                for t in range(4):
                    
                    move_r = r + dr[t]
                    move_c = c + dc[t]
                    
                    # 주어진 범위를 벗어나지 않으면서
                    if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                        
                        # 좋아하는 학생이 인접한지 여부
                        if grid[move_r][move_c] in std_like:
                            
                            cnt += 1
                
                rule_1.append([cnt, [r,c]])
    
    # 좋아하는 사람이 주변에 몇명인지를 기준으로 내림차순 정렬합니다.
    rule_1.sort(key = lambda x:-x[0])          
    
    max_val = rule_1[0][0]
    
    max_val_cnt = 0
    
    # Rule 2로 가기위한 후보
    rule_2_candidate = []
    
    for val in rule_1:
        
        val_cnt, val_coord = val
        
        if val_cnt == max_val:
            
            max_val_cnt += 1
            
            rule_2_candidate.append(val_coord)
    
    # Rule 1에서 끝나는 조건
    if max_val_cnt == 1:
        
        val_cnt, val_coord = rule_1[0]
        
        val_r, val_c = val_coord
        
        grid[val_r][val_c] = std_info
        return
    
    # Rule 2
    else:
        
        for candidate in rule_2_candidate:
            
            r, c = candidate
            empty_cnt = 0
            
            for t in range(4):
                
                move_r = r + dr[t]
                move_c = c + dc[t]
                
                # 범위를 벗어나지 않으면서
                if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                    
                    # 주변 칸이 비어있을 때
                    if grid[move_r][move_c] == 0:
                        
                        empty_cnt += 1
            
            # Rule 3로 가기위한 후보
            rule_2.append([empty_cnt, candidate])
        
        # 비어있는 칸이 가장 많은 칸 순으로 정렬한다.
        rule_2.sort(key = lambda x:-x[0])
        
        max_empty_val = rule_2[0][0]
        
        max_empty_val_cnt = 0
        
        # Rule 3로 가기위한 후보
        rule_3_candidate = []
        
        for val in rule_2:
            
            val_cnt, val_coord = val
            
            if val_cnt == max_empty_val:
                
                max_empty_val_cnt += 1
                
                rule_3_candidate.append(val_coord)
        
        # Rule 2에서 끝나는 조건
        if max_empty_val_cnt == 1:
            
            val_cnt, val_coord = rule_2[0]
            
            val_r, val_c = val_coord
            
            grid[val_r][val_c] = std_info
            return

        # Rule 3
        else:
            
            # 좌표 후보군을 추가
            for candidate in rule_3_candidate:
                
                r, c = candidate
                
                rule_3.append([r,c])
            
            rule_3.sort(key = lambda x:(x[0],x[1]))
            
            val_r, val_c = rule_3[0]
            
            grid[r][c] = std_info
            return

# 인접한 칸, abs(r1-r2) + abs(c1-c2) = 1 : 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] 
    
# N이 주어집니다.
N = int(sys.stdin.readline().rstrip())

# 격자 초기화
grid = [[0] * N for _ in range(N)]

# 학생 정보 : [학생의 번호, 좋아하는 학생 4명]
students = []

# N**2개의 줄에 학생 번호와, 해당 학생이 좋아하는 4명의 번호가 주어집니다.
for _ in range(N**2):
    
    seq = list(map(int, sys.stdin.readline().split()))
    
    students.append(seq)

for i in range(N**2):
    
    # 자리를 채우는 함수 실행
    fill(students[i])

# 학생 정렬
students.sort(key = lambda x:x[0])

# 만족도의 총합
total = 0

cnt = 0

for i in range(N**2):
    
    # 학생번호와 좋아하는 학생 수
    std_id = students[i][0]
    std_like = set(students[i][1:])
    
    for r in range(N):
        
        for c in range(N):
            
            if grid[r][c] == std_id:
                
                like_cnt = 0
                
                for t in range(4):
                    
                    move_r = r + dr[t]
                    move_c = c + dc[t]
                    
                    if 0 <= move_r <= N-1 and 0 <= move_c <= N-1:
                        
                        if grid[move_r][move_c] in std_like:
                            
                            like_cnt += 1
                
                if like_cnt == 0:
                    
                    continue
                
                elif like_cnt == 1:
                    
                    total += 1
                    
                elif like_cnt == 2:
                    
                    total += 10
                
                elif like_cnt == 3:
                    
                    total += 100
                
                elif like_cnt == 4:
                    
                    total += 1000
    
# 첫째 줄에 학생의 만족도의 총 합을 출력한다.
print(total)