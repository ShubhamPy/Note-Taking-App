########################################################################################################################
####################################### NOTESPRO STARTING UI ###########################################################
########################################################################################################################

from tkinter import *
import os
root=Tk()
root.title("Note Taking")
p=Label(root,text="Notespro*", height="18",width="250",bg='brown',fg='white',font=('Helvetica','20','bold','italic'))
p.pack()
root.configure(bg='brown')
root.geometry('400x700')
def notes():
    import functions
butt1=Button(root,text="Launch App",command=notes,bg = "olive",fg='white',padx=40,pady=10,font=('Helvetica','10','bold'))
butt1.pack(padx=25,pady=0)
button=Button(root,text="Exit",command=root.destroy,bg = "#636466",fg='white',padx=65,pady=8,font=('Helvetica','10','bold'))
button.pack(padx=25,pady=10)
root.mainloop()