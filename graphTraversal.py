##########DFS##############

# def dfs(graph,cur):
#     visited[cur] = True
#     for all neighbours v of cur in graph:
#         if visited[v] is False:
#             dfs(graph,v)
#     return
#
# O(|V|+|E|)



##########BFS#################

# def bfs(graph,source):
#     q.enqueue(source)
#     visited[source] = True
#     while q is not empty:
#         cur = q.front()
#         q.dequeue()
#         for all neightbours v of cur in graph:
#             if visted[v] is false:
#                 q.enqueue(v)
#                 visited[v] = True
#     return 
#
# O(|V|+|E|)