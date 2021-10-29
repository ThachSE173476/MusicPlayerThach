n = int(input())
mang = list(map(int,input().split()))
so_max = mang.count(max(mang))
so_min = mang.count(min(mang))
if n == 2:
    print(0)
else:
    if so_min == so_max and so_max >1 and so_min > 1:
        print(max(mang)-min(mang))
    elif so_min < so_max:
        mang.remove(min(mang))
        print(max(mang)-min(mang))
    elif so_min > so_max:
        mang.remove(max(mang))
        print(max(mang)-min(mang))
    elif so_max == so_min == 1:
        mang2 = mang.copy()
        mang.remove(max(mang))
        mang2.remove(min(mang2))
        if (max(mang) - min(mang)) >(max(mang2) - min(mang2)):
            print(max(mang2) - min(mang2))
        elif (max(mang) - min(mang)) <(max(mang2) - min(mang2)):
            print(max(mang) - min(mang))
        else:
            print(max(mang2) - min(mang2))


        
