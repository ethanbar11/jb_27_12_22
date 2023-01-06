amount = int(input('Please enter the amount of Fibonacci series numbers you want to create: '))

counter = 2

last = 0
current = 1
print(last)
print(current)

while counter < amount:  # as long as the amount of numbers I already created is smaller than amount the user asked to:
    new_number = current + last
    print(new_number)
    last = current
    current = new_number
    counter += 1  # counter = counter + 1

print('Finished creating the series.')
