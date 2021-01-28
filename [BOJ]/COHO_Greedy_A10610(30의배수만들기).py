list=[]

n=int(input())
 
num=[1,10**1,10**2,10**3,10**4,10**5]

num.sort(reverse=True)   #내림차순 정렬 

while True:
    value=n%10
    list.append(value)
    n=n//10
    if(n==0):
        break

list.sort(reverse=True) #오름차순 정렬

result=""

for i in range(len(list)):
    result+=str(list[i])
    
a=int(result)

if a%30==0:
    print(a)
else:
    print(-1)


