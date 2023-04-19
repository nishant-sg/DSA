####  Kruskal's
# Always add the smallest of all edges using min heap
# Check for cycle for each edge, there should not be a cycle,
# if there is a cycle then dont add that edge
# best case n-1 edges
# worst case e edges

## union find for cycle detection
# Maitain a parent array
# Inintially all nodes are parent of them selves
# then pick an edge, if both the nodes are of same parent then, the edge is unsafe to add
# else add the edge and make the nodes parent common
# therefore edges should not be added connected components



## Prims Algo
# always pick the smallest edge of all the explored edges
## O(N^2)