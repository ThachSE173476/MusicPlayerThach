nam = int(input())
can = ['CANH','TAN','NHAM','QUY','GIAP','AT','BINH','DINH','MAU','KY']
chi = ['THAN','DAU','TUAT','HOI',"TY'",'SUU','DAN','MAO','THIN','TY.','NGO','MUI']
if nam <=0:
    nam +=1
print(can[nam%10],chi[nam%12])
