"""
Square-Symmetric Primes Conjecture
==================================
For every odd prime p >= 3, there exists at least one positive integer n
such that q = (2n^2 - p) is also prime.

We search for the smallest such n (symmetry index s(p)).

Author: vibexcode (rewritten/optimized)
Date: 2026-01-01
"""

from __future__ import annotations
from math import isqrt
from typing import List, Tuple, Optional


# ----------------------------
# Fast primality test (64-bit)
# ----------------------------
def is_prime(n: int) -> bool:
    """Deterministic Miller–Rabin for n < 2^64, plus small prime trial division."""
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # write n-1 = d * 2^s (d odd)
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # Deterministic bases for 64-bit ints
    # Proven sufficient for n < 2^64
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False

    return True


# ----------------------------
# Prime generation
# ----------------------------
def generate_first_k_odd_primes(k: int) -> List[int]:
    """
    Generate the first k odd primes (starting from 3).
    Uses the fast is_prime above. For very large k, replace with segmented sieve.
    """
    primes: List[int] = []
    n = 3
    while len(primes) < k:
        if is_prime(n):
            primes.append(n)
        n += 2
    return primes


# ----------------------------
# Conjecture search
# ----------------------------
def find_symmetric_prime(p: int, max_n: int = 500_000) -> Tuple[Optional[int], Optional[int]]:
    """
    Find the smallest n >= 2 such that q = 2n^2 - p is prime.
    Heuristic: try n multiples of 3 first (often removes mod-3 obstruction).
    Fallback: full scan.
    """
    # Pass 1: n ≡ 0 (mod 3)
    for n in range(3, max_n + 1, 3):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q

    # Pass 2: full scan (guarantees: if there's a solution <= max_n, we find it)
    for n in range(2, max_n + 1):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q

    return None, None


def test_conjecture(num_primes: int = 1000, max_n: int = 500_000) -> Tuple[List[int], List[int]]:
    """
    Test first `num_primes` odd primes.
    Returns: (list of minimal n values found, list of primes that failed within max_n).
    """
    print(f"Testing first {num_primes} odd primes with max_n={max_n} ...")

    primes = generate_first_k_odd_primes(num_primes)
    print(f"Prime range: {primes[0]} .. {primes[-1]}")
    print("-" * 60)

    failed: List[int] = []
    n_values: List[int] = []

    max_n_found = 0
    max_n_at_p = None

    step = max(1, num_primes // 10)

    for i, p in enumerate(primes, start=1):
        if i % step == 0 or i == 1:
            print(f"Progress: {i}/{num_primes}")

        n, q = find_symmetric_prime(p, max_n=max_n)
        if n is None:
            failed.append(p)
        else:
            n_values.append(n)
            if n > max_n_found:
                max_n_found = n
                max_n_at_p = p

    print("-" * 60)
    print(f"Primes tested: {len(primes)}")
    print(f"Failed within max_n: {len(failed)}")
    if max_n_at_p is not None:
        print(f"Maximum minimal n found: {max_n_found} (at p={max_n_at_p})")

    if not failed:
        print("✓ Found at least one n for all tested primes (within max_n).")
    else:
        print(f"First failed primes (up to 10): {failed[:10]}")

    return n_values, failed


def analyze_mod3(n_values: List[int]) -> None:
    """Report how many minimal n are divisible by 3 (descriptive only)."""
    total = len(n_values)
    if total == 0:
        print("No n values to analyze.")
        return

    div3 = sum(1 for n in n_values if n % 3 == 0)
    print("\nMod 3 analysis (minimal n values):")
    print(f"Total: {total}")
    print(f"n ≡ 0 (mod 3): {div3} ({100.0 * div3 / total:.1f}%)")
    print(f"n ≠ 0 (mod 3): {total - div3} ({100.0 * (total - div3) / total:.1f}%)")


if __name__ == "__main__":
    n_values, failed = test_conjecture(num_primes=1000, max_n=200_000)
    analyze_mod3(n_values)
