from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

userdatadict={"admin":"admin123455"}

def on_enter(event):
    if usernameentry.get()=="Username":
        usernameentry.delete(0,END)
def on_enter2(event):
    if passwordentry.get()=="Password":
        passwordentry.delete(0,END)
def registeruser():
    userdatadict[username]= password
    print(userdatadict)

def logincheck():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror('Error','All Fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='0931')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','User doesnt exist')

        else:
            messagebox.showinfo('Welcome','Successful Login')
            window.destroy()





def global_window1():
    global window
    window=Tk()
    window.title("Login")
    window.geometry("990x660+500+300")
    window.resizable(0,0)
    global check
    check=0
    def hidepassword():
        global check
        if check==0:
            global openeyeimg
            hidepasswordbutton.configure(text="Hide  Password")
            openeyeimg = ImageTk.PhotoImage(file="images/openeye.png")
            closeyeimagelabel.configure(image=openeyeimg)
            passwordentry.configure(show="")
            check=1
        else:
            global closeyeimg
            hidepasswordbutton.configure(text="Show Password")
            closeyeimg=ImageTk.PhotoImage(file="images/closeye.png")
            closeyeimagelabel.configure(image=closeyeimg)
            passwordentry.configure(show="*")
            check=0


    bgimage=ImageTk.PhotoImage(file="images/bg.jpg")
    imagelabel=Label(window, image=bgimage)
    imagelabel.place(x=0, y=0)

    labellogin=Label(window, text="User Login", fg="#FF005E", font="Calibri 23 bold", bg="white")
    labellogin.place(x=632, y=120)
    
    global usernameentry, passwordentry
    #username
    usernameentry=Entry(window, width=25, bd=0, font="Calibri 11", fg="#DE6994")
    usernameentry.place(x=605, y=220)
    usernameentry.insert(0,"Username")
    usernameentry.bind("<FocusIn>", on_enter)
    frame1=Frame(window,width=200,height=2,bg="firebrick1")
    frame1.place(x=605,y=240) 
    #password
    passwordentry=Entry(window, width=25, bd=0, font="Calibri 11", fg="#DE6994",show="*")
    passwordentry.place(x=605, y=280)
    passwordentry.insert(0,"Password")
    passwordentry.bind("<FocusIn>", on_enter2)
    frame2=Frame(window,width=200,height=2,bg="firebrick1")
    frame2.place(x=605,y=300)
    global closeyeimage
    closeyeimage=ImageTk.PhotoImage(file="images/closeye.png")
    closeyeimagelabel=Label(window, image=closeyeimage, bg="white", bd=0)
    closeyeimagelabel.place(x=770, y=270)
    #hide password label
    hidepasswordbutton=Button(window,text="Show Password",font="Calibri 8",command=hidepassword, cursor="hand2",bd=0,bg="white",fg="#FF005E")
    hidepasswordbutton.place(x=720, y=308)
    #login
    loginbutton=Button(window, text="Login", bg="#FF005E", font="Calibri 12 bold", width=24, bd=0, fg="white", cursor="hand2", command=logincheck)
    loginbutton.place(x=605, y=350)

    loginchoice=Label(window, text="------Or login with------", fg="#FF005E", font="Calibri 14", bg="white")
    loginchoice.place(x=615, y=410)

    facebookimage=ImageTk.PhotoImage(file="images/facebook.png")
    facebookimglabel=Label(window, image=facebookimage, bg="white", cursor="hand2")
    facebookimglabel.place(x=620, y=450)

    googleimage=ImageTk.PhotoImage(file="images/google.png")
    googleimglabel=Label(window, image=googleimage, bg="white", cursor="hand2")
    googleimglabel.place(x=685, y=450)

    twitterimage=ImageTk.PhotoImage(file="images/twitter.png")
    twitterimglabel=Label(window, image=twitterimage, bg="white", cursor="hand2")
    twitterimglabel.place(x=750, y=450)
    #don'thaveaccount
    donthaveanaccountlabel=Label(window, text="Don't have an account yet?", fg="#FF005E", font="Calibri 9", bg="white")
    donthaveanaccountlabel.place(x=605, y=510)
    signupbutton=Button(window, text="Sign up.", bd=0, bg="white", fg="blue", cursor="hand2", command=signupwindow)
    signupbutton.place(x=755, y=509)



    window.mainloop()



def signupwindow():
    window.destroy()
    window2=Tk()
    window2.title("Sign Up")
    window2.geometry("990x660+500+300")
    window2.resizable(0,0)
    def on_enterr(event):
        if emailentry.get()=="E-mail":
            emailentry.delete(0,END)
    def on_enter22(event):
        if usernameentry1.get()=="Username":
            usernameentry1.delete(0,END)
    def on_enter3(event):
        if passwordentry1.get()=="Password":
            passwordentry1.delete(0,END)
    def on_enter4(event):
        if confirmpasswordentry.get()=="Confirm Password":
            confirmpasswordentry.delete(0,END)
    #messages
    def enterdata():
        termsandconditions=accept_var1.get()
        if termsandconditions=="Accepted":
            email=emailentry.get()
            global username, password
            username=usernameentry1.get()
            password=passwordentry1.get()
            confirmpassword=confirmpasswordentry.get()
            emailat=email.find("@")
            emaildotcom=email.find(".com")
            if password!=confirmpassword:
                messagebox.showwarning(title="Error", message="Password not confirmed.")
            if emailat==-1 or emaildotcom==-1:
                messagebox.showwarning(title="Error", message="Wrong E-mail.")
            if password==confirmpassword and emailat!=-1 and emaildotcom!=-1:
                try:
                    con=pymysql.connect(host='localhost',user='root',password='0931')
                    mycursor=con.cursor()
                except:
                    messagebox.showerror('Error','Database Connectivity Issue, Please try Again')
                    return
                try:
                    query='create database userdata'
                    mycursor.execute(query)
                    query='use userdata'
                    mycursor.execute(query)
                    query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))' 
                    mycursor.execute(query)
                except:
                    mycursor.execute('use userdata')
                query='select * from data where username=%s'
                mycursor.execute(query,(usernameentry1.get()))
                row=mycursor.fetchone()
                if row !=None:
                    messagebox.showerror('Error','Username Already Exists')
                else:
                    query='insert into data(email,username,password) values(%s,%s,%s)'
                    mycursor.execute(query,(emailentry.get(),usernameentry1.get(),passwordentry1.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration is Successful")

                window2.destroy()
                registeruser()
                global_window1()
        else:
            messagebox.showwarning(title="Error", message="You must accept the terms and conditions before proceeding.")
    global bgimage2
    bgimage2=ImageTk.PhotoImage(file="images/bg.jpg")
    imagelabel2=Label(window2, image=bgimage2)
    imagelabel2.place(x=0, y=0)
    
    frame3=Frame(window2, bg="white")
    frame3.place(x=553, y=100)
    signuplabel=Label(frame3, text="Sign Up", font="Calibri 27 bold", fg="firebrick1" , bg="white")
    signuplabel.grid(row=0,column=0,pady=20,padx=85)

    emailentry=Entry(window2, width=25, bd=0, font="Calibri", fg="#DE6994" , bg="white")
    emailentry.place(x=605, y=210)
    emailentry.insert(0, "E-mail")
    emailentry.bind("<FocusIn>", on_enterr)
    frame=Frame(window2, width=200, height=2, bg="firebrick1")
    frame.place(x=605, y=230)

    usernameentry1=Entry(window2, width=25, bd=0, font="Calibri", fg="#DE6994", bg="white")
    usernameentry1.place(x=605, y=270)
    usernameentry1.insert(0, "Username")
    usernameentry1.bind("<FocusIn>", on_enter22)
    frame2=Frame(window2, width=200, height=2, bg="firebrick1")
    frame2.place(x=605, y=290)

    passwordentry1=Entry(window2, width=25, bd=0, font="Calibri", fg="#DE6994", bg="white")
    passwordentry1.place(x=605, y=330)
    passwordentry1.insert(0, "Password")
    passwordentry1.bind("<FocusIn>", on_enter3)
    frame3=Frame(window2, width=200, height=2, bg="firebrick1")
    frame3.place(x=605, y=350)

    confirmpasswordentry=Entry(window2, width=25, bd=0, font="Calibri", fg="#DE6994", bg="white")
    confirmpasswordentry.place(x=605, y=390)
    confirmpasswordentry.insert(0, "Confirm Password")
    confirmpasswordentry.bind("<FocusIn>", on_enter4)
    frame3=Frame(window2, width=200, height=2, bg="firebrick1")
    frame3.place(x=605, y=410)

    accept_var1=StringVar(value="Not Accepted")
    termscheckbutton=Checkbutton(window2, text="I agree to the Terms & Conditions", font="Calibri 8", fg="#DE6994", bg="white", cursor="hand2", variable=accept_var1, onvalue="Accepted", offvalue="Not Accepted")
    termscheckbutton.place(x=600, y=440)

    signup1button=Button(window2, text="Sign Up", bd=0, bg="firebrick1", fg="white", font="Calibri 14", cursor="hand2", width=20, command=enterdata)
    signup1button.place(x=600, y=470)

global_window1()
