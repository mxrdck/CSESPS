

pal = input()



unique_n = len(set(pal))

if len(pal) == unique_n:
    print("NO SOLUTION")

if len(pal) % unique_n == 0:
    
    pass

else:
    print("NO SOLUTION")