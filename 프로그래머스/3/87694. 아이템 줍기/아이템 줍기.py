def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * 101 for _ in range(101)]

    # init 부분
    # 2배로 늘려서 생각
    # 좌표의 값 0 이면 빈 곳 중 외부, 1 은 테두리, -1은 도형 내부
    field = [[0] * 101 for _ in range(101)]
    for x1, y1, x2, y2 in rectangle:
        for y_ in range(2 * y1, 2 * y2 + 1):
            for x_ in range(2 * x1, 2 * x2 + 1):
                # 범위 조심, 꼭짓점 범위 가지!, range에서 명시한 범위와 다른 것 조심
                if 2 * y1 < y_ < 2 * y2 and 2 * x1 < x_ < 2 * x2: 
                    field[y_][x_] = -1
                else:
                    if field[y_][x_] == 0:
                        field[y_][x_] = 1
    
    # BFS를 활용해 최소 거리 찾기
    q = deque([(2 * characterX, 2 * characterY, 0)])
    visited[2 * characterY][2 * characterX] = True
    
    while q:
        x, y, dist = q.popleft()
        if x == 2 * itemX and y == 2 * itemY:
            return dist / 2
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0<=nx<101 and 0<=ny<101 and not visited[ny][nx] and field[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((nx, ny, dist + 1))
    return -1 # 조건 상 일어날 수 없는 코드
    









# def solution(rectangle, characterX, characterY, itemX, itemY):
#     from collections import deque
    
#     answer = 0
#     '''
#         | 1 | 1 |
#           -   -  
#         | 1 | 1 |
#           _   _
        
#         위 상황 같이 'ㄷ' 자일 때 dir 사용 시 잘못된 좌표를 체킹하게 됨
#         이 예외를 해결하기 위해 전체 맵을 2배로 늘려준다
#     '''
#     # 1 1 
#     # 1 1
#     field = [[-1] * 101 for _ in range(101)] # 51 * 2 (1 - 50)
    
#     for x1, y1, x2, y2 in rectangle:
#         for i in range(2*y1, 2*y2+1):
#             for j in range(2*x1, 2*x2+1):
#                 if 2*y1 < i < 2*y2 and 2*x1 < j < 2*x2:
#                     field[i][j] = 0
#                 else:
#                     if field[i][j] == -1:
#                         field[i][j] = 1
    
#     q = deque()
#     q.append((characterX*2, characterY*2, 0))
#     visited = [[False] * 101 for _ in range(101)]
#     # Y, X  - 행, 열 헷갈리지 말자!!
#     visited[characterY*2][characterX*2] = True
    
#     dir = [(0,1), (0,-1), (1,0), (-1,0)]
#     while q:
#         x, y, dist = q.popleft()
#         if x == itemX*2 and y == itemY*2:
#             return dist/2
#         for xi, yj in dir:
#             dx, dy = x + xi, y + yj
#             if 1<=dx<101 and 1<=dy<101 and field[dy][dx] == 1:
#                 if visited[dy][dx]: continue
#                 visited[dy][dx] = True
#                 q.append((dx,dy,dist+1))
    
#     return 0