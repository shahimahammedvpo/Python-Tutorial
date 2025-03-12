def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = [num for num in range(2, 1000) if is_prime(num)]
print("Prime numbers less than 1000:", primes)
