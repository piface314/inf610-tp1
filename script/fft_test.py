from random import randint, random
from math import pi
from sys import argv


k = int(argv[1])
out = argv[2]

def choose_freqs(n):
    if n <= 2:
        return ["0 1 0.00"]
    f = min(10, max(1, n//4 - 1))
    return [f"{randint(1, n//2 - 1)} {randint(1, 5)} {random() * pi:.2f}" for _ in range(f)]

def freq_line(n):
    fs = choose_freqs(n)
    return f"{len(fs)} {' '.join(fs)}"

with open(out, "w") as f:
    ns = (int(2 ** i) for i in range(k))
    lines = [f"{n} {freq_line(n)}\n" for n in ns]
    f.writelines(lines)