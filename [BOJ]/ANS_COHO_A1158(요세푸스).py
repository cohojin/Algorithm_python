n ,k = map(int,input().split())  # 숫자를 입력받고 

list_n=[i for i in range(1, n+1)]  #1부터 n까지 숫자를 넣는다.

index=k-1

while len(list_n) !=1:
    if index>=len(list_n):
        index%=len(list_n)
    print(list_n.pop(index), end=",")
    index+=(k-1)
    
print(list_n[0])
    
