number = int(input("input number: "))
a,b,c,d = 0,0,1,0

while a < number :
    b = 0
    while b <= number - a - 2 :
        print("  ", end='')
        b += 1

    d = 0
    b = 0
    while d < c :
        print("* ", end='')
        d += 1

    c += 2
    print()
    a += 1



