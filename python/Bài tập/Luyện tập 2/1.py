r, c = list(map(int,input().split()))
mang = []
for i in range(r):
    mang.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        mang[i][j] = str(mang[i][j])
dodaicot = []
for j in range(c):
    dodai = len(mang[0][j])
    for i in range(1,r):
        if len(mang[i][j])> dodai:
            dodai = len(mang[i][j])
    dodaicot.append(dodai)
for i in range(r):
    for j in range(c):
        print(" "*(dodaicot[j]-len(mang[i][j]))+mang[i][j],end=" ")
    print("")

