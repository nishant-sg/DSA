# Helps to detect negative cycle where dijkstra fails
# Only works on DG
# To make DG make two edges for every edge in UDG

# dis = [1e9]*n
# for _ in range(n-1):
#     for edge in edges:
#         u,v,d = edge
#         if d[u]+d<d[v]:
#             d[v] = d[u]+d
# d1 = dis
# for edge in edges:
#     u,v,d = edge
#     if d[u]+d<d[v]:
#         d[v] = d[u]+d
# if d1==dis:
#     print("No negative Cycle")
# else:
#     print("Negative Cycle")
