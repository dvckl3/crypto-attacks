from math import ceil, sqrt
def bsgs(g,h,p):
  N=ceil(sqrt(p-1))
  tbl={pow(g,i,p):i for i in range(N)}
  c = pow(g, N * (p - 2), p)
  for j in range(N):
    y=(h*pow(c,j,p))%p
    if y in tbl:
      return j*N+tbl[y]
  return None

  
print(bsgs(7894352216, 355407489, 604604729))

