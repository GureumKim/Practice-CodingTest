n = int(input())
target = int(input())

map_ = [[0]*n for _ in range(n)]
d = 0
y, x = 0, 0
rest = n**2

while rest:
    map_[y][x] = rest
    rest -= 1
    if d == 0 :
        if y+1>=n or map_[y+1][x]:
            x+=1
            d = (d + 1) % 4
        else:
            y+=1
    elif d == 1:
        if x+1>=n or map_[y][x+1]:
            y-=1
            d = (d + 1) % 4
        else:
            x+=1
    elif d == 2:
        if y < 1 or map_[y-1][x]:
            x -=1
            d = (d + 1) % 4
        else:
            y-=1
    elif d == 3:
        if x < 1 or map_[y][x-1]:
            y +=1
            d = (d + 1) % 4
        else:
            x-=1



ans = None
for i in range(n):
    for j in range(n):
        print(map_[i][j], end=" ")
        if map_[i][j] == target:
            ans = (i+1, j+1)
    print("")
print(*ans)