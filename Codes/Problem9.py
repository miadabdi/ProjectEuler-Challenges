import time
start = time.time()

def Pythagorean(limit):
    for a in range (1,limit):
        for b in range(a , limit):
            c = (a**2 + b**2)**0.5
            if a + b + c == limit:
                if (a**2) + (b**2) == c**2:
                    print("the product is:",int(a*b*c),"and made by",a,"*",b,"*",int(c))
                    return
Pythagorean(1000)

end = time.time()
print("it took {} seconds".format(end - start))
