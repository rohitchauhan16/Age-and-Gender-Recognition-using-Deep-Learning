from tkinter import *
import os
  
window = Tk()
window.title("DETECTION")
lblwidth = 700
window.geometry("{}x500".format(lblwidth))
window.configure(bg="#BC986A")
#99738E
  
# TITLE
lbl1 = Label(window, text="AGE & GENDER DETECTION", bg="#65350F", fg="white", font="none 24 bold", 
    width=lblwidth, anchor=CENTER)
lbl1.pack()

#GAD
l1 = Label(window, text="GENDER & AGE DETECTION", bg='#BC986A', fg='white',font="none 20 bold")
l1.pack(padx=15,pady=50) 

def prog1():
	os.system("python gad.py")

b1 = Button(window, text="OPEN", font="none 15 bold", bg='#FFFFFF', fg='black', padx=15, command=prog1)
b1.pack()


#DDD
"""l2 = Label(window, text="DROWSINESS DETECTION", bg='#BC986A', fg='white',font="none 20 bold", padx=20)
l2.pack(padx=5,pady=20) 

def prog2():
	os.system("python drowsinessDetection.py")
b2 = Button(window, text="OPEN", font="none 15 bold", bg='#FFFFFF', fg='black',padx=15, command=prog2)
b2.pack()
"""

#Close program

l3 = Label(window, text="CLOSE PROGRAM", bg='#BC986A', fg='white',font="none 20 bold", padx=70)
l3.pack(padx=15,pady=50) 

b3 = Button(window, text="QUIT", font="none 15 bold", bg='#FFFFFF', fg='black',padx=15, command=window.destroy)
b3.pack()


window.mainloop()