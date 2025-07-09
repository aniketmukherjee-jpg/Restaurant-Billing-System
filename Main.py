from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Restaurant Billing System - Aniket Mukherjee(U03AD21S0011)")
        title=Label(self.root,text="Restaurant Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.Samosa=IntVar()
        self.PaneerTikka=IntVar()
        self.MasalaDosa=IntVar()
        self.VegetablePakora=IntVar()
        self.PapdiChaat=IntVar()
        self.TomatoSoup=IntVar()
        self.MasalaPapad=IntVar()
        self.ButterChiken=IntVar()
        self.pasta=IntVar()
        self.BasmathiRice=IntVar()
        self.PannerMasala=IntVar()
        self.PalakPanner=IntVar()
        self.dal=IntVar()
        self.CholeBhature=IntVar()
        self.AlooTikka=IntVar()
        self.BhelPuri=IntVar()
        self.DahiVada=IntVar()
        self.PavBhaji=IntVar()
        self.Chai=IntVar()
        self.Cookies=IntVar()
        self.Coffee=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Samosa).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.PaneerTikka).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Masala Dosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.MasalaDosa).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.VegetablePakora).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.PapdiChaat).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.TomatoSoup).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.MasalaPapad).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        grocery=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=340,y=180,height=380,width=325)

        item8=Label(grocery,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.ButterChiken).grid(row=0,column=1,padx=10)

        item9=Label(grocery,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(grocery,text="Basmathi Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.BasmathiRice).grid(row=2,column=1,padx=10)

        item11=Label(grocery,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.PannerMasala).grid(row=3,column=1,padx=10)

        item12=Label(grocery,text="Palak Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.PalakPanner).grid(row=4,column=1,padx=10)

        item13=Label(grocery,text="Daal",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(grocery,text="Chole Bhuture",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.CholeBhature).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Aloo Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.AlooTikka).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.BhelPuri).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.DahiVada).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.PavBhaji).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Chai",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Chai).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Cookies",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Cookies).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Coffee",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Coffee).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery- Aniket Mukherjee",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Snacks",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_grocery=Label(billing_menu,text="Total Grocery",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Others",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="CGst",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_grocery=Label(billing_menu,text="SGst",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_hygine=Label(billing_menu,text="IGst",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.Samosa.get()*15
    self.no=self.PaneerTikka.get()*150
    self.la=self.MasalaDosa.get()*200
    self.ore=self.VegetablePakora.get()*12
    self.mu=self.PapdiChaat.get()*50
    self.si=self.TomatoSoup.get()*105
    self.na=self.MasalaPapad.get()*70
    total_snacks=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks)+" Rs")
    self.a.set(str(round(total_snacks*0.05,3))+" Rs")

    self.at=self.ButterChiken.get()*170
    self.pa=self.pasta.get()*140
    self.oi=self.PannerMasala.get()*180
    self.ri=self.BasmathiRice.get()*100
    self.su=self.PalakPanner.get()*190
    self.te=self.CholeBhature.get()*120
    self.da=self.dal.get()*110
    total_grocery=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery)+" Rs")
    self.b.set(str(round(total_grocery*0.01,3))+" Rs")

    self.so=self.AlooTikka.get()*60
    self.sh=self.BhelPuri.get()*40
    self.cr=self.PavBhaji.get()*60
    self.lo=self.DahiVada.get()*80
    self.fo=self.Chai.get()*10
    self.ma=self.Cookies.get()*15
    self.sa=self.Coffee.get()*12

    total_hygine=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine)+" Rs")
    self.c.set(str(round(total_hygine*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks+
                total_grocery+
                total_hygine+
                (round(total_grocery*0.01,3))+
                (round(total_hygine*0.10,3))+
                (round(total_snacks*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO URBAN TANDOOR\n\tPhone-No.8017940546")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Samosa.get()!=0:
        self.txtarea.insert(END,f"Samosa\t\t {self.Samosa.get()}\t{self.nu}\n")
    if self.PaneerTikka.get()!=0:
        self.txtarea.insert(END,f"Paneer Tikka\t\t {self.PaneerTikka.get()}\t{self.no}\n")
    if self.MasalaDosa.get()!=0:
        self.txtarea.insert(END,f"Masala Dosa\t\t {self.MasalaDosa.get()}\t{self.la}\n")
    if self.VegetablePakora.get()!=0:
        self.txtarea.insert(END,f"Vegetable Pakora\t\t {self.VegetablePakora.get()}\t{self.ore}\n")
    if self.PapdiChaat.get()!=0:
        self.txtarea.insert(END,f"Papdi Chaat\t\t {self.PapdiChaat.get()}\t{self.mu}\n")
    if self.TomatoSoup.get()!=0:
        self.txtarea.insert(END,f"Tomato Soup\t\t {self.TomatoSoup.get()}\t{self.si}\n")
    if self.MasalaPapad.get()!=0:
        self.txtarea.insert(END,f"Masala Papad\t\t {self.MasalaPapad.get()}\t{self.na}\n")
    if self.ButterChiken.get()!=0:
        self.txtarea.insert(END,f"Butter Chicken\t\t {self.ButterChiken.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.BasmathiRice.get()!=0:
        self.txtarea.insert(END,f"Basmathi Rice\t\t {self.BasmathiRice.get()}\t{self.ri}\n")
    if self.PannerMasala.get()!=0:
        self.txtarea.insert(END,f"Panner Masala\t\t {self.PannerMasala.get()}\t{self.oi}\n")
    if self.PalakPanner.get()!=0:
        self.txtarea.insert(END,f"Palak Paneer\t\t {self.PalakPanner.get()}\t{self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.CholeBhature.get()!=0:
        self.txtarea.insert(END,f"Chole Bhature\t\t {self.CholeBhature.get()}\t{self.te}\n")
    if self.AlooTikka.get()!=0:
        self.txtarea.insert(END,f"Aloo Tikka\t\t {self.AlooTikka.get()}\t{self.so}\n")
    if self.BhelPuri.get()!=0:
        self.txtarea.insert(END,f"Bhel Puri\t\t {self.BhelPuri.get()}\t{self.sh}\n")
    if self.DahiVada.get()!=0:
        self.txtarea.insert(END,f"Dahi Vada\t\t {self.DahiVada.get()}\t{self.lo}\n")
    if self.PavBhaji.get()!=0:
        self.txtarea.insert(END,f"Pav Bhaji\t\t {self.PavBhaji.get()}\t{self.cr}\n")
    if self.Chai.get()!=0:
        self.txtarea.insert(END,f"Chai\t\t {self.Chai.get()}\t{self.fo}\n")
    if self.Cookies.get()!=0:
        self.txtarea.insert(END,f"Cookies\t\t {self.Cookies.get()}\t{self.ma}\n")
    if self.Coffee.get()!=0:
        self.txtarea.insert(END,f"Coffee\t\t {self.Coffee.get()}\t{self.sa}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"CGST : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"SGST : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"IGST : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.Samosa.set(0)
        self.PaneerTikka.set(0)
        self.MasalaDosa.set(0)
        self.VegetablePakora.set(0)
        self.PapdiChaathaat.set(0)
        self.TomatoSoup.set(0)
        self.MasalaPapad.set(0)
        self.ButterChiken.set(0)
        self.pasta.set(0)
        self.BasmathiRice.set(0)
        self.PannerMasala.set(0)
        self.PalakPanner.set(0)
        self.dal.set(0)
        self.CholeBhature.set(0)
        self.AlooTikka.set(0)
        self.BhelPuri.set(0)
        self.DahiVada.set(0)
        self.PavBhaji.set(0)
        self.Chai.set(0)
        self.Cookies.set(0)
        self.Coffee.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
