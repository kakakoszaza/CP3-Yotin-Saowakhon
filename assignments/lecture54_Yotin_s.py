
def login():
    username = input("Username  : ")
    password = input("Password  : ")
    if username == "admin" and password == "1234":
        print("---correct----\n")
        return showMenu()
    else:
        print("---not correct----\n")
        return login()
def showMenu():
    print("----Ishop-----")
    print("1. Vat calculator")
    print("2. Price calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        print("Vat value = ",vatCalculate(int(input("Input product price : "))))
    elif userSelected == 2:
        print("Total price = ",priceCalculate())
    return userSelected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCalculate(price1 + price2)

login()