#In order for a number to be divided by all the numbers from 1 to 20 its enough to be divided by numbers from 11 to 20
i=20
found=False
while found==False:
    i=i+20
    found=True
    for j in range(11,20):
        if i%j!=0:
            found=False
            break
print(i)

    
        
    
	
