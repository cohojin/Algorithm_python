
sum=0

N,M,K=map(int,input().split())

data=list(map(int,input().split()))

data.sort() #[2,4,4,5,6]

while ( M>=1 ):
    for i in range(0,K):
        sum+=data[4]
        M-=1
    sum+=data[3]
    M-=1
    for i in range(0,K):
        sum+=data[4]
        M-=1
    sum+=data[3]
    M-=1
print(sum)
    
    
    

