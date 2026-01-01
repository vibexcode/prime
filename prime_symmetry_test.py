"""
Square-Symmetric Primes Conjecture
==================================
For every odd prime p >= 3, conjecturally there exists an integer n >= 2 such that
q = 2*n^2 - p is also prime.

We define:
- minimal symmetry index s(p): the smallest n >= 2 such that q is prime.

This script can:
- test the conjecture for the first N odd primes
- compute minimal s(p) (default, correct)
- optionally run a faster heuristic search (not guaranteed minimal)

Author: vibexcode
"""

from __future__ import annotations
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

    # Deterministic bases for 64-bit integers
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
# Prime generation (odd primes)
# ----------------------------
def generate_first_k_odd_primes(k: int) -> List[int]:
    """Generate the first k odd primes, starting from 3."""
    primes: List[int] = []
    x = 3
    while len(primes) < k:
        if is_prime(x):
            primes.append(x)
        x += 2
    return primes


# ----------------------------
# Core search (minimal vs fast)
# ----------------------------
def find_symmetric_prime_minimal(p: int, max_n: int) -> Tuple[Optional[int], Optional[int]]:
    """
    TRUE minimal search:
    scans n = 2..max_n in increasing order.
    If a solution exists with n <= max_n, returns the smallest such n.
    """
    for n in range(2, max_n + 1):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q
    return None, None


def find_symmetric_prime_fast_pref3(p: int, max_n: int) -> Tuple[Optional[int], Optional[int]]:
    """
    FAST heuristic search (NOT guaranteed minimal):
    tries n multiples of 3 first (often helps), then falls back to full scan.
    Use only when you explicitly want speed over minimality.
    """
    for n in range(3, max_n + 1, 3):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q

    for n in range(2, max_n + 1):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q

    return None, None


# ----------------------------
# Experiment runner
# ----------------------------
def test_conjecture(
    num_primes: int = 1000,
    max_n: int = 200_000,
    mode: str = "minimal",  # "minimal" (correct) or "fast" (heuristic)
) -> Tuple[List[int], List[int]]:
    """
    Tests the conjecture on the first `num_primes` odd primes.

    Returns:
      - n_values: list of n found (minimal if mode="minimal")
      - failed: primes p for which no solution was found with n <= max_n
    """
    if mode not in ("minimal", "fast"):
        raise ValueError("mode must be 'minimal' or 'fast'")

    finder = find_symmetric_prime_minimal if mode == "minimal" else find_symmetric_prime_fast_pref3

    print(f"Testing first {num_primes} odd primes with max_n={max_n} (mode={mode}) ...")

    primes = generate_first_k_odd_primes(num_primes)
    print(f"Prime range: {primes[0]} .. {primes[-1]}")
    print("-" * 60)

    failed: List[int] = []
    n_values: List[int] = []

    max_n_found = 0
    max_n_at_p: Optional[int] = None

    step = max(1, num_primes // 10)

    for i, p in enumerate(primes, start=1):
        if i == 1 or i % step == 0 or i == num_primes:
            print(f"Progress: {i}/{num_primes}")

        n, q = finder(p, max_n=max_n)
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
        label = "Maximum minimal n" if mode == "minimal" else "Maximum found n (heuristic)"
        print(f"{label}: {max_n_found} (at p={max_n_at_p})")

    if not failed:
        print("✓ Found at least one n for all tested primes (within max_n).")
    else:
        print(f"First failed primes (up to 10): {failed[:10]}")

    return n_values, failed


def analyze_mod3(n_values: List[int], label: str) -> None:
    """Report how many n values are divisible by 3."""
    total = len(n_values)
    if total == 0:
        print(f"\nMod 3 analysis ({label}): no data")
        return

    div3 = sum(1 for n in n_values if n % 3 == 0)
    print(f"\nMod 3 analysis ({label}):")
    print(f"Total: {total}")
    print(f"n ≡ 0 (mod 3): {div3} ({100.0 * div3 / total:.1f}%)")
    print(f"n ≠ 0 (mod 3): {total - div3} ({100.0 * (total - div3) / total:.1f}%)")


if __name__ == "__main__":
    # Default: correct minimal symmetry index
    n_values_min, failed_min = test_conjecture(num_primes=1000, max_n=200_000, mode="minimal")
    analyze_mod3(n_values_min, label="minimal n")

    # Optional: heuristic speed mode (NOT minimal)
    # n_values_fast, failed_fast = test_conjecture(num_primes=1000, max_n=200_000, mode="fast")
    # analyze_mod3(n_values_fast, label="fast (prefers n%3==0)")
