LENGTH = 50

red = [0, 0, 1, 2, 4]
green = [0, 0, 0, 1, 2 ]
blue = [0, 0, 0, 0, 1]
for i in range(5, LENGTH + 1):
    red.append(red[i - 1] + red[i - 2] + 1)
    green.append(green[i - 1] + green[i - 3] +1)
    blue.append(blue[i - 1] + blue[i - 4] + 1)
print(red[50] + green[50] + blue[50])
