# Square-Symmetric Primes Conjecture

## Conjecture

> **For every odd prime p ≥ 3, there exists at least one positive integer n such that (2n² - p) is also prime.**

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

## Open Questions
  Can this conjecture be proven?
  Is s(p) < C√p for some constant C?
  Why do 68% of s(p) values divide by 3?
  Does a similar result hold for 2nᵏ where k > 2?

---
*Research by **Uğur Kandemiş** (Vibe-X Protocol)*
