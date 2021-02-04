n,m=map(int,input().split()) #세로,가로
#오른쪽으로만 움직일수있다. 

if n==1:
  count=1
elif n==2:
  count = min(4,(m+1)//2)
elif n>=3:
  if(m<=6):
    print(min(m,4))
  else:
    print(m-2)
