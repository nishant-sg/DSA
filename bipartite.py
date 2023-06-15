###### Bipartite using BFS ######

# color = [-1]*n
# q = [source]
# color[source] = 0
# while q:
#     n = q.pop(0)
#     for neighbour in neighbours:
#         if color[neighbour] == -1:
#             color[neighbour] = !color[n]
#             q.push(neighbour)
#         elif color[neighbour] == color[n]:
#             return False
# return True


###### Bipartite using DFS ######

# def dfs(node,col):
#     color[node] = col
#     for neigh in neighbours:
#         if color[neigh] ==-1:
#             if dfs(neigh,!col) ==False:
#                    return False
#         elif color[neigh]==col:
#             return False
#     return True

