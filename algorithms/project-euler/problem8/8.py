SUBSEQ_LENGTH = 13
with open('p8_1000digit.txt', 'r') as f:
    contents = f.read()
numbers = contents.replace('\n',"")
max = 0
i = 0
product = 1
while i < len(numbers) - 13:
    if product == 1:
        for j in range(i, i + SUBSEQ_LENGTH):
            if int(numbers[j]) != 0:
                product *= int(numbers[j])
            else:
                product = 1
                i = j
                while int(numbers[i]) == 0 and i < len(numbers) - 13:
                    i += 1
                break
        i += 1
    else:
        if int(numbers[i + SUBSEQ_LENGTH - 1]) != 0:
            product = product / int(numbers[i - 1])
            product *= int(numbers[i + SUBSEQ_LENGTH - 1])
            i += 1
        else:
            product = 1
            i += SUBSEQ_LENGTH
    if product > max:
        max = product
print(max)
