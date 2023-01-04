from tkinter import *
from PIL import ImageTk, Image
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


        self.bg_1 = ImageTk.PhotoImage(file='photos/updated_bg.png')
        frame_label = Label(self.root, image=self.bg_1, bd_=0).place(x=4, y=4, relheight=1, relwidth=1)

        # self.cart = ImageTk.PhotoImage(file='photos/cart.png')
        # frame_label = Label(self.root, image=self.cart, bd_=0).place(x=4, y=4, width=200, height=250)
        # self.cart=Image.open('photos\cart2.png')
        # self.cart=self.cart.resize((200,300), Image.ANTIALIAS)
        # self.cart=ImageTk.PhotoImage(self.cart)
        # frame_label = Label(self.root, image=self.cart, bd_=0).place(x=200, y=200, width=200, height=250)



        #==================Image===================
        # self.phone_image=ImageTk.PhotoImage(file='photos/images.png')  
        # self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=300, y = 200) 


        #==================Login Frame =============  
        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame = Frame(self.root, bd=0, relief=RIDGE, bg='#2C74B3')
        login_frame.place(x=545, y=98, width=320, height=430)  


        title= Label(login_frame, text='Login System', font=('Footlight MT Light', 30,'bold'), bg='#2C74B3').place(x=0, y = 30, relwidth=1)
        hr=Label(login_frame).place(x=8, y=90, width=390, height=2)

        lbl_user=Label(login_frame, text= 'Employee ID', font=('Rockwell', 15), bg='#2C74B3').place(x=40, y=100)
        
        txt_username=Entry(login_frame, textvariable=self.employee_id, font=('times new roman', 15), bg='lightyellow').place(x=40, y=140, width=250)


        lbl_pass=Label(login_frame, text= 'Password', font=('Rockwell', 15), bg='#2C74B3').place(x=40, y=180)
        txt_pass=Entry(login_frame, textvariable=self.password,show='*', font=('times new roman', 15), bg='lightyellow').place(x=40, y=220, width=250)
        

        btn_login=Button(login_frame, text='Log In', command=self.login, font=('Arial Rounded MT Bold',15), bg = '#6ECCAF', activebackground='#6ECCAF', cursor='hand2').place(x=40, y=280, width=250, height=35)

        hr=Label(login_frame).place(x=40, y=350, width=250, height=2)
        or_=Label(login_frame, text='OR', fg='#F2EBE9', font=('times new roman', 12, 'bold'), bg='#2C74B3').place(x=150, y=337)

        btn_forget=Button(login_frame, text='Forget Password?', command=self.forget_password, font=('times new roman',13), fg='#DFF6FF',bd=0, activeforeground='blue', cursor='hand2', bg='#2C74B3').place(x=100, y=370)
       
        lbl_reg=Label(login_frame,text="WELCOME TO MY CART", font=('times new roman', 18, 'bold'), bg='#2C74B3', fg='#FFA500').place(x=24, y=400)
        

        #===================== Animation Images ================

        # self.im1=ImageTk.PhotoImage(file='photos/images.png')
        # self.im2=ImageTk.PhotoImage(file='photos/store.png')
        # self.im3=ImageTk.PhotoImage(file='photos/icon.png')


        # self.lbl_change_image=Label(self.root, bg='gray')
        # self.lbl_change_image.place(x=325, y=245, width=121, height=214)
        
        # self.animate()

#====================== All Functions ==========================
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000)
        # self.lbl_change_image.after(2000, self.animate)

    def login(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.employee_id.get()=='' or self.password.get()=='':
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            
            else:
                cur.execute('select utype from employee where eid=%s and pass=%s', (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror('Error', 'Invalid USERNAME/PASSWORD')
                
                else:
                    if user[0]=='Admin':
                        self.root.destroy()
                        os.system('python dashboard.py')
                    else:
                        self.root.destroy()
                        os.system('python billing.py')

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def forget_password(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.employee_id.get()=='':
                messagebox.showerror('Error','Employee Id must be required', parent= self.root)
            
            else:
                cur.execute('select email from employee where eid=%s', (self.employee_id.get(),))
                email = cur.fetchone()
                if email==None:
                    messagebox.showerror('Error', 'Invalid Employee ID, try again!', parent=self.root)
                else:

                    #=================forget window==================
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_confirm_password=StringVar()
                    #call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror('Error', 'Connection Error,try again',parent=self.root)
                    
                    
                    else:
                        self.forget_window=Toplevel(self.root)
                        self.forget_window.title('RESET PASSWORD')
                        self.forget_window.geometry('400x350+500+100')
                        self.forget_window.focus_force()
                        
                        
                        title=Label(self.forget_window, text='Reset Password', font=('goudy old style', 15, 'bold'), bg='#FFD4B2').pack(side=TOP, fill=X)
                        lbl_reset=Label(self.forget_window, text="Enter OTP send on Registered Email", font=('times new roman', 13)).place(x=20, y=60)
                        txt_reset=Entry(self.forget_window, textvariable=self.var_otp, font=('times new roman', 13), bg='lightyellow').place(x=20,y=100, width=250, height=30)

                        new_pass=Label(self.forget_window, text='New Password', font=('goudy old style', 15, 'bold')).place(x=20, y=160)
                        txt_new_pass=Entry(self.forget_window, textvariable=self.var_new_password, font=('times new roman', 13), bg='lightyellow').place(x=20,y=190, width=250, height=30)

                        confirm_pass=Label(self.forget_window, text='Confirm Password', font=('goudy old style', 15, 'bold')).place(x=20, y=225)
                        txt_confirm_pass=Entry(self.forget_window, textvariable=self.var_confirm_password, font=('times new roman', 13), bg='lightyellow').place(x=20,y=255, width=250, height=30)

                        self.btn_reset=Button(self.forget_window, text='Submit', command=self.validate_otp, font=('times new roman', 13), bg='#82AAE3')
                        self.btn_reset.place(x=280, y=100,width=100, height=30)

                        self.btn_update=Button(self.forget_window, text='Update', command=self.update_password, state=DISABLED, font=('times new roman', 13), bg='#FF8E9E')
                        self.btn_update.place(x=150, y=300,width=100, height=30)

                                      

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')

    def update_password(self):
        if self.var_new_password.get()=='' or self.var_confirm_password.get()=='':
            messagebox.showerror('Error', 'Password is required', parent=self.forget_window)

        elif self.var_new_password.get() != self.var_confirm_password.get():
            messagebox.showerror('Error', 'New Password and Confirm Password must be same', parent=self.forget_window)
        else:
            con=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'IMS'
            )
            cur = con.cursor()
            try:
                cur.execute('update employee set pass=%s where eid=%s', (self.var_new_password.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo('Success', 'Password Update Successfully', parent=self.forget_window)
                self.forget_window.destroy()
            except Exception as ex: 
                messagebox.showerror('Error', f'Error due to : {str(ex)}')




    def validate_otp(self):
        if int(self.mail_otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        
        else:
            messagebox.showerror('Error', 'Invalid OTP, Try again', parent=self.forget_window)


    def send_email(self, to_):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_ = email_password.email_
        password_ = email_password.pass_

        s.login(email_, password_)
        self.mail_otp= int(time.strftime('%H%M%S')) + int(time.strftime('%S')) 

        subject='MyCart - Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.mail_otp)}.\n\nWith Regards, \nMyCart Team'
        msg='Subject:{}\n\n{}'.format(subject, msg)
        
        s.sendmail(email_, to_, msg)
        chk=s.ehlo()             #if chk== 250 --- email send successfully
        
        if chk[0]==250:
           
            return 's'
        else:
            return 'f'

        












root = Tk()
obj= Login_System(root)
root.mainloop()
    