import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

def generate_primes(count):
    if count <= 0:
        return []
        
    primes = []
    current_number = 2

    while len(primes) < count:
        if is_prime(current_number):
            primes.append(current_number)
        
        current_number += 1
        
    return primes

if __name__ == "__main__":
    N = 15
    print(f"Generating the first {N} prime numbers:")
    
    list_of_primes = generate_primes(N)
    
    print(list_of_primes)
    
    test_numbers = [17, 25, 97, 1]
    print("\nTesting individual numbers using is_prime(n):")
    for num in test_numbers:
        print(f"Is {num} prime? {is_prime(num)}")
