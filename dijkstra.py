def initialize_single_source(g,s):
    n = len(g)
    d = [None] * n
    pai = [None] * n
    for v in range(n):
        d[v] = 10000
        pai[v] = None
    d[s] = 0
    return d, pai

def extract_min(q, s):
    n = len(q)
    min = None
    for v in range(n):
        if not s[v]:
            if min == None:
                min = v
            elif q[v] < q[min]:
                min = v
    return min
                

def dijkstra(g, f):
    d,pai = initialize_single_source(g,f)
    n = len(g)
    s = [False] * n
    q = d
    for i in range(n):
        u = extract_min(q,s)
        s[u] = True
        for w,v in g[u]:
            if d[v] > d[u] + w:
                d[v] = d[u]+w
                pai[v] = u
                # Implicito decrease-key
    return d,pai

g = [
    [(10,1),(5,3)],
    [(1,2),(2,3)],
    [(4,4)],
    [(3,1),(9,2),(2,4)],
    [(7,0),(6,2)]
]

d, pai = dijkstra(g,0)

print ("d =", d)
print ("pai =", pai)
