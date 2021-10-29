chuoi = input()
dem = 0
for start in range(len(chuoi)):
    for end in range(start+1,len(chuoi)+1):
        chuoi_con = chuoi[start:end]
        if chuoi_con == chuoi_con[ : :-1]:
            dem +=1
print(dem)
    