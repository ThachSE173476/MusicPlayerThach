import math
inp = input().split(sep=" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
#a,b,c = list(map(float, input().split()))
x = a**5 - 2*math.sqrt(math.fabs(b)) + a*b*c
print("{:.2f}".format(x))
#print(f'{a**5 - 2*math.sqrt(math.fabs(b)) + a*b*c:.2f}')