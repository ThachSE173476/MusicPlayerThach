print("Nguoi choi chon(keo, bua, bao): ", end="")
player = input()

import random
comChoice = ["keo", "bua", "bao"]
com = random.choice(comChoice)
print("May chon:",com)

if player == com:
    print("Hoa")
elif player == "keo":
    if com == "bua":
        print("Thua")
    else:
        print("Thang")
elif player == "bua":
    if com == "bao": 
        print("Thua")
    else:
        print("Thang")
elif player == "bao":
    if com == "keo":
        print("Thua")
    else:
        print("Thang")