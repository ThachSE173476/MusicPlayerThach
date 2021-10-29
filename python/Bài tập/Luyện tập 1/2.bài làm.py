n = int(input())#so hoc sinh trong lop
k = int(input())#so de thi
p = int(input())#hang cua Alice dang ngoi
q = int(input())-1#vi tri cot cua Alice
cot_out = 0
hang_out = 0
#tao mang 2 chieu
if n % 2 ==0:
    sohang =n//2
    cho = [[h,h] for h in range(sohang+1)]
    d = 1
    for i in range(1,sohang+1):
        for j in range(2):
            cho[i][j] = d
            if d == k:
                d =1
            else:
                d +=1
else:
    sohang = (n+1)//2
    cho = [[h,h] for h in range(sohang+1)]
    d = 1
    for i in range(1,sohang):
        for j in range(2):
            cho[i][j] = d
            if d == k:
                d =1
            else:
                d +=1
    cho[sohang][0] = d
    cho[sohang][1] = 0
#xu li mang
if k %2 == 0:
    for i in range(p-1,0,-1):#tim dang truoc
        for j in range(2):
            if cho[p][q] == cho[i][j]:
                hang_out = i
                cot_out = j +1
                break
        if hang_out != 0 and cot_out != 0:
            break
    for i in range(p+1,sohang+1):#tim dang sau
        for j in range(2):
            if cho[p][q] == cho[i][j]:
                hang_out = i
                cot_out = j +1
                break
        if hang_out != 0 and cot_out != 0:
            break       
else:
    for i in range(p-1,0,-1):#tim dang truoc
        for j in range(2):
            if cho[p][q] == cho[i][j]:
                hang_out=i
                cot_out= j +1
                break
        if hang_out != 0 and cot_out != 0:
            break
    for h in range(p+1,sohang+1):#tim dang sau
        for k in range(2):
            if cho[p][q] == cho[h][k]:
                hang_out = h
                cot_out = k+1
                break
        if hang_out != 0 and cot_out != 0:
            break
    if i==1 and h == sohang:
        hang_out=0
        cot_out =0
    elif p-i < p-h:
        hang_out = i
        cot_out = j +1
    elif p-i > p-h:
        hang_out = h
        cot_out = k +1
    elif p-i == p-h:
        hang_out=i
        cot_out = j +1
#output
if hang_out == 0 and cot_out == 0:
    print(-1) 
else:
    print(hang_out,cot_out)      
        