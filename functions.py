###################################################################################################################################
##################################### NOTE TAKING APP (NOTESPRO) ##################################################################
###################################################################################################################################
from tkinter import *
import pymysql as pm
from tkinter import messagebox
root=Tk()
root.title("Note Taking App")
p=Label(root, text= 'Notespro',height="20",width="40",bg='#145660',fg='white',font=('Helvetica','18','bold','italic'))
p.place(x=470,y=90)
root.configure(bg='#145660')
root.geometry('1920x1080')
####################################################################################################################################
####################################### ADD NEW NOTES ##############################################################################
####################################################################################################################################
def notes():
    root = Tk()
    root.title("Add Notes")
    root.geometry("1930x1080")
    z = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
    z.pack()
    g = Label(root, height="2", width="12", bg='#636466', fg="white", text="Create Note ID :",
              font=('Helvetica', '18', 'italic'))
    g.place(x=400, y=38)
    root.configure(bg="black")
    tt = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
    tt.place(x=611, y=50)
    txt = Text(root, width='80', height='20', font=('Helvetica', '15'))
    txt.place(x=370, y=100)

    def addnotes():
        try:
            global hu
            hu = int(tt.get())
            tu = txt.get("1.0", "end-1c")
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            query_insert = "insert into test(id,text) values(%d,'%s')" % (hu, tu)
            cursor.execute(query_insert)
            con.commit()
        except pm.DatabaseError as e:
            if con:
                con.rollback()
                print(e)
        finally:
            con.close()
            cursor.close()

    butto2 = Button(root, text="Save>>", command=addnotes, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto2.place(x=1080, y=580)
    butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto3.pack(pady=25)
    root.mainloop()
butt1=Button(root,text="Add New Notes>>",command=notes,bg = "red",padx=40,pady=10,bd=7,fg='white',font=('Helvetica',12,'bold'))
butt1.place(x=370,y=20)

#####################################################################################################################################
####################################### EDIT NOTES ##################################################################################
#####################################################################################################################################
def ed():
    root = Tk()
    root.title("Edit Notes")
    root.geometry("1930x1080")
    p = Label(root, height='22', width="100", bg='#636466', font=('Helvetica', '20', 'italic'))
    p.pack()
    q = Label(root, height="2", width="12", bg='#636466', fg="white", text="Enter Note ID :",
              font=('Helvetica', '18', 'italic'))
    q.place(x=400, y=38)
    root.configure(bg="black")
    tt = Entry(root, bd=5, width='45', font=('Helvetica', '19'))
    tt.place(x=611, y=50)
    txt = Text(root, width='80', height='20', font=('Helvetica', '15'))
    txt.place(x=370, y=100)

    def editmsg():
        try:
            hu = int(tt.get())
            tu = txt.get("1.0", "end-1c")
            con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
            cursor = con.cursor()
            query_text = "update test set text='%s' where id=%d" % (tu, hu)
            cursor.execute(query_text)
            con.commit()
        except pm.DatabaseError as e:
            if con:
                con.rollback()
        finally:
            cursor.close()
            con.close()

    butto2 = Button(root, text="Save>>", command=editmsg, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto2.place(x=1080, y=580)
    butto3 = Button(root, text="Quit", command=root.destroy, bg="red", padx=50, pady=10, fg='white',
                    font=('Helvetica', '8', 'bold'))
    butto3.pack(pady=25)
    root.mainloop()
but=Button(root,text="Edit Notes>>",command=ed,bg = "red",padx=55,pady=10,bd=7,fg='white',font=('Helvetica',12,'bold'))
but.place(x=950,y=20)

################################# LIST BOX #########################################################################################

r=Listbox(root,width='73',height='13',font=('Helvetica','15'))
r.place(x=370,y=400)

#####################################################################################################################################
########################################## SEARCH ###################################################################################
#####################################################################################################################################

q = Label(root, text='Enter Note ID :',bg='#145660',fg='white', font=('Helvetica', '15', 'bold'))
q.place(x=400, y=220)
s1 = Entry(root, bd=5, width='52', font=('Helvetica', '19'))
s1.place(x=400, y=250)
def search():

    try:
        k = int(s1.get())
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        searchquery = "select * from test where id={}".format(k)
        cursor.execute(searchquery)
        data=cursor.fetchone()
        r.insert(END,data)
        con.commit()
    except pm.DatabaseError as e:
        if con:
            con.rollback()
    finally:
        con.close()
        cursor.close()
butt3 = Button(root, text="Search>>", bg="red", padx=25, pady=5, bd=5, fg='white',font=('Helvetica', '10', 'bold'),command=search)
butt3.place(x=610, y=305)

######################################################################################################################################
################################################ DELETE ##############################################################################
######################################################################################################################################

def delete():
    try:
        k = int(s1.get())
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        delete = "delete from test where id={}".format(k)
        cursor.execute(delete)
        con.commit()
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(e)
    finally:
        con.close()
        cursor.close()

butt4= Button(root, text="Delete>>", bg="red", padx=25, pady=5, bd=5, fg='white',font=('Helvetica', '10', 'bold'),command=delete)
butt4.place(x=790,y=305)

#########################################################################################################################################
########################################### SORT NOTES ##################################################################################
#########################################################################################################################################

lab = Label(root, text='List All Notes :',bg='#145660',fg='white', font=('Helvetica', '15', 'bold'))
lab.place(x=700, y=100)
def sortalpha():
    try:
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        query_show = "SELECT * from test ORDER BY text ASC"
        cursor.execute(query_show)
        data = cursor.fetchall()
        raw=list(data)
        root = Tk()
        root.title("List of notes (Sorted in Asc Alphabets)")
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        root.geometry("500x800")
        mylist = Listbox(root, width="900", yscrollcommand=scrollbar.set, font=('Helvetica', '15', 'italic'))
        for l in raw:
            mylist.insert(END, l)
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        root.mainloop()
        con.commit()
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(e)
    finally:
        con.close()
        cursor.close()
bu = Button(root, text="By Alphabets >>", bg="red", padx=25, pady=5, bd=5, fg='white',font=('Helvetica', '10', 'bold'),command=sortalpha)
bu.place(x=530, y=150)

def sortnum():
    try:
        con = pm.connect(host="localhost", database='Notespro', user='root', password='1337')
        cursor = con.cursor()
        query_show = "select * from test"
        cursor.execute(query_show)
        data = cursor.fetchall()
        raw=list(data)
        root = Tk()
        root.title("List of notes (Sorted in ASC Numbers)")
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        root.geometry("500x800")

        mylist = Listbox(root, width="900", yscrollcommand=scrollbar.set, font=('Helvetica', '15', 'italic'))
        for l in raw:
            mylist.insert(END, l)

        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

        root.mainloop()

        con.commit()
    except pm.DatabaseError as e:
        if con:
            con.rollback()
            print(e)
    finally:
        con.close()
        cursor.close()
bu1 = Button(root, text="By Numbers >>", bg="red", padx=25, pady=5, bd=5, fg='white',font=('Helvetica', '10', 'bold'),command=sortnum)
bu1.place(x=820, y=150)

#########################################################################################################################################
#########################################################################################################################################

butt6=Button(root,text="Exit",command=root.destroy,bg = "red",fg='white',padx=50,pady=10,bd='5',font=('Helvetica', '10', 'bold'))
butt6.place(x=710,y=750)
root.mainloop()