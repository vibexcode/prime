# Square-Symmetric Primes Conjecture

## Heuristic Motivation

### Why the form p + q = 2n²?

This conjecture is not based on an arbitrary numerical pattern, but on heuristic considerations arising from the interaction between prime distribution and quadratic growth.

The quantity **2n²** defines a symmetric quadratic curve centered on even integers with regular modular behavior. Unlike linear centers (as in classical Goldbach-type problems), quadratic centers grow sufficiently fast to provide an expanding search space for admissible prime pairs, while remaining sparse enough to avoid trivial saturation. This balance makes **2n²** a natural candidate for studying prime symmetry.

From a probabilistic number-theoretic perspective, the **Bateman–Horn heuristic** suggests that polynomial expressions of the form

    q(n) = 2n² − p

should attain prime values with asymptotic density proportional to

    ~ 1 / log(2n²),

provided that no local congruence obstructions systematically eliminate candidates. For odd primes p, the expression 2n² − p avoids trivial modular exclusions, making the existence of admissible n values heuristically plausible.

The conjecture can thus be interpreted as a *quadratic prime-pair symmetry*: for a fixed odd prime p, the sequence of values 2n² − p sweeps through odd integers with increasing density, while primality acts as a sparse but non-negligible filter. Empirically, the observed fact that relatively small values of n suffice suggests that the expected waiting time for a prime hit grows slowly compared to the quadratic scale.

Finally, the form 2n² exhibits notable modular regularities. In particular, when n ≡ 0 (mod 3), one has

    2n² ≡ 0 (mod 18),

which aligns with the observed clustering of minimal solutions around multiples of 3. This suggests that the phenomenon may reflect structural compatibility between modular constraints on primes, rather than random coincidence.

These considerations do not constitute a proof, but they provide a heuristic framework explaining why the conjecture is plausible and why counterexamples may be rare or nonexistent within large computational ranges.


## **For every odd prime p ≥ 3, there exists at least one positive integer n such that (2n² - p) is also prime.**

In other words, primes p and q = 2n² - p are symmetric around the square n².

## Numerical Evidence

| Primes Tested | Maximum p   | Counterexamples | Max n |
|---------------|-------------|-----------------|-------|
| 1,000         | 7,919       | 0               |  90   |
| 10,000        | 104,743     | 0               |  279  |
| 100,000       | 1,299,721   | 0               |  915  |
| 1,000,000     | 15,485,863  | 0               | 2,925 |

## Key Findings

### 1. Growth of Symmetry Index

The smallest n for each prime p is called the **symmetry index s(p)**.

Observed relationship:

| Max p      | √(Max p) | Max s(p) | Ratio s(p)/√p |
|------------|----------|----------|---------------|
| 7,919      | 89       | 90       | 1.01          |
| 104,743    | 324      | 279      | 0.86          |
| 1,299,721  | 1,140    | 915      | 0.80          |
| 15,485,863 | 3,935    | 2,925    | 0.74          |

**Conclusion:** s(p) appears to grow as O(√p)

### 2. Divisibility Pattern

Among the first 1,000 primes:

| Condition            | Count | Percentage |
|----------------------|-------|------------|
| n divisible by 3     | 681   | **68.1%**  |
| n not divisible by 3 | 319   | 31.9%      |
  
Expected by random chance: 33.3%

This suggests the formula 2n² - p favors producing primes when n ≡ 0 (mod 3).

### Note on Statistical Significance

If the minimal values of n were uniformly distributed modulo 3, one would expect approximately **33.3%** of them to satisfy  
n ≡ 0 (mod 3).

However, in the observed data, approximately **68.1%** of the minimal n values fall into this class, representing a deviation of more than **2×** the expected frequency. While no formal hypothesis test is performed here, the magnitude of this deviation strongly suggests a structural bias rather than random fluctuation.

This observation motivates further theoretical investigation into modular constraints induced by the quadratic form 2n².

## Relation to Goldbach

This conjecture is equivalent to asking:

> "Can every number of the form 2n² be written as the sum of two odd primes?"

This is a special case of Goldbach's Conjecture restricted to numbers of the form 2n².

## Usage
### Option 1: Run directly
```bash
python prime_symmetry_test.py
```

To test with different number of primes:
```bash
python
from prime_symmetry_test import test_conjecture, analyze_divisibility

n_values, failed = test_conjecture(10000)  # Test first 10,000 primes
analyze_divisibility(n_values)
```
---
## Open Questions
  Can this conjecture be proven?
  Is s(p) < C√p for some constant C? 
  Why do 68% of s(p) values divide by 3?
  Does a similar result hold for 2nᵏ where k > 2?

---
*Research by **Uğur Kandemiş** (Vibe-X Protocol)*
