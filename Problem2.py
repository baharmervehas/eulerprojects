x = 1
temp = 0
y = 0
sum = 0
while temp < 4000000:
    y = x + temp
    x = temp
    temp = y
    if y > 4000000:
        break
    else:
        if y%2 == 0:
            sum += y

print(sum)


'''
for i in range(11):
    y = x + temp
    x = temp
    temp = y
    #print(y)
    if y%2==0:
        sum += y
print(sum)
'''
