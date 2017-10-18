found = False
for a in range(1, 250):
    for b in range(1, 500):
        csqr = a**2 + b**2 
        c = 1000 - a - b
        if c**2 == csqr:
            found = True
            break
    if found:
        break
print(a, b, c, a*b*c) 
        
        
