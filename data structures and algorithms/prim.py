import heapq
"""
edges are in (weight, source, destination)
nodes are indicated with numbers not letters
"""
def prim(edges, n):
    adj = {}
    visited = set()
    MST = []

    for i in range(1, n+1):
        adj[i] = []
    
    for w,s,d in edges:
        adj[s].append([w,s,d])
        adj[d].append([w,d,s])

    minHeap = [[w,s,d] for (w,s,d) in adj[1]]
    
    visited.add(1)
    while len(visited) < n: 
        if minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
        if n2 in visited:
            continue
        MST.append([n1,n2])
        visited.add(n2)
        for w,s,d in adj[n2]:
            if d not in visited:
                heapq.heappush(minHeap, [w,s,d])
    
    return MST




