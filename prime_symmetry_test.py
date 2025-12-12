"""
Square-Symmetric Primes Conjecture
==================================
For every odd prime p >= 3, there exists at least one positive integer n
such that (2n² - p) is also prime.

Author: vibexcode
Date: June 2025
Repository: https://github.com/vibexcode/prime
"""

def is_prime(n):
    """Check if a number is prime"""
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

def find_symmetric_prime(p, max_n=500000):
    """Find the smallest n where 2n² - p is also prime"""
    for n in range(2, max_n):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q
    return None, None

def test_conjecture(num_primes=1000):
    """Test the conjecture for a given number of primes"""
    print(f"Testing first {num_primes} odd primes...")
    
    # Generate primes
    primes = []
    num = 3
    while len(primes) < num_primes:
        if is_prime(num):
            primes.append(num)
        num += 2
    
    print(f"Range: {primes[0]} - {primes[-1]}")
    print("-" * 50)
    
    failed = []
    max_n_found = 0
    max_n_prime = 0
    n_values = []
    
    for i, p in enumerate(primes):
        if num_primes >= 10 and i % (num_primes // 10) == 0:
            print(f"Progress: {i}/{num_primes}")
        
        n, q = find_symmetric_prime(p)
        if n is None:
            failed.append(p)
        else:
            n_values.append(n)
            if n > max_n_found:
                max_n_found = n
                max_n_prime = p
    
    # Results
    print("-" * 50)
    print(f"Primes tested: {len(primes)}")
    print(f"Failed: {len(failed)}")
    print(f"Maximum n: {max_n_found} (for p = {max_n_prime})")
    
    if not failed:
        print("✓ Found at least one n for all primes!")
    else:
        print(f"Failed primes: {failed[:10]}...")
    
    return n_values, failed

def analyze_divisibility(n_values):
    """Analyze divisibility of n values by 3"""
    div_by_3 = sum(1 for n in n_values if n % 3 == 0)
    total = len(n_values)
    
    print(f"\nDivisibility by 3 Analysis:")
    print(f"Divisible by 3: {div_by_3} ({100*div_by_3/total:.1f}%)")
    print(f"Not divisible by 3: {total - div_by_3} ({100*(total-div_by_3)/total:.1f}%)")

if __name__ == "__main__":
    n_values, failed = test_conjecture(1000)
    analyze_divisibility(n_values)
