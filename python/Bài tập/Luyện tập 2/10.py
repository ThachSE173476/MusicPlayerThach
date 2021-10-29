n = int(input())
so_may_con_lai = list(map(int,input().split()))
so_may_toi_thieu = max(so_may_con_lai)-min(so_may_con_lai)+1
print(so_may_toi_thieu-n)