from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
from operator import itemgetter


def Register():
    regWindow = Tk()
    regWindow.title("Register")
    regWindow.geometry("400x400")

    connectt = mysql.connector.connect(host= "localhost" ,user = "root" , passwd = "Earnbitlogin" ,database="registerandlogin")                                  
    cursor = connectt.cursor()

    Text= Label(text="Registration",font="Verdana 20 bold")
    Text.place(x=100,y=30)

    name = Label(regWindow,text="Name")
    name.place(x=90,y=100)                                   
    email = Label(regWindow,text="Email")
    email.place(x=90,y=140)
    password = Label(regWindow,text="password")
    password.place(x=90,y=180)                                      
    reenter = Label(regWindow,text="re-enter")
    reenter.place(x=90,y=220)

    e1= Entry(regWindow)
    e1.place(x=180,y=100)
    e2= Entry(regWindow)
    e2.place(x=180,y=140)                       
    e3= Entry(regWindow,show="*")
    e3.place(x=180,y=180)                                   
    e4= Entry(regWindow,show="*")
    e4.place(x=180,y=220)
                                       
    def clearEntryBox():
        e1.delete(first=0,last=25)
        e2.delete(first=0,last=25)
        e3.delete(first=0,last=25)        
        e4.delete(first=0,last=25)

    def error():
        msg.showerror(title="error",message="password not same")

    def insert():
        insert= ("insert into Register (namee,email,password,reenter) values(%s,%s,%s,%s)")
        values= [e1.get(),e2.get(),e3.get(),e4.get()]
        cursor.execute(insert,values)
        if e3.get() == e4.get():
            connectt.commit()
            clearEntryBox()
            msg.showinfo(title="done",message="Account created")
        else:
            error()
            
    register= Button(regWindow,text="Register",fg="green",font="Verdana 10 bold",command=insert)
    register.place(x=175,y=260)

    exitbutton= Button(regWindow,text="Exit",bg="red",command=regWindow.destroy)
    exitbutton.place(x=350,y=350)


def Login():
    loginWindow = Tk()
    loginWindow.title("Register")
    loginWindow.geometry("400x400")

    connecttt = mysql.connector.connect(host= "localhost" ,user = "root" , passwd = "Earnbitlogin" ,database="registerandlogin")                                  
    cursor1 = connecttt.cursor()

    connectttt = mysql.connector.connect(host= "localhost" ,user = "root" , passwd = "Earnbitlogin" ,database="registerandlogin")                                  
    cursor2 = connectttt.cursor()
     
    Text= Label(text="Registration",font="Verdana 20 bold")
    Text.place(x=140,y=30)
                                   
    email = Label(loginWindow,text="Email")
    email.place(x=100,y=150)
    password = Label(loginWindow,text="password")
    password.place(x=100,y=180)  

    e1= Entry(loginWindow)
    e1.place(x=160,y=150)
    e2= Entry(loginWindow,show="*")
    e2.place(x=160,y=180)

    def check():
        fetchmail="select email from Register"
        fetchpass="select password from Register"

        cursor1.execute(fetchmail)
        cursor2.execute(fetchpass)

        email=e1.get()
        password=e2.get()
        e=[]
        p=[]
        for i in cursor1:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res1=list(map(itemgetter(0),e))
        res2=list(map(itemgetter(0),p))
        k = len(res1)
        i=1
        while i < k:
            if res1[i]==email and res2[i]==password:
                msg.showinfo(title="Done",message="Login successful")
                break
            i+=1
        else:
            msg.showerror(title="Error",message="Something went wrong")


    login= Button(loginWindow,text="Login",fg="green",font="Verdana 10 bold",command=check)
    login.place(x=160,y=200)

    exitbutton= Button(loginWindow,text="Exit",bg="red",command=loginWindow.destroy)
    exitbutton.place(x=350,y=350)

    loginWindow.mainloop()
    
    

mainWindow = Tk()
mainWindow.title("Welcome To EarnBit")
mainWindow.geometry("400x400")

Text= Label(text="Login and Registration",font="Verdana 20 bold")
Text.place(x=30,y=30)    

toRegister = Button(mainWindow,text="Register",fg="green",font="Verdana 10 bold",command=Register)
toRegister.place(x=120,y=220)

toLogin = Button(mainWindow,text="Login",fg="green",font="Verdana 10 bold",command=Login)
toLogin.place(x=200,y=220)

exitbutton= Button(mainWindow,text="Exit",bg="red",command=mainWindow.destroy)
exitbutton.place(x=350,y=350)

mainWindow.mainloop()    
