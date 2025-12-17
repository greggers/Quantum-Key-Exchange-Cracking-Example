import random
from sympy import isprime

# Generate a random prime number
def generate_prime(bitsize):
    while True:
        num = random.getrandbits(bitsize)
        if isprime(num):
            return num

# Generate RSA keys
def generate_rsa_keys(bitsize=8):
    p = generate_prime(bitsize)
    q = generate_prime(bitsize)
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Find e (public exponent), must be coprime with phi_n
    e = 3
    while gcd(e, phi_n) != 1:
        e += 2
    
    # Calculate d (private exponent)
    d = modinv(e, phi_n)
    
    return (e, n), (d, n)

# Helper function to compute greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean algorithm to find modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA encryption function
def encrypt_rsa(plaintext, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

# RSA decryption function
def decrypt_rsa(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

if __name__ == "__main__":
    # Example usage
    public_key, private_key = generate_rsa_keys()
    plaintext = "hello"
    ciphertext = encrypt_rsa(plaintext, public_key)
    decrypted_message = decrypt_rsa(ciphertext, private_key)

    print("Public Key:", public_key)
    print("Private Key:", private_key)
    print("Plaintext:", plaintext)
    print("Encrypted:", ciphertext)
    print("Decrypted:", decrypted_message)
