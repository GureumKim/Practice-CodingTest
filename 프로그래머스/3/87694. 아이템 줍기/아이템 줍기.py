def solution(rectangle, characterX, characterY, itemX, itemY):
    from collections import deque
    
    answer = 0
    '''
        | 1 | 1 |
          -   -  
        | 1 | 1 |
          _   _
        
        위 상황 같이 'ㄷ' 자일 때 dir 사용 시 잘못된 좌표를 체킹하게 됨
        이 예외를 해결하기 위해 전체 맵을 2배로 늘려준다
    '''
    # 1 1 
    # 1 1
    field = [[-1] * 101 for _ in range(101)] # 51 * 2 (1 - 50)
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*y1, 2*y2+1):
            for j in range(2*x1, 2*x2+1):
                if 2*y1 < i < 2*y2 and 2*x1 < j < 2*x2:
                    field[i][j] = 0
                else:
                    if field[i][j] == -1:
                        field[i][j] = 1
    
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    visited = [[False] * 101 for _ in range(101)]
    # Y, X  - 행, 열 헷갈리지 말자!!
    visited[characterY*2][characterX*2] = True
    
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    while q:
        x, y, dist = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return dist/2
        for xi, yj in dir:
            dx, dy = x + xi, y + yj
            if 1<=dx<101 and 1<=dy<101 and field[dy][dx] == 1:
                if visited[dy][dx]: continue
                visited[dy][dx] = True
                q.append((dx,dy,dist+1))
    
    return 0