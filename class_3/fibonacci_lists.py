amount = int(input('Please enter the amount of Fibonacci series numbers you want to create: '))
fib = [0, 1]

for i in range(amount - 2):
    new_number = fib[-1] + fib[-2]
    fib.append(new_number)

print(fib)
