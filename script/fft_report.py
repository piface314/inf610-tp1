from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import os
import re

instances = []
with open(argv[1]) as f:
    while True:
        header = f.readline()
        if not header:
            break
        n, op = map(int, header.split(" "))
        sds = map(float, f.readline().strip().split(" "))
        sds = list(zip(sds, sds, sds))
        freqd = [complex(*map(float, z.split())) for z in re.findall(r"\((.*? .*?)\)", f.readline())]
        instances.append((n, sds, freqd, op))

os.makedirs(argv[2], exist_ok=True)

def n2logn(n):
    return n * np.log2(n)

def time_plot(instances):
    x = [t[0] for t in instances]
    y = [t[3] for t in instances]
    r_x = np.linspace(min(x), max(x), 1000)
    r_y = n2logn(r_x)
    r_y2 = n2logn(r_x)/2
    fig = plt.figure(figsize=(10,6), dpi=300)
    ax = fig.add_subplot(111)
    plt.tight_layout()
    lines = [plt.plot(x, y, "bo-")[0], plt.plot(r_x, r_y, "r-")[0], plt.plot(r_x, r_y2, "g-")[0]]
    for xi, yi in zip(x[6:], y[6:]):
        ax.text(xi-10, yi+100, f"$T({xi}) = {yi}$", ha="right")
    plt.xlabel("Tamanho da entrada, $n$")
    plt.ylabel("Qt. de operações, $T(n)$")
    plt.legend(lines, ["$T(n)$ medido", "$n\\log(n)$", "$T(n) = (n/2)\\log(n)$"])
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], "fft-time.png"), bbox_inches='tight', pad_inches = 0.1)
    plt.close()

def signal(x, f, a, b):
    return a * np.sin(2 * np.pi * f * x + b)

def signal_plot(idx, label, x, y, s_x, s_y):
    plt.figure(figsize=(10,3), dpi=300)
    plt.plot(x, y, "k-")
    plt.plot(s_x, s_y, "ko")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Sinal $x(t)$")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], f"signal-{idx}-{label}.png"), bbox_inches='tight', pad_inches = 0.1)
    plt.close()

def freq_domain_plot(idx, zs):
    zs = zs[:len(zs)//2]
    x = np.arange(len(zs))
    plt.figure(figsize=(10,3), dpi=300)
    plt.bar(x, [abs(z) for z in zs])
    plt.xticks(x, x)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("$|y|$")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], f"freqd-{idx}.png"), bbox_inches='tight', pad_inches = 0.1)
    plt.close()

colors = ["r", "g", "b"]
def instance_details_plot(idx, n, sds, zs):
    x = np.linspace(0, 1, 1000)
    s_x = np.linspace(0, 1, n)
    input_signals = [(signal(x, f, a, b), signal(s_x, f, a, b)) for f, a, b in sds]
    legend = [f"$f={f}, A={a}, \\varphi={b}$" for f, a, b in sds]
    final_y = sum([y for y, _ in input_signals])
    final_s_y = sum([y for _, y in input_signals])

    plt.figure(figsize=(10,3), dpi=300)
    lines = []
    for i, (y, s_y) in enumerate(input_signals):
        c = colors[i%len(colors)]
        lines.append(plt.plot(x, y, color=c)[0])
        plt.plot(s_x, s_y, color=c, marker="o", linestyle="")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Sinal $x(t)$")
    plt.legend(lines, legend)
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], f"signal-{idx}-input.png"), bbox_inches='tight', pad_inches = 0.1)
    plt.close()
    
    signal_plot(idx, "result", x, final_y, s_x, final_s_y)
    freq_domain_plot(idx, zs)

time_plot(instances)

if len(argv) > 3:
    for idx, (n, sds, z, _) in enumerate(instances):
        instance_details_plot(idx, n, sds, z)