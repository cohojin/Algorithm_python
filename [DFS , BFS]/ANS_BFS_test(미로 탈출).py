from collections import deque

graph=[]

n,m=map(int,input().split()) #n 세로 m 가로  

#처음과 끝은 무조건 1이다.
for i in range(n):
  graph.append(list(map(int,input())))
 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  #queue 구현을 위해 deque 라이브러리를 사용
  queue=deque()
  queue.append((x,y))
  #큐가 빌 때까지 반복
  while queue:
    x,y=queue.popleft()
    #현재 위치에서 네 방향으로 위치 확인 
    for i in range(4):
      nx= x+dx[i]
      ny= y+dy[i]
      # 위치를 벗어날 경우 무시 
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      # 벽인 경우 무시 
      if graph[nx][ny] == 0:
        continue
      # 처음 방문하는 경우에만 최단 거리 기록 
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
  return graph[n-1][m-1]

print(bfs(0,0))
