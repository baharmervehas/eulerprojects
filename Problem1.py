a = 0

for numbers in range(1000):
    if numbers % 3 == 0 or numbers % 5 == 0:
        #print(numbers)

        a += numbers
print(a)