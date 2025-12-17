import time
import random
from sympy import isprime, factorint

# Generate a large random prime
def generate_large_prime(bitsize):
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num

# Measure factorization time
def measure_factorization_time(bitsize):
    p = generate_large_prime(bitsize)
    q = generate_large_prime(bitsize)
    n = p * q  # RSA modulus

    print(f"Generated RSA modulus (n = p * q) of size {bitsize * 2} bits")

    start_time = time.time()
    factors = factorint(n)  # Classical factorization
    end_time = time.time()

    print(f"Factors found: {factors}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":

    # Test with different bit sizes
    print("Factoring 16-bit RSA key...")
    measure_factorization_time(8)  # 16-bit modulus (small example)

    print("\nFactoring 32-bit RSA key...")
    measure_factorization_time(16)  # 32-bit modulus

    print("\nFactoring 64-bit RSA key (this may take some time)...")
    measure_factorization_time(32)  # 64-bit modulus

    print("\nFactoring 92-bit RSA key (this may take some time)...")
    measure_factorization_time(41)  # 92-bit modulus

    print("\nFactoring 128-bit RSA key (this will take a while)...")
    #measure_factorization_time(64)  # 128-bit modulus

    print("\nFactoring 512-bit RSA key (this will take significantly longer)...")
    # Uncomment the next line if you want to test 512-bit RSA factorization (very slow!)
    # measure_factorization_time(256)
