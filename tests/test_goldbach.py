from goldbach import prime_pair_counts


def test_prime_pair_counts_n28():
    # For N=28, the only Goldbach pairs are (5, 23) and (11, 17)
    counts = prime_pair_counts(28)
    assert counts[28] == 2


def test_prime_pair_counts_includes_all_evens():
    counts = prime_pair_counts(28)
    expected_evens = list(range(4, 29, 2))
    assert list(counts.keys()) == expected_evens


def test_prime_pair_counts_small_values():
    counts = prime_pair_counts(10)
    assert counts[4] == 1   # 2+2
    assert counts[6] == 1   # 3+3
    assert counts[8] == 1   # 3+5
    assert counts[10] == 2  # 3+7, 5+5
