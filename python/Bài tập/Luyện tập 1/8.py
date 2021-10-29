n, m = list(map(int,input().split()))
x, y = list(map(int,input().split()))
k = int(input())
if x == m and (y == 1 or y ==n):
    if k == max(n, m):
        print(k-1)
    else:
        print(k+1)
elif x ==1 and (y == 1 or y ==n):
    if k == max(n, m):
        print(k-1)
    else:
        print(k+1)
else:
    if k == max(n, m):
        print(k+1)
    else:
        print(k+2)
