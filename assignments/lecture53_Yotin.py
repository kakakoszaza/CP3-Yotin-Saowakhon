def vatcalculate(x):
    result = x + (x * 7 / 100)
    return result
x = int(input('Price : '))
print("\nPrice is %d\nTotal Price is" %x,vatcalculate(x))


