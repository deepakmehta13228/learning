def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If the number is divisible by any integer between 2 and its square root, it's not prime

    return True  # If no divisors are found, the number is prime

# Example usage:
num = (int)(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
