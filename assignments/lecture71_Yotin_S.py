menuList = []
priceList = []
def showbill():
    for number in range(len(menuList)):
        print(menuList[number], priceList[number],'บ.')
def sumPrice():
        print('Total : ', sum(priceList),'บ.')

print('-----Welcome to FoodLand----')
while True :
    menuName = input('Please Enter menu : ')
    if(menuName.lower()== "exit"):
        break
    else:
        menuPrice = int(input('Price : '))
        menuList.append(menuName)
        priceList.append(menuPrice)

print('.........YOUR ORDER.........')
showbill()
sumPrice()
print('..........THANKYOU..........')
