with open('p13_50digitnumbers.txt', 'r') as f:
    contents = f.read()
numbers = contents.split('\n')
S = sum(int(numbers[i]) for i in range(0, len(numbers) - 1))
print(str(S)[:10])
