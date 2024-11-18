def solution(sizes):
    answer = 0
    max_width, max_height = 0, 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    
    answer = max_width * max_height
    return answer