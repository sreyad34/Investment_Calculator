from tkinter import *

root = Tk()
root.title("Investment Calculator")

#labeling headers
myLabel = Label(root, text="Pick the button number associated with the option number.")
blankline1 = Label(root, text="                                       ")
c_int_beg = Label(root,text="1: Compound Interest with contributions at begenning of months.",wraplength=200)
c_int_end = Label(root,text="2: Compound Interest with contributions at end of months.",wraplength=200)
c_diff_cont = Label(root,text="3: Compound Interest when contribution rate differs from times compounded.",wraplength=200)
blankline4 = Label(root, text="                                       ")


#where the headers go on the grid
myLabel.grid(row=0,column=0,columnspan=10, padx=100,pady=10)
blankline1.grid(row=1,column=0,columnspan=10, padx=100,pady=10)
c_int_beg.grid(row=2,column=2,columnspan=3, padx=10,pady=10)
c_int_end.grid(row=2,column=5,columnspan=3, padx=10,pady=10)
c_diff_cont.grid(row=2,column=8,columnspan=3, padx=10,pady=10)
blankline4.grid(row=26,column=0,columnspan=10, padx=10,pady=10)

#labeling side column titls
principaltitle = Label(root, text = "Initial Amount")
annualratetitle = Label(root, text="Annual Rate of Return")
compoundedratetitle = Label(root, text="Times Compounded (Yearly/Monthly)", wraplength=250)
contributionstitle = Label(root, text = "Additional Contributions Amount")
timetitle = Label(root, text = "Number of Years Later: ")
periodicconttitle = Label(root, text="Periodic Contributions Compounded (Yearly/Monthly)",wraplength=250)
answertitle = Label(root, text="For your chosen option, your investment will be worth:",wraplength=250)

#where side column titles go
principaltitle.grid(row=3, column=0,columnspan=2, padx=10,pady=10)
annualratetitle.grid(row=4, column=0,columnspan=2, padx=10,pady=10)
compoundedratetitle.grid(row=5, column=0,columnspan=2, padx=10,pady=10)
contributionstitle.grid(row=6, column=0,columnspan=2, padx=10,pady=10)
timetitle.grid(row=7, column=0,columnspan=2, padx=50,pady=10)
periodicconttitle.grid(row=8, column=0,columnspan=2, padx=10,pady=10)
answertitle.grid(row=27, column=0,columnspan=2, padx=10,pady=10)

e = Entry(root, width=20,borderwidth=6)
e.grid(row=27, column=2, columnspan=1, padx=10, pady=10)

#button 1 when clicked
def button_click1(principal, annual_rate, compounded, contributions, time_years):
    e.delete(0,END)
    rate = annual_rate/100
    principle_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    total_compounded = principle_interest+future_val
    e.insert(0,int(total_compounded))

#button 2 when clicked
def button_click2(principal, annual_rate, compounded, contributions, time_years):
    e.delete(0,END)
    rate = annual_rate/100
    principle_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    future_val_end = (future_val)*(1+(rate/compounded))
    total_compounded = principle_interest+future_val_end
    e.insert(0,int(total_compounded))

#button 3 when clicked
def button_click3(principal, annual_rate, compounded, contributions, periodic_cont, time_years):
    e.delete(0,END)
    rate = annual_rate/100
    periodic = periodic_cont/12
    principal_interest = principal*((1+(rate/compounded))**(compounded*time_years))
    future_val = contributions*(((1+(rate/compounded))**(compounded*time_years)-1)/(rate/compounded))
    future_val_cont_end = future_val*periodic
    total_compounded = future_val_cont_end+principal_interest
    e.insert(0,int(total_compounded))


def button_clear():
    e.delete(0,END)


#Entry boxes for 1
b1p = Entry(root,width=20,borderwidth=6)
b1a = Entry(root,width=20,borderwidth=6)
b1com = Entry(root,width=20,borderwidth=6)
b1con = Entry(root,width=20,borderwidth=6)
b1t = Entry(root,width=20,borderwidth=6)
disabled1 = Entry(root,width=20,borderwidth=6, state=DISABLED)

b1p.grid(row=3,column=2, columnspan=1, padx=1,pady=10)
b1a.grid(row=4,column=2, columnspan=1, padx=1,pady=10)
b1com.grid(row=5,column=2, columnspan=1, padx=1,pady=10)
b1con.grid(row=6,column=2, columnspan=1, padx=1,pady=10)
b1t.grid(row=7,column=2, columnspan=1, padx=1,pady=10)
disabled1.grid(row=8,column=2, columnspan=1, padx=1,pady=10)

#Entry boxes for 2
b2p = Entry(root,width=20,borderwidth=6)
b2a = Entry(root,width=20,borderwidth=6)
b2com = Entry(root,width=20,borderwidth=6)
b2con = Entry(root,width=20,borderwidth=6)
b2t = Entry(root,width=20,borderwidth=6)
disabled2 = Entry(root,width=20,borderwidth=6, state=DISABLED)

b2p.grid(row=3,column=5, columnspan=1, padx=1,pady=10)
b2a.grid(row=4,column=5, columnspan=1, padx=1,pady=10)
b2com.grid(row=5,column=5, columnspan=1, padx=1,pady=10)
b2con.grid(row=6,column=5, columnspan=1, padx=1,pady=10)
b2t.grid(row=7,column=5, columnspan=1, padx=1,pady=10)
disabled2.grid(row=8,column=5, columnspan=1, padx=1,pady=10)

#Entry boxes for 3
b3p = Entry(root,width=20,borderwidth=6)
b3a = Entry(root,width=20,borderwidth=6)
b3com = Entry(root,width=20,borderwidth=6)
b3con = Entry(root,width=20,borderwidth=6)
b3pc = Entry(root,width=20,borderwidth=6)
b3t = Entry(root,width=20,borderwidth=6)

b3p.grid(row=3,column=8, columnspan=1, padx=1,pady=10)
b3a.grid(row=4,column=8, columnspan=1, padx=1,pady=10)
b3com.grid(row=5,column=8, columnspan=1, padx=1,pady=10)
b3con.grid(row=6,column=8, columnspan=1, padx=1,pady=10)
b3pc.grid(row=7,column=8, columnspan=1, padx=1,pady=10)
b3t.grid(row=8,column=8, columnspan=1, padx=1,pady=10)


#creation of solving buttons
button_1 = Button(root, text="Solve for Option 1",padx=40,pady=20,command=lambda: button_click1(int(b1p.get()),int(b1a.get()),int(b1com.get()),int(b1con.get()),int(b1t.get())))
button_2 = Button(root, text="Solve for Option 2",padx=40,pady=20,command=lambda: button_click2(int(b2p.get()),int(b2a.get()),int(b2com.get()),int(b2con.get()),int(b2t.get())))
button_3 = Button(root, text="Solve for Option 3",padx=40,pady=20,command=lambda: button_click3(int(b3p.get()),int(b3a.get()),int(b3com.get()),int(b3con.get()),int(b3pc.get()),int(b3t.get())))
clear_button = Button(root, text="Clear",padx=40,pady=20, command=button_clear)


#where solving buttons go on grid
button_1.grid(row=9,column=2)
button_2.grid(row=9,column=5)
button_3.grid(row=9,column=8)
clear_button.grid(row=27,column=5)


root.mainloop()
