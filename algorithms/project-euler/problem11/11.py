with open('p11_20x20.txt', 'r') as f:
    contents = f.read()
lines = contents.split('\n')
numbers = [line.split(' ') for line in lines]
max = 0
for i in range(0, 20):
    for j in range(0,20):
        product = 1
        if i + 3 < 20:
            for counter in range(i, i + 4):
                product *= int(numbers[counter][j])
            if product > max:
                max = product
        product = 1
        if j + 3 < 20:
            for counter in range(j, j + 4):
                product *= int(numbers[i][counter])
            if product > max:
                max = product
        product = 1
        if i + 3 < 20 and j + 3 < 20:
            for counter in range(i, i + 4):
                product *= int(numbers[counter][counter])
            if product > max:
                max = product
        product = 1
        if i + 3 < 20 and j - 3 >= 0:
            counter2 = j
            for counter in range(i, i + 4):
                product *= int(numbers[counter][counter2])
                counter2 -= 1
            if product > max:
                max = product
print(max)
