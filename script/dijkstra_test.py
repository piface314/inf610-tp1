from random import randint, triangular, choice
from sys import argv


n_0 = int(argv[1])
n_f = int(argv[2])
step = int(argv[3])
out = argv[4]

def w():
    return int(triangular(0, 100, 10))

def graph(n):
    adj = [[] for _ in range(n)]
    e = set()
    c = 2
    def vchoice(u):
        return choice([i for i in range(n) if i != u and tuple(sorted((u,i))) not in e])
    for u in range(n):
        for _ in range(c):
            v = vchoice(u)
            e.add(tuple(sorted((u,v))))
            adj[u].append((v, w()))
    return adj

def graph_str(adj):
    v = len(adj)
    e = sum(map(len, adj))
    lines = [
        f"{v} {e} {randint(0, v-1)}\n",
        *[f"{i} {j} {w}\n" for i, adj_i in enumerate(adj) for j, w in sorted(adj_i)]
    ]
    return ''.join(lines)

with open(out, "w") as f:
    lines = [graph_str(graph(n)) for n in range(n_0, n_f, step) if n >= 10]
    f.writelines(lines)