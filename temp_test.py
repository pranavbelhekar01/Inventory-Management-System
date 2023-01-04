from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import os
import email_password
import smtplib
import time

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title('Login system | Developed By Pranav')
        self.root.geometry('1350x700+0+0')
        self.mail_otp=''


        self.bg_1 = ImageTk.PhotoImage(file='photos/login_bg.png')
        frame_label = Label(self.root, image=self.bg_1, bd_=0).place(x=0, y=0, relheight=1, relwidth=1)
        # self.phone_image=ImageTk.PhotoImage(file='photos/login_bg.png')  
        # self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=300, y = 200)

root = Tk()
obj= Login_System(root)
root.mainloop()
    