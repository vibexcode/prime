"""
Kare-Simetrik Asallar Konjektürü
================================
Her tek asal p >= 3 için, en az bir n vardır ki (2n² - p) de asaldır.

Yazar: [Senin adın]
Tarih: Haziran 2025
"""

def is_prime(n):
    """Sayının asal olup olmadığını kontrol eder"""
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
    """p asalı için 2n² - p'nin asal olduğu en küçük n'yi bulur"""
    for n in range(2, max_n):
        q = 2 * n * n - p
        if q > 1 and is_prime(q):
            return n, q
    return None, None

def test_conjecture(num_primes=1000):
    """Konjektürü belirtilen sayıda asal için test eder"""
    print(f"İlk {num_primes} tek asal için test başlıyor...")
    
    # Asalları oluştur
    primes = []
    num = 3
    while len(primes) < num_primes:
        if is_prime(num):
            primes.append(num)
        num += 2
    
    print(f"Aralık: {primes[0]} - {primes[-1]}")
    print("-" * 50)
    
    failed = []
    max_n_found = 0
    max_n_prime = 0
    n_values = []
    
    for i, p in enumerate(primes):
        if i % (num_primes // 10) == 0:
            print(f"İlerleme: {i}/{num_primes}")
        
        n, q = find_symmetric_prime(p)
        if n is None:
            failed.append(p)
        else:
            n_values.append(n)
            if n > max_n_found:
                max_n_found = n
                max_n_prime = p
    
    # Sonuçlar
    print("-" * 50)
    print(f"Test edilen asal sayısı: {len(primes)}")
    print(f"Başarısız: {len(failed)}")
    print(f"En büyük n: {max_n_found} (p = {max_n_prime} için)")
    
    if not failed:
        print("✓ Tüm asallar için en az bir n bulundu!")
    
    return n_values, failed

def analyze_divisibility(n_values):
    """n değerlerinin 3'e bölünebilirlik analizini yapar"""
    div_by_3 = sum(1 for n in n_values if n % 3 == 0)
    total = len(n_values)
    
    print(f"\n3'e Bölünebilirlik Analizi:")
    print(f"3'e bölünen: {div_by_3} (%{100*div_by_3/total:.1f})")
    print(f"3'e bölünmeyen: {total - div_by_3} (%{100*(total-div_by_3)/total:.1f})")

if __name__ == "__main__":
    n_values, failed = test_conjecture(1000)
    analyze_divisibility(n_values)
