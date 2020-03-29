from tkinter import *
import math

def leftclickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get()) / 100, 2)
    if result > 30 :
        Bmi = "อ้วนมาก"
    elif result > 25 :
        Bmi = "อ้วน"
    elif result > 23 :
        Bmi = "น้ำหนักเกิน"
    elif result > 18.6 :
        Bmi = "น้ำหนักปกติ เหมาะสม"
    else:
        Bmi = "ผอมเกินไป"
    labelResult1.configure(text = result)
    labelResult3.configure(text= Bmi)

MainWindow = Tk()
labelHight = Label(MainWindow, text="ส่วนสูง (Cm) :")
labelHight.grid(row=0, column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0, column=1)

labelWeight = Label(MainWindow, text="น้ำหนัก (Kg) :")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', leftclickButton)
calculateButton.grid(row=2, column=0)

labelResult1 = Label(MainWindow, text="ผลลัพธ์")
labelResult3 = Label(MainWindow, text="")
labelResult1.grid(row=2, column=1)
labelResult2 = Label(MainWindow, text="BMI :").grid(row=3, column=0)
labelResult3.grid(row=3, column=1)

MainWindow.mainloop()