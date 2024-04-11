def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(min_num, max_num):
    prime_numbers = []
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

print(find_prime_numbers(1,100))
