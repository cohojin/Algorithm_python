N,M = map(int, input().split()) # N>=K

count= 0 #연산을 한번 할때마다 카운트가 늘어난다. 

# N과M이 같아지는 순간 1증가시키고 연산을 한번 할때마다 1증가 N==1이면 break를 통해 빠져나옴

while(True):
    if(N==M):
        count+=1
        break
     
    if(N==1): #만약 N이 M과 같지 않고 M보다 작은 숫자가 나오면 1일때 탈출한다. 
        break
    
    if(N%M !=0 ):
        N-=1
        count+=1
    else:
        N=N//M
        count+=1


print(count)
    
    


