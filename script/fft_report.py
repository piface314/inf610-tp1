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
        freqs = list(map(int, f.readline().strip().split(" ")))
        freqd = [complex(*map(float, z.split())) for z in re.findall(r"\((.*? .*?)\)", f.readline())]
        instances.append((n, freqs, freqd, op))

os.makedirs(argv[2], exist_ok=True)

def time_plot(instances):
    x = [t[0] for t in instances]
    y = [t[3] for t in instances]
    plt.figure(figsize=(12,5), dpi=300)
    plt.tight_layout()
    plt.plot(x, y, "bo-")
    plt.xlabel("Tamanho da entrada, $n$")
    plt.ylabel("Qt. de operações, $T(n)$")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], "time.png"))
    plt.close()

def signal(x, f, a = 1, b = 0):
    return a * np.sin(2 * np.pi * f * x + b)

def signal_plot(idx, label, x, y, s_x, s_y):
    plt.figure(figsize=(12,5), dpi=300)
    plt.tight_layout()
    plt.plot(x, y, "b-")
    plt.plot(s_x, s_y, "bo")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], f"signal-{idx}-{label}.png"))
    plt.close()

def freq_domain_plot(idx, zs):
    zs = zs[:len(zs)//2]
    x = np.arange(len(zs))
    plt.figure(figsize=(12,5), dpi=300)
    plt.tight_layout()
    plt.bar(x, [abs(z) for z in zs])
    plt.xticks(x, x)
    plt.xlabel("Frequência (Hz)")
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join(argv[2], f"freqd-{idx}.png"))
    plt.close()

def instance_details_plot(idx, n, fs, zs):
    x = np.linspace(0, 1, 1000)
    s_x = np.linspace(0, 1, n)
    input_signals = [(signal(x, f), signal(s_x, f)) for f in fs]
    final_y = sum([y for y, _ in input_signals])
    final_s_y = sum([y for _, y in input_signals])
    # for i, (y, s_y) in enumerate(input_signals):
    #     signal_plot(idx, i, x, y, s_x, s_y)
    # signal_plot(idx, "result", x, final_y, s_x, final_s_y)
    freq_domain_plot(idx, zs)

time_plot(instances)
for idx, (n, f, z, _) in enumerate(instances):
    instance_details_plot(idx, n, f, z)