k, t =list(map(int,input().split()))
ga = [i for i in range(k)]+ [i for i in range(k,-1,-1)]
if t<= 2*k:
  print(ga[t])
else:
  print(ga[t%(2*k)]) 