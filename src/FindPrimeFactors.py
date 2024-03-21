def prime_factors(number):
    factors = []
    # Remove factors of 2 first
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    # Now n must be odd. Starting from 3, check odd factors up to sqrt(n)
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.append(i)
            number //= i
    # If n is a prime greater than 2
    if number > 2:
        factors.append(number)
    return factors

# Test the function:
number = 630
print("Prime factors of", number, "are:", prime_factors(number))