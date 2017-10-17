for i in range(997, 100, -1):

    #creates the imaged number of i
    h = i // 100
    d = i % 100 // 10
    u = i % 10
    i_im = u * 100 + d * 10 + h

    #create the palindrome number
    n = i * 1000 + i_im  
 
    for j in range(999, 100, -1):
        if n % j == 0 and n / j >= 100 and n / j < 1000:
            print(n, j, n // j)
            break
    else:
        continue

    break
