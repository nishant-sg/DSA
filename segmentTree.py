

def updateRange(start,end,ustart,uend,treeIndex,update):
    # print(treeIndex)
    if lazy[treeIndex]!=0:
        tree[treeIndex] = (end-start+1) * lazy[treeIndex]
        if start!=end:
            lazy[2*treeIndex+1] += lazy[treeIndex]
            lazy[2*treeIndex+2] += lazy[treeIndex]
        lazy[treeIndex] = 0
    if ustart>end or uend<start:
        return 
    if ustart<=start and uend>=end:
        tree[treeIndex] += (end-start+1) * update
        if start!=end:
            tree[2*treeIndex+1] += update
            tree[2*treeIndex+2] += update
        return

    mid = (start+end) //2
    updateRange(start,mid,ustart,uend,(treeIndex*2) +1,update)
    updateRange(mid+1,end,ustart,uend,(treeIndex*2) +2,update)
    # 
    tree[treeIndex] = tree[2*treeIndex+1] +tree[2*treeIndex+2]


def getquery(start,end,qstart,qend,treeIndex):
    if lazy[treeIndex]!=0:
        tree[treeIndex] = (end-start+1) * lazy[treeIndex]
        if start!=end:
            lazy[2*treeIndex+1] += lazy[treeIndex]
            lazy[2*treeIndex+2] += lazy[treeIndex]
        lazy[treeIndex] = 0

    if qstart>end or qend<start:
        return 0
    
    if qstart<=start and qend>=end:
        return tree[treeIndex]

    mid = (start+end) //2
    # 
    return (getquery(start,mid,qstart,qend,(2*treeIndex)+1)+getquery(mid+1,end,qstart,qend,(2*treeIndex)+2))

def constructTree(arr,start,end,treeIndex):
    print(start,treeIndex,end)
    if start>end:
        return 
    if start == end:
        tree[treeIndex] = arr[start]
        return
    else:
        mid = (start+end) //2
        constructTree(arr,start,mid,2*treeIndex+1)
        constructTree(arr,mid+1,end,2*treeIndex+2)
        # 
        tree[treeIndex] = tree[2*treeIndex+1]+tree[2*treeIndex+2]

arr = [1, 3, 5, 7, 9, 11]
n = len(arr)
tree = [0]*100
lazy = [0]*100
constructTree(arr,0,n-1,0)
print(tree)
print(getquery(0,n-1,1,4,0))
updateRange(0,n-1,1,4,0,5)
print(getquery(0,n-1,1,4,0))
updateRange(0,n-1,1,4,0,-5)
print(getquery(0,n-1,3,5,0))
print(getquery(0,n-1,0,2,0))