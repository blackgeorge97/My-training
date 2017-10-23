for i in range(997, 100, -1):
    #create the mirrored number of i
    i_mirrored = int(str(i)[::-1])
    #create the palindrome number
    palindrome = i * 1000 + i_mirrored  
    for j in range(999, 100, -1):
        if palindrome % j == 0 and palindrome / j >= 100 and palindrome / j < 1000:
            print(palindrome, j, palindrome // j)
            break
    else:
        continue
    break
