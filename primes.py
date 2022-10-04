"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2

    while number_of_primes:
        if isPrime(number):
            list.append(number)
            number_of_primes = number_of_primes - 1
            number = number + 1
        else:
            number = number + 1
    return list

def isPrime(number):
    if number == 2:
        return True
    else:
        for value in range(2, number):
            if (number % value) == 0:
                return False
            else:
                return True
    return False
