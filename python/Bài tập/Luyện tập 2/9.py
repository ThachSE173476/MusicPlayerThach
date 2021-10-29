so_thi_sinh, stt = list(map(int,input().split()))
so_diem = list(map(int,input().split()))
if so_diem[stt-1] > 0:
    b = so_diem[stt:]
    print(stt+ b.count(so_diem[stt-1]))
else:
    so_thi_sinh_duoc_du_thi = 0
    for i in range(stt):
        if so_diem[i]>0:
            so_thi_sinh_duoc_du_thi += 1
    print(so_thi_sinh_duoc_du_thi)

