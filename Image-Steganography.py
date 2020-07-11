from tkinter import *
import os.path
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
import stepic


def encode_logic():
    msg=message.get()
    new=newfile.get()
    try:
        im=Image.open(c)
        im1=stepic.encode(im,bytes(msg,'utf-8'))
        im1.save(foldername+"/"+new+".png",'PNG')
    except:
        Label(screen6, text="").pack()
        Label(screen6, text="Unable to encode").pack()
    else:
        Label(screen6, text="").pack()
        Label(screen6, text="Successfully Encoded",fg="green").pack()
    


def choose_folder():
    global foldername
    foldername=filedialog.askdirectory()

    global screen6
    screen6= Toplevel(screen)
    screen6.title("Choosing-Folder")
    screen6.geometry("450x400+500+200")
    Label(screen6,text = "Encoding",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen6, text="").pack()

    Label(screen6, text="").pack()
    Label(screen6,text="Folder chosen is:").pack()
    Label(screen6,text=foldername, fg="blue").pack()
    Label(screen6, text="").pack()

    Label(screen6, text="").pack()
    Button(screen6,text="Proceed",width=30,height=1,command=encode_logic).pack()

    Label(screen6, text="").pack()
    Button(screen6,text="Exit",width=10,height=1,command=screen6.destroy).pack()
    
   
    


def encoding():
    global screen5
    global message
    global newfile
    
    
    screen5=Toplevel(screen)
    screen5.title("Encoding")
    screen5.geometry("450x400+500+200")
    Label(screen5,text = "Encoding",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen5, text="").pack()

    message=StringVar()
    newfile=StringVar()
    
    Label(screen5, text="Enter the text to be encoded",fg="blue").pack()
    msg_entry = Entry(screen5, textvariable=message)
    msg_entry.pack()
    
    
    Label(screen5, text="").pack()
    
    Label(screen5, text="Enter the name of the new file").pack()
    new_entry = Entry(screen5, textvariable=newfile)
    new_entry.pack()

    Label(screen5,text="Choose the location for saving new file").pack()
    Button(screen5,text="Proceed & Select Folder",width=30,height=1,command=choose_folder).pack()


def encode():
    choice=askopenfilename(initialdir = "/",title = "Choose an Image",filetypes =(("PNG Files","*.png"),("All Files","*.*")))
    global screen4
    global c


    c=choice
    
    screen4=Toplevel(screen)
    screen4.title("Encode")
    screen4.geometry("450x400+500+200")
    
    Label(screen4,text = "Encode",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen4, text="").pack()
    
    Label(screen4,text="Image chosen is:").pack()
    Label(screen4,text=choice, fg="blue").pack()
    Label(screen4, text="").pack()
    
    Button(screen4,text="Proceed",width=10,height=1,command=encoding).pack()
    
def decode():
    choicedecode=askopenfilename(initialdir = "/",title = "Choose an Image",filetypes =(("PNG Files","*.png"),("All Files","*.*")))
    cd=choicedecode
    global screen7
    screen7=Toplevel(screen)
    screen7.title("Decode")
    screen7.geometry("450x400+500+200")

    Label(screen7,text = "Decode",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen7, text="").pack()

    Label(screen7,text="Message decoded is").pack()
    im2=Image.open(cd)
    msgImg=stepic.decode(im2)

    Label(screen7, text="").pack()
    Label(screen7,text=msgImg,fg="blue",font=("Calibri",13)).pack()

    Label(screen7, text="").pack()
    Button(screen7,text="Exit",width=10,height=1,command=screen7.destroy).pack() 


def main_page():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Image Steganography")
    screen3.geometry("450x400+500+200")
    Label(screen3,text = "Welcome"+" "+str(usernamecheck)+"!",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Encode Text", width=20, height=4,command=encode).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Decode Text", width=20, height=4,command=decode).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Cancel",width=10,height=1,command=screen3.destroy).pack()    


    
def register_user():
    global savepath
    global filename
    username_info= username.get()
    p=password.get()

    savepath= './Users/'
    filename= os.path.join(savepath,username_info+".txt")
        
    if(len(username_info)>=1 and len(p)>=1):
        if(os.path.exists(filename)):
            Label(screen1, text="User already exists",fg="red").pack()
        else:
            file=open(filename,"w")
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
    global usernamecheck
    savepath= './Users/'
    usernamecheck = username1.get()
    passwordcheck = password1.get()

    filenamelogin= os.path.join(savepath,usernamecheck+".txt")
    if(len(usernamecheck)>=1 and len(passwordcheck)>=1):
        try:
            file=open(filenamelogin,"r")
            pas = file.read(8)
            if(passwordcheck == pas):
                main_page()
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
    screen2.geometry("450x400+500+200")

    global username1
    global password1
    global username_login
    global password_login
    username1 = StringVar()
    password1 = StringVar()

    Label(screen2,text = "Login-Page",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Username").pack()
    username_login = Entry(screen2, textvariable=username1)
    username_login.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    password_login= Entry(screen2, show='*', textvariable=password1)
    password_login.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1,command=login_check).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Cancel",width=10,height=1,command=screen2.destroy).pack()    


    
def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("450x400+500+200")
    
    global username_entry
    global password_entry
    global username
    global password
    username= StringVar()
    password= StringVar()

    Label(screen1,text = "SignUp-Page",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Please enter your details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    password_entry= Entry(screen1,show='*',textvariable=password)
    password_entry.pack()
    Label(screen1, text="NOTE: Password should contain 8 characters", fg="red").pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1,command=register_user).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Cancel",width=10,height=1,command=screen1.destroy).pack()    


    
def main_screen():
    global screen
    screen =Tk()
    screen .geometry("450x400+500+200")
    screen.title("Image-Steganography")
    Label(text = "Welcome",bg ="grey",width="300",height="2", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30", command = login).pack()
    Label(text = "").pack()
    Button(text="Register",height="2",width="30", command =register).pack()
    Label(screen, text="").pack()
    Button(screen, text="Exit",width=10,height=1,command=screen.destroy).pack()    

    screen.mainloop()

main_screen()
