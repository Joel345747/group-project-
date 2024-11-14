from tkinter import *

def sel():
   if (var.get() == 1):
       label.config(text ='orange cat')
   elif (var.get() ==2):
      label.config(text ='spotted dog')
   elif (var.get() ==3):
      label.config(text = 'brown cow')
   elif (var.get() ==4):
      label.config(text = 'blue bird')
root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="cat", variable=var, value =1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="dog", variable=var, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="cow", variable=var, value=3, command=sel)
R3.pack( anchor = W)
R4 = Radiobutton(root, text="bird", variable=var, value=4, command=sel)
R4.pack( anchor = W)
label = Label(root)
label.pack()
root.mainloop()
