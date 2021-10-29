a,b,c = list(map(float, input().split()))
import math
print(f'{a**5 - 2*math.sqrt(math.fabs(b)) + a*b*c:.2f}')
