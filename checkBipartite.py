def dfs(v, c):
    visited[v] = True
    color[v] = c
    for u in l[v]:
        if not visited[u]:
            dfs(u, 1 - c)