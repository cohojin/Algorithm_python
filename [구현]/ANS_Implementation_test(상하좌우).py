space= int (input()) # 공간의 크기

x,y =1,1

moves=input().split() #몇번을 이동할 것인지 나타낸다.


dx=[0,0,-1,1]   # R,L,U,D를 좌표값으로 나타낸것 
dy=[1,-1,0,0]
plans=["R","L","U","D"]

#moves에 첫번째 요소에 접근 
for move in moves:
    for i in range(len(plans)):
        if (move==plans[i]):
            nx= x+dx[i]
            ny= y+dy[i]
    if nx<1 or ny<1 or nx> space or ny> space:
        continue
    x,y=nx,ny

print(x,y)

        
        
            
            
        
    
    



