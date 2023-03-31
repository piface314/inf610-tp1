from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import os


instances = []
with open(argv[1]) as f:
    while True:
        header = f.readline()
        if not header:
            break
        n, e, op = map(int, header.split(" "))
        f.readline()
        f.readline()
        instances.append((n, op))

os.makedirs(argv[2], exist_ok=True)

def n2(x, a, b, c):
    return a * x * x + b * x + c

def time_plot(instances):
    x = [t[0] for t in instances]
    y = [t[1] for t in instances]
    r_x = np.linspace(min(x), max(x), 1000)
    r_y2 = n2(r_x, 2, 0, 0)
    r_y1 = n2(r_x, 1, 0, 0)
    fig = plt.figure(figsize=(10,4), dpi=300)
    ax = fig.add_subplot(111)
    plt.tight_layout()
    lines = [plt.plot(x, y, "bo-")[0], plt.plot(r_x, r_y2, "r-")[0], plt.plot(r_x, r_y1, "g-")[0]]
    for xi, yi in zip(x[6:], y[6:]):
        ax.text(xi-10, yi+100, f"$T({xi}) = {yi}$", ha="right")
    plt.xlabel("Tamanho da entrada, $n$")
    plt.ylabel("Qt. de operações, $T(n)$")
    plt.legend(lines, ["$T(n)$ medido", "$c_2 n^2$", "$c_1 n^2$"])
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], "dijkstra-time.png"), bbox_inches='tight', pad_inches = 0.1)
    plt.close()

time_plot(instances)