n,m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))

#DFS로 특정 노드 방문 뒤 연결 노드 방문 