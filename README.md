## Heuristic Motivation and Square-Centered Symmetry

### Why the form p + q = 2n²?

This conjecture is not proposed as an arbitrary numerical pattern, but is motivated by heuristic considerations arising from the interaction between prime distribution and quadratic growth.

The quantity **2n²** defines a symmetric quadratic center on the number line. Unlike linear centers (as in classical Goldbach-type problems), quadratic centers grow fast enough to provide an expanding search space for admissible prime pairs, while remaining sparse enough to avoid trivial saturation. This balance makes **2n²** a natural candidate for studying structured prime symmetry.

From a probabilistic number-theoretic perspective, the **Bateman–Horn heuristic** suggests that polynomial expressions of the form

    q(n) = 2n² − p

should attain prime values with asymptotic density proportional to

    ~ 1 / log(2n²),

provided that no local congruence obstructions systematically eliminate candidates. For odd primes p, the expression 2n² − p avoids trivial modular exclusions, making the existence of admissible n values heuristically plausible.

Empirically, the fact that relatively small values of n suffice across large datasets suggests that the expected waiting time for a prime hit grows slowly compared to the quadratic scale.

---

### # Square-Symmetric Primes Conjecture

This repository investigates the following conjecture:

> **Conjecture.**  
> For every odd prime \( p \ge 3 \), there exists an integer \( n \ge 2 \) such that  
> \[
> q = 2n^2 - p
> \]
> is also prime.

Equivalently:
\[
p + q = 2n^2
\]
so the primes \(p\) and \(q\) are symmetric around the square center \(n^2\).

---

## Interpretation (Geometric Intuition)

- The square \(n^2\) acts as a **symmetry center**.
- Prime pairs \((p,q)\) appear as equal-distance deviations:
  \[
  p = n^2 - d,\quad q = n^2 + d
  \]
- The center \(n^2\) itself cannot be prime (for \(n>1\)), so primality is realized only through symmetric offsets.

This makes \(n^2\) a **binding but non-collapsing constraint**:  
it enforces balance without destroying primality.

---

## What the Code Does

The main script:

1. Generates the first \(N\) odd primes.
2. For each prime \(p\), searches for an integer \(n\) such that  
   \(q = 2n^2 - p\) is prime.
3. By default, computes the **true minimal symmetry index**
   \[
   s(p) = \min\{n \ge 2 : 2n^2 - p \text{ is prime}\}.
   \]

An optional **heuristic mode** is provided for faster scanning, but it does **not**
guarantee minimality and is clearly labeled as such.

---

## Minimal vs Fast Search Modes

- **minimal (default)**  
  Scans \(n = 2,3,4,\dots\) in increasing order.  
  Guarantees that the returned \(n\) is the smallest possible.

- **fast (heuristic)**  
  Prioritizes \(n \equiv 0 \pmod{3}\) to speed up searches.  
  Useful for large experiments, but **not guaranteed to return the minimal \(n\)**.

The conjecture itself concerns **existence**, not minimality;  
minimality is used here as a canonical, reproducible choice.

---

## Modular (Local Obstruction) Analysis

We also test whether the polynomial
\[
q(n,p) = 2n^2 - p
\]
is **locally obstructed** modulo small integers.

A complete scan for all moduli \( m \le 31 \) shows:

- No nontrivial local obstructions.
- The only obstruction occurs for \(p \equiv 0 \pmod{2}\), which is outside the
  scope of the conjecture (odd primes only).

Thus, the conjecture is **locally consistent**: it does not collapse modulo
small integers.

---

## Mod 3 Phenomenon

Empirically, many minimal symmetry indices satisfy \( n \equiv 0 \pmod{3} \).

This is **not** a local obstruction.
Instead, it reflects a **modular narrowing**:
certain residue classes of \(n\) avoid forced divisibility by 3 in
\(q = 2n^2 - p\).

In other words:
- mod 3 creates a *preferred escape route*,
- not a barrier.

---

## Status

- No counterexample found for the tested ranges.
- No small-modulus local obstruction detected.
- The conjecture remains open.

This repository provides experimental evidence and geometric intuition,
not a proof.

---

## Usage

Run the main script to test the conjecture on the first \(N\) odd primes
and analyze symmetry indices.



---
*Research by **Uğur Kandemiş** (Vibe-X Protocol)*
