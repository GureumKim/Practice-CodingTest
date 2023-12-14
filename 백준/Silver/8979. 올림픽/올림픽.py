n, k = map(int,input().split())
data = [tuple(map(int,input().split())) for _ in range(n)]
data = sorted(data,key=lambda x: (x[1],x[2],x[3]),reverse=True)
rank,cnt = 0,0
for country in data:
    if country[1] != data[rank][1]:
        rank +=cnt
        cnt = 1
    elif country[2] != data[rank][2]:
        rank+=cnt
        cnt = 1
    elif country[3] != data[rank][3]:
        rank+=cnt
        cnt = 1
    else:
        cnt += 1

    # print(country[0])
    # print(rank)
    # print(cnt)
    # print("===")

    if country[0] == k:
        print(rank+1)
        break