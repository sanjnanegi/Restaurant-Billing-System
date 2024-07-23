from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

text_Input = StringVar()
operator = ""

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300, height=700,bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

#=================================================================
#                  			CALCULATOR
#=================================================================
def btnclick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f2,font=('arail', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="7", bg="powder blue", command=lambda: btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="8", bg="powder blue", command=lambda: btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="9", bg="powder blue", command=lambda: btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="+", bg="powder blue", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="4", bg="powder blue", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="5", bg="powder blue", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="6", bg="powder blue", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="-", bg="powder blue", command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="1", bg="powder blue", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="2", bg="powder blue", command=lambda: btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="3", bg="powder blue", command=lambda: btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="*", bg="powder blue", command=lambda: btnclick("*"))
Multiply.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="0", bg="powder blue", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="C", bg="powder blue", command=btnClearDisplay)
btnClear.grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="=", bg="powder blue", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="/", bg="powder blue", command=lambda: btnclick("/"))
Division.grid(row=5,column=3) 

#========================================================================
#                  		TIME AND HEADING NAME
#========================================================================

localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="7TH HEAVEN",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#========================================================================
#                  		BILL CALCULATIONS
#========================================================================

def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Paneer.get()==""):
        CoPaneer=0
    else:
        CoPaneer=float(Paneer.get())

   
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())


    if (MixVeg.get()==""):
        CoMixVeg=0
    else:
        CoMixVeg=float(MixVeg.get())


    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())

        
    if (Tea.get()==""):
        CoTea=0
    else:
        CoTea=float(Tea.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofPaneer = CoPaneer * 250
    CostofDrinks= CoD * 300
    CostofDosa = CoDosa* 150
    CostofMixVeg = CoMixVeg * 90
    CostPulav = CoPulav* 120
    CostTea = CoTea * 40


    Central_GST= (((CostofPaneer+CostofDrinks+CostofDosa+CostofMixVeg+CostPulav+CostTea)* 2.5)/100)

    State_GST =(((CostofPaneer+CostofDrinks+CostofDosa+CostofMixVeg+CostPulav+CostTea)* 2.5)/100)

    Total_cost = (CostofPaneer+CostofDrinks+CostofDosa+CostofMixVeg+CostPulav+CostTea)

    CostofMeal= "Rs", str('%.2f' % (CostofPaneer+CostofDrinks+CostofDosa+CostofMixVeg+CostPulav+CostTea))
    C_gst = "Rs", str ('%.2f' % Central_GST)
    S_gst = "Rs", str ('%.2f' % State_GST)
    OverAllCost ="Rs", str ('%.2f' % (Total_cost+Central_GST+State_GST))


    Sgst.set(S_gst)
    Cost.set(CostofMeal)
    Cgst.set(C_gst)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    Tea.set("")
    Paneer.set("")
    Dosa.set("")
    MixVeg.set("")
    Pulav.set("")
    Drinks.set("")

    rand.set("")

    Total.set("")
    Sgst.set("")
    Cgst.set("")
    Cost.set("")
    
#========================================================================
#                  RESTAURANT MENU
#========================================================================
Tea=StringVar()
Paneer=StringVar()
Dosa=StringVar()
MixVeg=StringVar()
Pulav=StringVar()
Drinks=StringVar()
rand = StringVar()
Cost=StringVar()
Sgst=StringVar()
Cgst=StringVar()
Total=StringVar()


lblTea= Label(f1, font=('arial', 16, 'bold'),text="Tea",bd=16,anchor="w")
lblTea.grid(row=0, column=0)
lblTea=Entry(f1, font=('arial',16,'bold'),textvariable=Tea,bd=10,insertwidth=4,bg="white",justify='right')
lblTea.grid(row=0,column=1)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=1, column=0)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="white",justify='right')
txtDrinks.grid(row=1,column=1)

lblMixVeg= Label(f1, font=('arial', 16, 'bold'),text="Ice-Cream",bd=16,anchor="w")
lblMixVeg.grid(row=2, column=0)
lblMixVeg=Entry(f1, font=('arial',16,'bold'),textvariable=MixVeg,bd=10,insertwidth=4,bg="white",justify='right')
lblMixVeg.grid(row=2,column=1)

lblPaneer= Label(f1, font=('arial', 16, 'bold'),text="Paneer",bd=16,anchor="w")
lblPaneer.grid(row=3, column=0)
txtPaneer=Entry(f1, font=('arial',16,'bold'),textvariable=Paneer,bd=10,insertwidth=4,bg="white",justify='right')
txtPaneer.grid(row=3,column=1)

lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=4, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="white",justify='right')
txtDosa.grid(row=4,column=1)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Rice-Plate",bd=16,anchor="w")
lblPulav.grid(row=5, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="white",justify='right')
txtPulav.grid(row=5,column=1)


#========================================================================
#                  RESTAURANT BILL INFO
#========================================================================

lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=2)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblSgst= Label(f1, font=('arial', 16, 'bold'),text="SGST",bd=16,anchor="w")
lblSgst.grid(row=2, column=2)
txtSgst=Entry(f1, font=('arial',16,'bold'),textvariable=Sgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSgst.grid(row=2,column=3)


lblCgst= Label(f1, font=('arial', 16, 'bold'),text="CGST",bd=16,anchor="w")
lblCgst.grid(row=3, column=2)
txtCgst=Entry(f1, font=('arial',16,'bold'),textvariable=Cgst,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCgst.grid(row=3,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=4,column=3)


#========================================================================
#                  BUTTONS
#========================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)


root.mainloop()
