row=list() # 공백 리스트 생성

N,M=map(int,input().split())

for i in range(N):
    row.append(list(map(int,input().split()))) # 입력받은 값들을 list에 추가

mode=list() #공백 리스트 생성

#각 행에서 최소값을 구해서 mode라는 공백리스트에 삽입 
for i in range(N):
    min=row[i][0]
    for j in range(M):
        if min<=row[i][j]:
            min=min
        else:
            min=row[i][j]
    mode.append(min)

#mode라는 리스트에서 가장 큰 값을 max 
max=mode[0]

for i in range(N):
    if mode[i]<=max:
        max=max
    else:
        max=mode[i]

print(max)
            

            



    
    
    
