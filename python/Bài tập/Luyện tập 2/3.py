n, m = list(input().split())
do_dai_n = len(n)
so_n_can_tim = 0
if int(n) >int(m):
    print(0)
elif int(n) == int(m):
    print(1)
else:
    if int(m) < int(n) + (int(m)//(10**do_dai_n))*10**do_dai_n:
        print(int(m)//(10**do_dai_n))
    else:
        print(int(m)//(10**do_dai_n)+1)
