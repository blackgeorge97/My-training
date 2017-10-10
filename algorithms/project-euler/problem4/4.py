found=False
for i in range(997,100,-1):
    n=i*1000+i%10*100+i//10%10*10+i//100
    for j in range(999,100,-1):
        if n%j==0 and n/j>=100 and n/j<1000:
            found=True
            break
    if found==True:
        break
print(n,j,n//j)
