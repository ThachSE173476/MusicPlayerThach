#doi 1:
doi1_tran1 = list(map(int,input().split()))
doi1_tran2 = list(map(int,input().split()))
doi1_tran3 = list(map(int,input().split()))
#doi 2:
doi2_tran1 = list(map(int,input().split()))
doi2_tran2 = list(map(int,input().split()))
doi2_tran3 = list(map(int,input().split()))
#them danh sach doi 1:
doi1 = []
doi1.append(doi1_tran1)
doi1.append(doi1_tran2)
doi1.append(doi1_tran3)
#them danh sach doi 2:
doi2 = []
doi2.append(doi2_tran1)
doi2.append(doi2_tran2)
doi2.append(doi2_tran3)
#tinh diem cua doi 1:
diem_1 = 0
sothevang_1 = 0
sobanthang_1 = 0
hieusobanthang_1 = 0
for i in range(3):
    if doi1[i][0] > doi1[i][1]:
        diem_1 +=3
    elif doi1[i][0] < doi1[i][1]:
        diem_1 += 0
    else:
        diem_1 += 1
    sobanthang_1 += doi1[i][0]
    sothevang_1 += doi1[i][2]
    hieusobanthang_1 += (doi1[i][0]-doi1[i][1])
#tinh diem cua doi 2:
diem_2 = 0
sothevang_2 = 0
sobanthang_2 = 0
hieusobanthang_2 = 0
for i in range(3):
    if doi2[i][0] > doi2[i][1]:
        diem_2 +=3
    elif doi2[i][0] < doi2[i][1]:
        diem_2 += 0
    else:
        diem_2 += 1
    sobanthang_2 += doi2[i][0]
    sothevang_2 += doi2[i][2]
    hieusobanthang_2 += (doi2[i][0]-doi2[i][1])
#so sanh:
#so diem truoc:
if diem_1 > diem_2:
    print(diem_1,hieusobanthang_1,sobanthang_1,sothevang_1)
elif diem_1 < diem_2:
    print(diem_2,hieusobanthang_2,sobanthang_2,sothevang_2)
else:
#so ve hieu so:
    if hieusobanthang_1 > hieusobanthang_2:
        print(diem_1,hieusobanthang_1,sobanthang_1,sothevang_1)
    elif hieusobanthang_1 < hieusobanthang_2:
        print(diem_2,hieusobanthang_2,sobanthang_2,sothevang_2)
    else:
#so ve so ban thang:
        if sobanthang_1 > sobanthang_2:
            print(diem_1,hieusobanthang_1,sobanthang_1,sothevang_1)
        elif sobanthang_1 < sobanthang_2:
            print(diem_2,hieusobanthang_2,sobanthang_2,sothevang_2)
        else:
#so ve so the vang:
            if sothevang_1 < sothevang_2:
                print(diem_1,hieusobanthang_1,sobanthang_1,sothevang_1)
            elif sothevang_1 > sothevang_2:
                print(diem_2,hieusobanthang_2,sobanthang_2,sothevang_2)
            else:
                print(diem_2,hieusobanthang_2,sobanthang_2,sothevang_2)