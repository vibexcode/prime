"""
Exploratory regression analysis of square-centered symmetric prime pairs.

This script generates visualizations for exploratory purposes only.
No claims of proof, optimality, or deterministic laws are made.
"""

import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_closest_symmetric_prime(p, max_n=1000):
    best_n = None
    best_q = None
    min_diff = float('inf')
    
    for n in range(2, max_n):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            diff = abs(p - q)
            if diff < min_diff:
                min_diff = diff
                best_n = n
                best_q = q
    
    return best_n, best_q, min_diff

# Farklı örneklem boyutları test et
sample_sizes = [200, 500, 1000, 2000, 5000]

print("Örneklem Boyutu | Eğim (slope) | Kesişim (intercept)")
print("-" * 55)

results = []

for size in sample_sizes:
    # Asalları oluştur
    primes = []
    num = 3
    while len(primes) < size:
        if is_prime(num):
            primes.append(num)
        num += 2
    
    p_values = []
    q_values = []
    
    for p in primes:
        n, q, diff = find_closest_symmetric_prime(p)
        if n:
            p_values.append(p)
            q_values.append(q)
    
    # Linear Regression
    p_arr = np.array(p_values)
    q_arr = np.array(q_values)
    slope, intercept = np.polyfit(p_arr, q_arr, 1)
    
    results.append((size, slope, intercept, p_values, q_values))
    print(f"{size:^15} | {slope:^12.4f} | {intercept:^12.2f}")

# En büyük örneklem için grafik
size, slope, intercept, p_values, q_values = results[-1]

plt.figure(figsize=(12, 8))
p_arr = np.array(p_values)
q_arr = np.array(q_values)
fit_line = slope * p_arr + intercept

plt.scatter(p_values, q_values, alpha=0.4, s=10, label='Data points')
plt.plot([0, max(p_values)], [0, max(p_values)], 'r--', linewidth=2, label='p = q')
plt.plot(p_arr, fit_line, 'b-', linewidth=2, label=f'Best fit: q = {slope:.3f}p + {intercept:.1f}')
plt.xlabel('p (prime)')
plt.ylabel('q (closest symmetric prime)')
plt.title(f'Closest Symmetric Prime Pairs (n = {size})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('large_sample_fit.png', dpi=150)
plt.show()
