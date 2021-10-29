n = int(input())
day_so =[]
for i in range(n):
    day_so.append(int(input()))
so_la_ma = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
so_tu_1_9 =['','I','II','III','IV','V','VI','VII','VIII','IX']
so_tu_10_90 =['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
so_tu_100_900 =['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
so_tu_1000_5000 =['','M','MM','MMM']
def sotu1den10(a):
    b = so_tu_1_9[a]
    return b
def sotu10den99(a):
    hang_chuc = a//10
    hang_donvi= a%10
    b= so_tu_10_90[hang_chuc]+so_tu_1_9[hang_donvi]
    return b
def sotu100den999(a):
    hang_tram = a//100
    hang_chuc_va_donvi = a%100
    b = so_tu_100_900[hang_tram]+sotu10den99(hang_chuc_va_donvi)
    return b
def sotu1000den3999(a):
    hang_ngan = a//1000
    hang_tram_va = a%1000
    b = so_tu_1000_5000[hang_ngan]+sotu100den999(hang_tram_va)
    return b
for i in range(n):
    if 0< day_so[i]<=9:
        print(sotu1den10(day_so[i]))
    elif 10<= day_so[i]<=99:
        print(sotu10den99(day_so[i]))
    elif 100<= day_so[i]<=999:
        print(sotu100den999(day_so[i]))
    elif 1000<= day_so[i]<=3999:
        print(sotu1000den3999(day_so[i]))
    