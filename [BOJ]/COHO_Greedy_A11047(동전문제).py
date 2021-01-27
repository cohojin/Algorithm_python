n,k=map(int,input().split()) # 동전종류 , 동전 합

money=[]

for i in range(n):
    i=int(input()) #n개를 입력받고
    money.append(i) #리스트에 넣기


money.sort(reverse=True) #입력받은 money를 내림차순으로 정리하고

 

count=0 #몇가지 종류가 쓰였는지
sum=0 #한종류를 몇번사용했는지

 

for i in range(len(money)):
    if(k>=money[i]):
        sum=k//money[i]
        count+=sum
        k=k%money[i]
print(count)
