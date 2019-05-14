print('--------------------------','LogIn','--------------------------')
user = input('Username : ')
password = input('Password : ')
if user == 'ronin' and password == '1996' :
    print('------------------','Connected Done !','------------------')
    print('Welcome To _Smile_Shops...')
    print('>>> User : %s >>>\n' %user)
    print('--- กรุณาเลือกสินค้า ---\n1. USB 3.0 Hub\n2. USB 3.1 Hub')
    selected = int(input('Select >> '))
    if selected == 1 :
        price,vat = 325,7
        to1 = price + (price * vat / 100)
        print('USB 3.0 Hub')
        print('Price = %d  THB' %price ,' + ','Vat 7 %')
        a = int(input('จำนวน (1-2) :  '))
        if a == 1 :
            print('\nUSB 3.0 Hub จำนวน 1ชิ้น\nPrice = %.2f  THB' %to1)
        elif a == 2 :
            to2 = to1 * 2
            print('\nUSB 3.0 Hub จำนวน 2 ชิ้น\nPrice = %.2f  THB' %to2)

    elif selected == 2 :
        price,vat = 465,7
        to1 = price + (price * vat / 100)
        print('\nUSB 3.1 Hub')
        print('Price = %d  THB' %price ,' + ','Vat 7 %')
        a = int(input('จำนวน (1-2) :  '))
        if a == 1 :
            print('\nUSB 3.1 Hub จำนวน 1 ชิ้น\nPrice = %.2f  THB' %to1)
        elif a == 2 :
            to2 = to1 * 2
            print('\nUSB 3.1 Hub จำนวน 2 ชิ้น\nPrice = %.2f  THB' %to2)


    
    
    
