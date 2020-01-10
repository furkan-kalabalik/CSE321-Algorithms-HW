def check_bipartite_dfs(graph):
    visited = []
    color = []
    for i in range(len(graph)):
        visited.append(False)
    
    for i in range(len(graph)):
        color.append(2)
    
    for i in range(len(graph)):#Maybe this is directional graph
        if not visited[i]:
             dfs(i, 0,visited,color)
 
    for i in range(len(graph)):
        for j in graph[i]:
            if color[i] == color[j]:
                return False
    return True

def dfs(vertex, colored,visited,color):
    visited[vertex] = True
    color[vertex] = colored
    for u in graph[vertex]:
        if not visited[u]:
            dfs(u, 1 - colored,visited,color)
 
# Adjacency list of graph
graph = {0: [1,2], 1:[0,3],2:[0,3],3:[1,2,4],4:[3]}
print(check_bipartite_dfs(graph))

