from collections import deque

def extract_blocks(board, value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    blocks = []

    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        block = []
        min_x, min_y = x, y

        while queue:
            cx, cy = queue.popleft()
            block.append((cx, cy))
            min_x, min_y = min(min_x, cx), min(min_y, cy)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == value:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        # 블록의 좌표를 기준점을 (0, 0)으로 정규화
        normalized_block = [(x - min_x, y - min_y) for x, y in block]
        normalized_block.sort()  # 블록의 순서를 정렬하여 비교 가능하게 만듦
        return normalized_block

    for i in range(n):
        for j in range(n):
            if board[i][j] == value and not visited[i][j]:
                blocks.append(bfs(i, j))

    return blocks

def rotate(block):
    return [(y, -x) for x, y in block]

def generate_rotations(block):
    rotations = []
    current = block
    for _ in range(4):
        current = rotate(current)
        # 정규화 후 정렬
        min_x = min(x for x, y in current)
        min_y = min(y for x, y in current)
        normalized = sorted((x - min_x, y - min_y) for x, y in current)
        rotations.append(normalized)
    return rotations

def solution(game_board, table):
    game_board_blocks = extract_blocks(game_board, 0)  # 빈 공간 추출
    table_blocks = extract_blocks(table, 1)  # 테이블의 퍼즐 조각 추출

    used = [False] * len(table_blocks)  # 사용된 블록 체크
    total_filled = 0

    for gb_block in game_board_blocks:
        for i, tb_block in enumerate(table_blocks):
            if used[i]:
                continue  # 이미 사용된 블록은 스킵

            tb_rotations = generate_rotations(tb_block)
            if gb_block in tb_rotations:
                total_filled += len(gb_block)  # 채워진 칸 수 추가
                used[i] = True  # 해당 블록 사용 처리
                break  # 다음 빈 공간으로 이동

    return total_filled