def check(dy,dx,dir,cnt):
    global total
    if dy==m or dx==n or map_[dy][dx]:
        dir = (dir+1)%4
        cnt += 1
        return 1, dir, cnt
    else:
        map_[dy][dx] = 1
        total+=1
        return 0, dir, cnt

m,n = map(int,input().split())
map_ = [[0]*n for _ in range(m)]
map_[0][0] = 1
cnt = 0
total = 1
end_point = m*n
# di = 0,1,2,3 (우,하,좌,상)
y,x, di = 0,0,0
while total < end_point:
    if di == 0:
        x+=1
        res, di, cnt = check(y,x,di,cnt)
        if res:
            x-=1
    elif di == 1:
        y+=1
        res, di, cnt = check(y, x, di, cnt)
        if res:
            y-=1
    elif di == 2:
        x-=1
        res, di, cnt = check(y, x, di, cnt)
        if res:
            x+=1
    else:
        y -=1
        res, di, cnt = check(y, x, di, cnt)
        if res:
            y+=1
print(cnt)