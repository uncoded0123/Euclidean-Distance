# Euclidean Distance
from tkinter import *


def retrieve_hypotenuse():

    root = Tk()

    root.title('Euclidean Distance')

    def get_c():

        a2 = int(e1.get())
        b2 = int(e2.get())
        
        c2 = a2**2 + b2**2
        c = round(c2**(1/2),3)
        
        label3.config(text="Euclidean Distance: {}".format(c))

    # font size
    fnt = 15
    label0 = Label(root,text="Euclidean Distance", font="Helvetica 20")
    label1 = Label(root,text="Delta x", font="Helvetica 20")
    e1 = Entry(root, font="Helvetica %s bold"%(fnt))
    label2 = Label(root,text="Delta y", font="Helvetica 20")
    e2 = Entry(root, font="Helvetica %s bold"%(fnt))


    button1 = Button(root, command=get_c, text="Find",font="Helvetica %s bold"%(fnt))
    label3 = Label(root, font="Helvetica 20")

    label0.pack()
    label1.pack()
    e1.pack()
    label2.pack()
    e2.pack()
    button1.pack()
    label3.pack()
    

    root.mainloop()


retrieve_hypotenuse()
