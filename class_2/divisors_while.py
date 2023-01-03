x = 23000

# with a While loop

i = 1
lst = []
while i <= x:
    if x % i == 0:
        lst.append(i)
    i = i + 1
print(lst)
print('The total amount of divisors is', len(lst))
print('This is all the divisors of', x)

# with a For loop
