tre_trung, xinh_dep, co_gau, giau_co = list(map(int,input().split()))
if xinh_dep == co_gau == 1:
    print(1)
elif xinh_dep == tre_trung and co_gau == giau_co==1:
    print(1)
elif tre_trung==xinh_dep ==co_gau == giau_co==0:
    print(1)
elif tre_trung ==xinh_dep==co_gau==0 and giau_co==1:
    print(1)
else:
    print(0)

