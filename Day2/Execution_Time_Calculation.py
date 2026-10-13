
import random
import time

# Generate random numbers
def generate_random_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 100))
    return numbers


# Check whether a number is prime
def prime_check(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Method 1: Check every number for primality
def remove_primes(numbers):
    result = []

    for num in numbers:
        if not prime_check(num):
            result.append(num)

    return result


# Generate all prime numbers between 1 and 100
def generate_prime_list():
    primes = []

    for num in range(2, 101):
        if prime_check(num):
            primes.append(num)

    return primes


# Method 2: Use precomputed prime numbers
def remove_primes_optimized(numbers, prime_set):
    result = []

    for num in numbers:
        if num not in prime_set:
            result.append(num)

    return result


# Compare execution times
sizes = [100, 10000, 100000]

prime_list = generate_prime_list()
prime_set = set(prime_list)

for n in sizes:
    numbers = generate_random_numbers(n)

    # Method 1
    start = time.perf_counter()
    result1 = remove_primes(numbers)
    time1 = time.perf_counter() - start

    # Method 2
    start = time.perf_counter()
    result2 = remove_primes_optimized(numbers, prime_set)
    time2 = time.perf_counter() - start

    difference = time1 - time2

    print(f"\nList size: {n}")
    print(f"Original method: {time1:.6f} seconds")
    print(f"Optimized method: {time2:.6f} seconds")
    print(f"Time saved: {difference:.6f} seconds")

    if difference > 0:
        print("Optimization improved execution time.")
    elif difference < 0:
        print("Optimized method was slower for this run.")
    else:
        print("Both methods took approximately the same time.")
