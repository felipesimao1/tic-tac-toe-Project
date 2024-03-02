def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    primes = [x for x in range(2, n) if is_prime(x)]
    return primes

def main():
    n = 100  # Define o limite superior para encontrar números primos
    primes = generate_primes(n)
    print("Prime numbers up to", n, ":")
    print(primes)

if __name__ == "__main__":
    main()
