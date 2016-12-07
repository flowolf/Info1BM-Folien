
def euklid(a,b):
    if a == 0:
        return b
    while b > 0:
        if a > b:
            a = a - b
            print("a: " + str(a))
        else:
            b = b - a
            print("b: " + str(b))
    return a
