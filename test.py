blah = [1, 7, 19, 22]



def is_odd(numero):
    odd = True

    if numero % 2 == 0:
        odd = False
    else:
        odd = True
    return odd

#main program

for n in blah:
    if is_odd(n):
        print(f"{n} is odd")
    else:
        print(f"{n} is even")


