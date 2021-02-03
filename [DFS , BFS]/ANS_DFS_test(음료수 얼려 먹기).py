n,m = map(int,input().split()) #얼음틀

ice_shape=list()

for i in range(n):
  ice_shape.append(list(map(int,input())))

def dfs(x,y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료 
  # x,y값이 -1까지 가능한 이유는 0번인덱스의 값도 계산해주기 위해 -1까지 허용
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
  # 현재 노드를 방문하지 않았다면 
    if ice_shape[x][y] == 0:
    #해당노드 방문 처리 
        ice_shape[x][y] =1 
    #상 하 좌 우 위치도 재귀적으로 호출 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
ans=0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i,j) == True:
      ans += 1
print(ans)
