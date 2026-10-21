print([x for x in range(0,31) if x % 3 ])

numbers = []
n = -1
while n <= 29:
    n += 1
    if not n % 3:
        continue
    numbers.append(n)
print(numbers)
