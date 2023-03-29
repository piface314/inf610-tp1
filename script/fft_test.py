from random import randint
from sys import argv


k = int(argv[1])
out = argv[2]

def choose_freqs(n):
    if n <= 2:
        return [0]
    f = min(10, max(1, n//4))
    return sorted([randint(1, n//2 - 1) for _ in range(f)])

def freq_line(n):
    fs = choose_freqs(n)
    return f"{len(fs)} {' '.join(map(str, fs))}"

with open(out, "w") as f:
    ns = (int(2 ** i) for i in range(k))
    lines = [f"{n} {freq_line(n)}\n" for n in ns]
    f.writelines(lines)