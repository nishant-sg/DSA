# Dijkstra Algorithm

# pq = []
# dist = [1e9]*n
# dist[src] = 0
# pq.push([0,src])
# while pq:
#     d,n = pq.pop(0)
#     for neigh in neighbours:
#         edgeWeight,node = neigh
#         if d+edgeWeight<dist[neigh]:
#             dist[neigh] = d+edgeWeight
#             pq.push([dist[neigh],neigh])
# 
# returrn dist