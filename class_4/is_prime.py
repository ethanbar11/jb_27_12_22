def is_prime(num):
    for i in range(2, num):
        print('Checking if', num, 'can be divided by', i)
        if num % i == 0:
            print('I found that', num, 'can be divided by', i)
            return False
    return True


x = int(input('Please enter a number:'))
print('The number', x, 'is prime:', is_prime(x))
