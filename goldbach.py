#!/usr/bin/env python3
import colorsys
import matplotlib.pyplot as plt
from collections import defaultdict

MAX_N = 250


def _sieve(limit):
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return is_prime


def _color_for(i):
    h = (i * 137.508) % 360
    return colorsys.hls_to_rgb(h / 360, 0.40, 0.75)


def _prime_pairs(n, is_prime):
    for p in range(2, n // 2 + 1):
        if is_prime[p] and is_prime[n - p]:
            yield p, n - p


def _all_pairs_by_n(even_numbers, is_prime):
    return {n: list(_prime_pairs(n, is_prime)) for n in even_numbers}


def _plot_prime_pairs():
    even_numbers = [n for n in range(4, MAX_N + 1) if n % 2 == 0]
    is_prime = _sieve(max(even_numbers))

    all_pairs_by_n = _all_pairs_by_n(even_numbers, is_prime)

    # Batch points by color index so we make one scatter call per color
    xs_by_color = defaultdict(list)
    ys_by_color = defaultdict(list)
    seg_xs = defaultdict(list)
    seg_ys = defaultdict(list)

    for n, pairs in all_pairs_by_n.items():
        for i, (p, q) in enumerate(pairs):
            xs_by_color[i].extend([n, n])
            ys_by_color[i].extend([p, q])
            seg_xs[i].extend([n, n, None])
            seg_ys[i].extend([p, q, None])

    max_pair_index = max(xs_by_color.keys(), default=0)

    fig, ax = plt.subplots(figsize=(18, 8))

    for c in range(max_pair_index + 1):
        if xs_by_color[c]:
            color = _color_for(c)
            ax.plot(seg_xs[c], seg_ys[c], color=color, linewidth=0.8, alpha=0.5, zorder=2)
            ax.scatter(xs_by_color[c], ys_by_color[c], color=color, s=30, zorder=3)

    ax.set_xlabel("Even Number (N)", fontsize=13)
    ax.set_ylabel("Prime (P or Q)  where  P + Q = N", fontsize=13)
    ax.set_title(f"Goldbach Conjecture — Prime Pairs for Even Numbers 4–{MAX_N}", fontsize=15)
    ax.set_xticks(even_numbers)
    ax.tick_params(axis="x", rotation=90, labelsize=7)
    ax.grid(axis="x", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig("goldbach.png", dpi=150)
    plt.show()
    print("Plot saved to goldbach.png")


def prime_pair_counts(max_n):
    """Return {n: count} of Goldbach prime pairs for each even n in [4, max_n]."""
    even_numbers = [n for n in range(4, max_n + 1) if n % 2 == 0]
    is_prime = _sieve(max_n)
    return {n: sum(1 for _ in _prime_pairs(n, is_prime)) for n in even_numbers}


def _plot_num_prime_pairs():
    counts_by_n = prime_pair_counts(MAX_N)
    even_numbers = list(counts_by_n.keys())
    counts = list(counts_by_n.values())

    fig, ax = plt.subplots(figsize=(18, 6))
    ax.bar(even_numbers, counts, width=1.6, color="#4363D8", edgecolor="none")

    ax.set_xlabel("Even Number (N)", fontsize=13)
    ax.set_ylabel("Number of prime pairs", fontsize=13)
    ax.set_title(f"Goldbach Conjecture — Prime Pair Counts for Even Numbers 4–{MAX_N}", fontsize=15)
    ax.set_xticks(even_numbers)
    ax.tick_params(axis="x", rotation=90, labelsize=7)
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig("goldbach_counts.png", dpi=150)
    plt.show()
    print("Plot saved to goldbach_counts.png")


if __name__ == "__main__":
    _plot_prime_pairs()
    #_plot_num_prime_pairs()
