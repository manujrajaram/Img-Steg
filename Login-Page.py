#importing libraries
from tkinter import *
from PIL import Image
import stepic


def register_user():
    username_info= username.get()
    p=password.get()
    
        
    if(len(username_info)>=1 and len(p)>=1):   
        file=open(username_info+".txt","w")
        if(len(p)==8):
            password_info= password.get()
            file.write(password_info)
            file.close()
            Label(screen1, text ="Signup Successful", fg= "green", font=("Calibri",11)).pack() 
        elif(len(p)>8):
            Label(screen1, text ="Password should not be greater than 8 characters", fg= "red", font=("Calibri",11)).pack()
        elif(len(p)<8):
            Label(screen1, text ="Password should not be less than 8 characters", fg= "red", font=("Calibri",11)).pack()
    else:
        Label(screen1, text="Please enter values in the field").pack()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

        
            
    
def login_check():
    usernamecheck = username1.get()
    passwordcheck = password1.get()

    if(len(usernamecheck)>=1 and len(passwordcheck)>=1):
        try:
            file=open(usernamecheck+".txt","r")
            pas = file.read(8)
            if(passwordcheck == pas):
                Label(screen2, text="Login Successful", fg="green").pack()
            else:
                Label(screen2, text="Incorrect Password", fg="red").pack()
        except:
            Label(screen2, text="User does not exists",fg="red").pack()
    else:
        Label(screen2, text="Please enter the values in the filed", fg="red").pack()

    username_login.delete(0,END)
    password_login.delete(0,END)
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x350")

    global username1
    global password1
    global username_login
    global password_login
    username1 = StringVar()
    password1 = StringVar()

    Label(screen2, text="Username").pack()
    username_login = Entry(screen2, textvariable=username1)
    username_login.pack()
    Label(screen2, text="Password").pack()
    password_login= Entry(screen2, textvariable=password1)
    password_login.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1,command=login_check).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Cancel", width=10, height=1,command=screen2.destroy).pack()
  

def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x350")
    
    global username_entry
    global password_entry
    global username
    global password
    username= StringVar()
    password= StringVar()

    Label(screen1, text="Please enter your details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry= Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="NOTE: Password should contain 8 characters", fg="red").pack()
    Button(screen1, text="Register", width=10, height=1,command=register_user).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Cancel", width=10, height=1,command=screen1.destroy).pack()
    
    
def main_screen():
    global screen
    screen =Tk()
    screen .geometry("400x350")
    screen.title("Image-Steganography")
    Label(text = "Login-Page",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30", command = login).pack()
    Label(text = "").pack()
    Button(text="Register",height="2",width="30", command =register).pack()

    screen.mainloop()

main_screen()
