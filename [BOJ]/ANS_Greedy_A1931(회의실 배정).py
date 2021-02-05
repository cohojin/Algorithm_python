n= int(input()) #회의의 수

time=[]

#회의 시간을 입력받아서 튜플 형태로 time 리스트에 넣는다 
for i in range(n):
  start,end=map(int,input().split())
  time.append((start,end)) 

#시작값,끝나는값을 오름차순 정렬
time=sorted(time,key=lambda a:a[0])
time=sorted(time,key=lambda a:a[1])

count=0
last=0

for i,j in time:
  if(i>=last):
    count+=1
    last=j


print(count)
