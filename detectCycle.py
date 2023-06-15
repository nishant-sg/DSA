###### Detect Cycle UDG using DFS ######

# vis = [0]*n
# def dfs(n,p):
#     vis[n] = 1
#     for neighbour in neighbours:
#         if not vis[neighbour]:
#             if dfs(neighbour,node):
#                 return True
#         elif(neighbour != p):
#             return True
#     return False


###### Detect Cycle UDG using BFS ######

# visited = [0]*n
# q = [[source,-1]]
# visited[source] = 1
# while q:
#     n,p = q.pop(0)
#     for neighbour in neighbours:
#         if not visited[neighbour]:
#             visited[neighbour] = 1
#             q.push(neighbour,n)
#         elif p!=neighbour:
#             return True
# return False


###### Detect Cycle DG using DFS ######
# maintain visited and pathvisited array

# vis = [0]*n
# pathvisited = [0]*n
# def dfs(n):
#     vis[n] = 1
#     pathvisited[n] = 1
#     for neigh in neighbours:
#         if pathvisited[neigh] :
#             return True
#         elif vis[neigh] == 0:
#             if dfs(neigh)==True:
#                 return True

#     pathvisited[n] = 0
#     return False


