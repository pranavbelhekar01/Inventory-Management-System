import mysql.connector
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
from employee import employeeclass
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sale import salesclass
import os
import time

class IMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1370x700+0+0')
        self.root.title('Inventory Management system | Developed by Pranav')
        self.root.config(bg='#FFEBB7')
        #====== Background Image ======
        # self.bg_img = ImageTk.PhotoImage(Image.open('photos\store.png'))
        # self.frame=Frame(self.root, width=1200, height=800)
        # self.frame.pack(fill=X)
        
        # label=Label(self.root, image=self.bg_img)
        self.bg_1 = ImageTk.PhotoImage(file='photos/darshboard_bg.png')
        frame_label = Label(self.root, image=self.bg_1, bd_=0).place(x=4, y=4, relheight=1, relwidth=1)

        
        # =========== Title ============
        self.icon_title=PhotoImage(file='photos\store.png')
        title = Label(self.root, text='Inventory Management System',compound=RIGHT,font=('times new roman', 40, 'bold'),bg='#2B3467', anchor='w',padx='40', fg='#EFF5F5').place(x=0,y=0,relwidth=1,height=70)
        self.button_img = PhotoImage(file='photos\logout_button.png')
        # main_button = Button(self.root,image = self.button_img, command=RAISED, font=('times new roman', 15, 'bold'), bg="gold2", borderwidth=0).place(x=1100,y=10, height=50,width=150)
        main_button = Button(self.root,text='Logout', command=self.logout, font=('times new roman', 15, 'bold'), bg="#FF7000", borderwidth=3, cursor='hand2').place(x=1100,y=10, height=50,width=150)

        # ============ clock ==============
        self.lbl_clock = Label(self.root, text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS',font=('times new roman', 15,'bold'),bg='#F8F988',padx='40')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        # ============ Left Menu =============
            #resizing and inserting image
        self.MenuLogo=Image.open('photos\woman.png')
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg='#A5F1E9')
        LeftMenu.place(x=0,  y=98, width=200, height=565)

            
        lbl_menulogo= Label(LeftMenu, image=self.MenuLogo, border=0)
        lbl_menulogo.pack(side=TOP, fill=X) # fill sets the image according to the frame size
            # Label Menu                        
        label_menu = Label(LeftMenu,text='Menu', font=('times new roman', 15, 'bold'), bg="gold2").pack(side=TOP, fill=X)
            # buttons
        self.icon_side=Image.open('photos\icon.png')
        self.icon_side=self.icon_side.resize((40,40),Image.ANTIALIAS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        btn_employee = Button(LeftMenu,text='Employee', command=self.employee, compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu,text='Supplier', command=self.supplier, compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu,text='Category', command=self.category, compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu,text='Product', command=self.product, compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu,text='Sales',command=self.sales, compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu,text='Exit', compound=LEFT,image=self.icon_side, font=('times new roman', 15, 'bold'), bg="#EB6440", borderwidth=3, cursor='hand2',padx=20, anchor='w').pack(side=TOP, fill=X)
        
        # ====== Content ======
        self.im1 = ImageTk.PhotoImage(file='photos/red_frame.png')
        frame_label = Label(self.root, image=self.im1, bd_=0).place(x=290, y=130)

        self.im2 = ImageTk.PhotoImage(file='photos/yellow_frame.png')
        frame_label = Label(self.root, image=self.im2, bd_=0).place(x=590, y=130)

        self.im3 = ImageTk.PhotoImage(file='photos/blue_frame.png')
        frame_label = Label(self.root, image=self.im3, bd_=0).place(x=290, y=280)
        
  

        self.im4 = ImageTk.PhotoImage(file='photos/dark_blue_frame.png')
        frame_label = Label(self.root, image=self.im4, bd_=0).place(x=590, y=280)

        self.im5 = ImageTk.PhotoImage(file='photos/dark_yellow_frame.png')
        frame_label = Label(self.root, image=self.im5, bd_=0).place(x=290, y=430)


        self.lbl_employee=Label(self.root, text='Total Employee\n[0]', bg='#EB4550', fg='black', font=('times new roman', 15,'bold'), borderwidth=0, relief=RIDGE)
        self.lbl_employee.place(x=300, y=140, height=100, width=200)

        self.lbl_supplier=Label(self.root, text='Total Supplier\n[0]', bg='#FCFFE7', fg='black', font=('times new roman', 15,'bold'), borderwidth=0, relief=RIDGE)
        self.lbl_supplier.place(x=600, y=140, height=100, width=200)

        self.lbl_category=Label(self.root, text='Total Category\n[0]', bg='#3E6D9C', fg='black', font=('times new roman', 15,'bold'), borderwidth=0, relief=RIDGE)
        self.lbl_category.place(x=300, y=290, height=100, width=200)

        self.lbl_product=Label(self.root, text='Total Product\n[0]', bg='#2B3467', fg='black', font=('times new roman', 15,'bold'), borderwidth=0, relief=RIDGE)
        self.lbl_product.place(x=600, y=290, height=100, width=200)

        self.lbl_sales=Label(self.root, text='Total Sales\n[0]', bg='#FFDB89', fg='black', font=('times new roman', 15,'bold'), borderwidth=0, relief=RIDGE)
        self.lbl_sales.place(x=300, y=440, height=100, width=200)
        
        self.update_content()
# =============================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)

    def update_content(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        
        cur = con.cursor()
        try:
            cur.execute('select * from product')
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')

            cur.execute('select * from supplier')
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute('select * from category')
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute('select * from employee')
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')

            sale_bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(sale_bill)}]')

           
            time_ = time.strftime('%I:%M:%S')
            date_ = time.strftime('%d-%m-%Y')
            self.lbl_clock.config(text=f'Welcome to Inventory Management System\t\t Date: {str(date_)} \t\t Time: {str(time_)}')
            self.lbl_clock.after(200, self.update_content)



        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')

    
    def logout(self):
        self.root.destroy()
        os.system('python login.py')




 



if __name__ == '__main__':
    root = Tk()
    obj=IMS(root)
    root.mainloop()
# created by Pranav Belhekar
