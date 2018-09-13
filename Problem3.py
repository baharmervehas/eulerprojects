x = 0
i = 2
number = 600851475143

while  i * i < number:
    while number % i == 0:
        number = number / i
    i += 1

print(number)
