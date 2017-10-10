summ=0
a,b=1,2
while b<4000000:
    if b%2==0:
        summ=summ+b
    a,b=b,a+b
print(summ)


