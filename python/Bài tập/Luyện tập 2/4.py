n = int(input())
tap_hop_so =[]
for i in range(n):
    tap_hop_so.append(int(input()))
cach_doc_0_9 = ['zero','one','two','three','four','five','six','seven','eight','nine']
cach_doc_10_19 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
cach_doc_20_90 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def sohangdonvi(a):
    return cach_doc_0_9[a]
def somuoimay(a):
    return cach_doc_10_19[a-10]
def sohangchuc(a):
    hang_chuc = a//10
    hang_donvi = a %10
    if hang_donvi == 0:
        b = cach_doc_20_90[hang_chuc]
    else:
        b = cach_doc_20_90[hang_chuc]+'-'+cach_doc_0_9[hang_donvi]
    return b
def cach_doc_so_nho_hon100(a):
    if 0<= a <=9:
        c = sohangdonvi(a)
    elif 10<= a <=19:
        c = somuoimay(a)
    elif 20<= a <=99:
        c = sohangchuc(a)
    return c
def sohangtram(a):
    hang_tram = a//100
    hang_chuc_va_don_vi = a%100
    if hang_chuc_va_don_vi ==0:
        b = cach_doc_0_9[hang_tram]+' hundred'
    else:
        b = cach_doc_0_9[hang_tram]+' hundred '+cach_doc_so_nho_hon100(hang_chuc_va_don_vi)
    return b
def sohangngan(a):
    hang_ngan = a //1000
    hang_tram = a %1000
    if hang_tram == 0:
        b = cach_doc_0_9[hang_ngan]+' thousand'
    elif hang_tram<100:
        b = cach_doc_0_9[hang_ngan]+' thousand, '+cach_doc_so_nho_hon100(hang_tram) 
    else:
        b = cach_doc_0_9[hang_ngan]+' thousand, '+sohangtram(hang_tram)
    return b
for i in range(n):
    if 0 <= tap_hop_so[i] <= 9:
        print(sohangdonvi(tap_hop_so[i]))
    elif 10<= tap_hop_so[i]<=19:
        print(somuoimay(tap_hop_so[i]))
    elif 20<= tap_hop_so[i]<=99:
        print(sohangchuc(tap_hop_so[i]))
    elif 100<= tap_hop_so[i]<=999:
        print(sohangtram(tap_hop_so[i]))
    elif 1000<= tap_hop_so[i]<=9999:
        print(sohangngan(tap_hop_so[i]))