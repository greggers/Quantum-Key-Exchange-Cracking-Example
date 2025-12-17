import rsa_encryption
import math

# Classical method to find the greatest common divisor (gcd)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Classical factorization (find factors of n)
def classical_factorization(n):
    # Try different possible divisors up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1  # if no factors are found, return n itself

# Example usage of Shor's algorithm (simulated classically)
def break_rsa_using_shors_algorithm(n):
    # Step 1: Find factors of n using a classical method (for demonstration)
    p, q = classical_factorization(n)
    return p, q

if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = rsa_encryption.generate_rsa_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Example public key (n = p * q) from earlier
    n = public_key[1]
    p, q = break_rsa_using_shors_algorithm(n)

    print(f"Found factors: p = {p}, q = {q}")

    # Compute φ(n)
    phi_n = (p - 1) * (q - 1)

    # Step 2: Compute the private key (d) using the modular inverse
    e = public_key[0]  # e from public key
    d = rsa_encryption.modinv(e, phi_n)

    print(f"Private key: d = {d}")
