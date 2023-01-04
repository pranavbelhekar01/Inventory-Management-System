import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import time
import os
import tempfile
class billclass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1370x700+0+0')
        self.root.title('Inventory Management system | Developed by Pranav')
        self.root.config(bg='ivory2')
        self.cart_list=[]
        self.chk_print=0

        # =========== Title ============
        self.icon_title=PhotoImage(file='photos\store.png')
        title = Label(self.root, text='Inventory Management System',image=self.icon_title, compound=RIGHT,font=('times new roman', 40, 'bold'),bg='dark turquoise', anchor='w',padx='40').place(x=0,y=0,relwidth=1,height=70)
        self.button_img = PhotoImage(file='photos\logout_button.png')
        # main_button = Button(self.root,image = self.button_img, command=RAISED, font=('times new roman', 15, 'bold'), bg="gold2", borderwidth=0).place(x=1100,y=10, height=50,width=150)
        main_button = Button(self.root,text='Logout', command=self.logout, font=('times new roman', 15, 'bold'), bg="gold2", borderwidth=3, cursor='hand2').place(x=1100,y=10, height=50,width=150)

        # ============ clock ==============
        self.lbl_clock = Label(self.root, text='Welcome to Inventory Management System\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS',font=('times new roman', 15,'bold'),bg='light cyan',padx='40')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        #============= Product Frame ============

        self.var_search=StringVar()
        productFrame1= Frame(self.root,bd=4, relief=RIDGE, bg='#F1F7B5')
        productFrame1.place(x=6, y=110, width=410, height=528)

        pTitle= Label(productFrame1, text="All Products", font=('goudy old style', 20, 'bold'), bg='#3C2A21', fg='white').pack(side=TOP, fill=X)

        productFrame2= Frame(productFrame1,bd=4, relief=RIDGE, bg='#CEEDC7')
        productFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search=Label(productFrame2, text='Search Product | By Name ', font=('goudy old style', 15, 'bold'), bg='#CEEDC7', fg='#1A120B').place(x=2, y=5)

        lbl_search= Label(productFrame2, text='Product Name', font=('goudy old style', 15, 'bold'), bg='#CEEDC7', fg='#3C2A21').place(x=5, y=45)
        txt_search= Entry(productFrame2, textvariable=self.var_search, font=('goudy old style', 15, 'bold'), bg='#D5CEA3', fg='#3C2A21').place(x=132, y=47, width=150, height=22)

        btn_search=Button(productFrame2, text='Search',command=self.search, font=('goud old style', 15), bg='green', fg='white', cursor='hand2').place(x=292, y=45, width=80, height=25)
        btn_show_all=Button(productFrame2, text='Show All',command=self.show, font=('goud old style', 14), bg='blue', fg='white', cursor='hand2').place(x=292, y=10, width=80, height=25)


        #==================== product frames ==============
        cart_frame=Frame(productFrame1, bd=3, relief=RIDGE)
        cart_frame.place(x=2,y=140,width=398, height=350)
        
        scrolly = Scrollbar(cart_frame,orient=VERTICAL)
        scrollx = Scrollbar(cart_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(cart_frame, columns= ('pid','name','price','quantity', 'status'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading('pid', text='Product ID')
        self.productTable.heading('name', text='Name')
        self.productTable.heading('price', text='Price')
        self.productTable.heading('quantity', text='Quantity')
        self.productTable.heading('status', text='Status')
        self.productTable['show'] = 'headings'

        self.productTable.column('pid', width=90)
        self.productTable.column('name', width=100)
        self.productTable.column('price', width=100)
        self.productTable.column('quantity', width=100)
        self.productTable.column('status', width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind('<ButtonRelease-1>', self.get_data)
        lbl_note= Label(productFrame1, text='Note: Enter 0 Quantity to remove product from the Cart', font=('goudy old style', 10), bg='#F1F7B5', fg='red').pack(side=BOTTOM, fill=X)

        #self.show()


        #==============================================Customer Frame=======================================

        self.var_name=StringVar()
        self.var_contact=StringVar()
        customerFrame= Frame(self.root,bd=4, relief=RIDGE, bg='#F1F7B5')
        customerFrame.place(x=420, y=110, width=530, height=70)
        
        cTitle= Label(customerFrame, text="Customer Details", font=('goudy old style', 14, 'bold'), bg='#3C2A21', fg='white').pack(side=TOP, fill=X)

        lbl_name= Label(customerFrame, text='Name', font=('goudy old style', 12, 'bold'), bg='#F1F7B5', fg='#3C2A21').place(x=5, y=35)
        txt_name= Entry(customerFrame, textvariable=self.var_name, font=('goudy old style', 12), bg='#D5CEA3', fg='#3C2A21').place(x=60, y=35, width=150)

        lbl_contact= Label(customerFrame, text='Contact No.', font=('goudy old style', 12, 'bold'), bg='#F1F7B5', fg='#3C2A21').place(x=270, y=35)
        txt_contact= Entry(customerFrame, textvariable=self.var_contact, font=('goudy old style', 12), bg='#D5CEA3', fg='#3C2A21').place(x=380, y=35, width=140)


        #============calculator cart frame==================
        cal_cart_frame= Frame(self.root,bd=2, relief=RIDGE, bg='#F1F7B5')
        cal_cart_frame.place(x=420, y=190, width=530, height=360)

        #=============calculator Frame===============

        self.var_cal_input=StringVar()
        cal_frame= Frame(cal_cart_frame,bd=2, relief=RIDGE, bg='#F1F7B5')
        cal_frame.place(x=5, y=10, width=260, height=340)

        txt_cal_input=Entry(cal_frame, textvariable=self.var_cal_input, font=('arial', 15, 'bold'), width=21, bd=10, relief=GROOVE, bg='#F3EFE0', state='readonly', justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=4)

        btn_7=Button(cal_frame, text='7', command=lambda:self.get_input(7), font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=1, column=0)
        btn_8=Button(cal_frame, text='8', command=lambda:self.get_input(8),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=1, column=1)
        btn_9=Button(cal_frame, text='9', command=lambda:self.get_input(9),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=1, column=2)
        btn_plus=Button(cal_frame, text='+', command=lambda:self.get_input('+'),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=1, column=3)

        btn_4=Button(cal_frame, text='4', command=lambda:self.get_input(4),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=2, column=0)
        btn_5=Button(cal_frame, text='5', command=lambda:self.get_input(5),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=2, column=1)
        btn_6=Button(cal_frame, text='6', command=lambda:self.get_input(6),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=2, column=2)
        btn_subtract=Button(cal_frame, text='-', command=lambda:self.get_input('-'),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=2, column=3)

        btn_1=Button(cal_frame, text='1', command=lambda:self.get_input(1),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=3, column=0)
        btn_2=Button(cal_frame, text='2', command=lambda:self.get_input(2),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=3, column=1)
        btn_3=Button(cal_frame, text='3', command=lambda:self.get_input(3),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=3, column=2)
        btn_multiply=Button(cal_frame, text='*', command=lambda:self.get_input('*'),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=3, column=3)

        btn_0=Button(cal_frame, text='0', command=lambda:self.get_input(0),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#FAEAB1').grid(row=4, column=0)
        btn_c=Button(cal_frame, text='C', command=self.clear_cal, font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=4, column=1)
        btn_equal=Button(cal_frame, text='=',command=self.perform_cal, font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=4, column=2)
        btn_divide=Button(cal_frame, text='/', command=lambda:self.get_input('/'),  font=('arial', 14, 'bold'), bd=5, width=4, pady=15, cursor='hand2', bg='#D0B8A8').grid(row=4, column=3)





        
        
        #==================== cart frame ==============
        cart_frame=Frame(cal_cart_frame, bd=3, relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245, height=342)
        self.carTitle= Label(cart_frame, text="Cart\tTotal Product:   0 ", font=('goudy old style', 14, 'bold'), bg='#3C2A21', fg='white')
        self.carTitle.pack(side=TOP, fill=X)

        
        scrolly = Scrollbar(cart_frame,orient=VERTICAL)
        scrollx = Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cartTable=ttk.Treeview(cart_frame, columns= ('pid','name','price','quantity'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        self.cartTable.heading('pid', text='Product ID')
        self.cartTable.heading('name', text='Name')
        self.cartTable.heading('price', text='Price')
        self.cartTable.heading('quantity', text='Quantity')
        self.cartTable['show'] = 'headings'

        self.cartTable.column('pid', width=70)
        self.cartTable.column('name', width=100)
        self.cartTable.column('price', width=90)
        self.cartTable.column('quantity', width=70)
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind('<ButtonRelease-1>', self.get_data_cart)


        #================= Add Widgets Buttons ==================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_stock=StringVar()
        Add_cartWidgetsFrame= Frame(self.root,bd=2, relief=RIDGE, bg='#F1F7B5')
        Add_cartWidgetsFrame.place(x=420, y=550, width=530, height=88)


        lbl_p_name=Label(Add_cartWidgetsFrame, text='Product Name', font=('goudy old style', 11), bg = '#F1F7B5').place(x=5, y=2)
        txt_p_name=Entry(Add_cartWidgetsFrame, textvariable=self.var_pname, font=('goudy old style', 11), bg = '#D5CEA3', state='readonly').place(x=5, y=30, width=150, height=22)

        lbl_p_price=Label(Add_cartWidgetsFrame, text='Price Per Qty', font=('goudy old style', 11), bg = '#F1F7B5').place(x=180, y=2)
        txt_p_price=Entry(Add_cartWidgetsFrame, textvariable=self.var_price, font=('goudy old style', 11), bg = '#D5CEA3', state='readonly').place(x=180, y=30, width=150, height=22)

        lbl_p_qty=Label(Add_cartWidgetsFrame, text='Quantity', font=('goudy old style', 11), bg = '#F1F7B5').place(x=360, y=2)
        txt_p_qty=Entry(Add_cartWidgetsFrame, textvariable=self.var_quantity, font=('goudy old style', 11), bg = '#D5CEA3').place(x=360, y=30, width=150, height=22)

        self.lbl_instock=Label(Add_cartWidgetsFrame, text='In Stock ', font=('goudy old style', 11), bg = '#F1F7B5')
        self.lbl_instock.place(x=5, y=56)

        btn_clear_cart=Button(Add_cartWidgetsFrame, text='Clear', command=self.clear_cart, font=('goud old style', 15), bg='#227C70', fg='white', cursor='hand2').place(x=180, y=56, width=150, height=25)
        btn_add_cart=Button(Add_cartWidgetsFrame, text='Add | Update Cart', command=self.add_update_cart, font=('goud old style', 14), bg='#C58940', fg='white', cursor='hand2').place(x=340, y=56, width=180, height=25)



        #================================Billing Area================================

        billFrame=Frame(self.root,bd=2, relief=RIDGE, bg='#F1F7B5')
        billFrame.place(x=954, y=110, width=310, height=410)

        bTitle= Label(billFrame, text="Customer Bill Area", font=('goudy old style', 14, 'bold'), bg='#3C2A21', fg='white').pack(side=TOP, fill=X)

        scrolly=Scrollbar(billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_bill_area=Text(billFrame)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)


        #===============================billing buttons====================
        billMenuFrame=Frame(self.root,bd=2, relief=RIDGE, bg='#F1F7B5')
        billMenuFrame.place(x=954, y=520, width=310, height=118)

        self.lbl_amount= Label(billMenuFrame,text='Bill Amount\n0.0', font=('goudy old style', 14), bg = '#1C315E',fg='white')
        self.lbl_amount.place(x=2, y=5, width=100,height=60)

        self.lbl_discount= Label(billMenuFrame,text='Discount\n5%', font=('goudy old style', 14), bg = '#227C70',fg='white')
        self.lbl_discount.place(x=104, y=5, width=100,height=60)

        self.lbl_net_pay= Label(billMenuFrame,text='Net Pay\n0.0', font=('goudy old style', 14), bg = '#D09CFA',fg='white')
        self.lbl_net_pay.place(x=206, y=5, width=100,height=60)

        btn_print=Button(billMenuFrame, text='Print', command=self.print_bill, font=('goud old style', 13), bg='#FF7000', fg='white', cursor='hand2')
        btn_print.place(x=2, y=70, width=100, height=40)
        btn_clear_all=Button(billMenuFrame, text='Clear All', command=self.clear_all, font=('goud old style', 13), bg='#10A19D', fg='white', cursor='hand2')
        btn_clear_all.place(x=104, y=70, width=100, height=40)
        btn_generate=Button(billMenuFrame, text='Generate\n Bill', command=self.generate_bill, font=('goud old style', 13), bg='#540375', fg='white', cursor='hand2')
        btn_generate.place(x=206, y=70, width=100, height=40)


        self.show() 
        self.update_date_time()
        

#=================================================All Functions==================================================================

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    

    def show(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            cur.execute("select pid, name, price, quantity, status  from product where status = 'Active'")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def search(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_search.get() =='':
                messagebox.showerror('Error', 'Search input is required', parent=self.root)
            else:
                cur.execute("select pid,Name,price,quantity, status from product where Name LIKE '%"+self.var_search.get()+"%' and status = 'Active'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END, values=row)
                else:
                    messagebox.showerror('Error', 'No Record Found', parent=self.root)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')

    def get_data(self,ev):
        f=self.productTable.focus()
        content= (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f'In Stock [ {str(row[3])} ]')
        self.var_stock.set(row[3])
        self.var_quantity.set('1')
    

    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content= (self.cartTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f'In Stock [ {str(row[4])} ]')
        self.var_stock.set(row[4])
        self.var_quantity.set(row[3])
        


    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error', 'Please select Product from the Product List', parent=self.root)

        elif self.var_quantity.get()=='':
            messagebox.showerror('Error', 'Quantity is Required', parent=self.root)
        
        elif int(self.var_quantity.get()) > int(self.var_stock.get()):
            messagebox.showerror('Error', 'No Sufficient Quantity available in stock', parent=self.root)

        else:
            #price_cal=float(int(self.var_quantity.get())*float(self.var_price.get()))

            price_cal=self.var_price.get()

            
            # print(self.cart_list)

            #================ update cart ============
            present='no'
            index_= 0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_ += 1
            if present=='yes':
                op = messagebox.askyesno("confirm",'Product already present \nDo you want to Update | Remove from the cart list', parent=self.root)
                if op == True:
                    if self.var_quantity.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]= price_cal  #price
                        self.cart_list[index_][3]= self.var_quantity.get() #quantity
            else:
                cart_data=[self.var_pid.get(), self.var_pname.get(), price_cal, self.var_quantity.get(), self.var_stock.get()]
                self.cart_list.append(cart_data)

            self.show_cart()
            self.bill_updates()
    

    def bill_updates(self):
        self.bill_amount=0
        self.net_pay=0
        self.discount=0

        for row in self.cart_list:
            self.bill_amount = self.bill_amount + ((float(row[2])) * int(row[3]))

        self.discount=(self.bill_amount * 5)/100
        self.net_pay = self.bill_amount - self.discount   # discounted amount

        self.lbl_amount.config(text=f'Bill Amount\n{str(self.bill_amount)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.carTitle.config(text=f'Cart\tTotal Product:   {str(len(self.cart_list))} ')


                

    
    def show_cart(self):
        try:
            
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')



    def generate_bill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror('Error', 'Customer Details are required!', parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror('Error', 'Please add product to cart', parent=self.root)
        else:
            #============== Bill Top =================
            self.bill_top()
            #============== Bill Middle ==============
            self.bill_middle()
            #============== Bill bottom ==============
            self.bill_bottom()


            file = open(f'bill/{str(self.invoice)}.txt', 'w')
            file.write(self.txt_bill_area.get('1.0',END))
            file.close()

            messagebox.showinfo('Saved', 'Bill has been generated', parent=self.root)

            self.chk_print=1
            
    
    def bill_top(self):
        self.invoice = int(time.strftime('%H%M%S')) + int(time.strftime('%d%m%Y'))    #to give bill number and to generate unique number
        bill_top_temp=f"""
\t  My Cart Inventory

 Phone No. 98343*****  Pune-411033
{str('='*35)}
 Customer Name: {self.var_name.get()}
 Ph no.: {self.var_contact.get()}
 Bill No.: {str(self.invoice)}\t\tDate:{str(time.strftime('%d%m%Y'))}
{str('='*35)}
 Product Name\t\tQuantity\tPrice(Rs.)
                           
{str('='*35)}
        
        """
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)
    

    def bill_bottom(self):
        bill_bottom_temp=f"""
{str('='*35)}
 Bill Amount\t\t\t {self.bill_amount}
 Discount\t\t\t {self.discount}
 Net Pay\t\t\t {self.net_pay}
{str('='*35)}\n 
        """
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            
            for row in self.cart_list:
                
                pid = row[0]
                name=row[1]
                quantity= int(row[4]) - int(row[3])
                if int(row[3]) == int(row[4]):
                    status='Inactive'
                if int(row[3]) != int(row[4]):
                    status='Active'

                price=str(float(row[2]*int(row[3])))
                self.txt_bill_area.insert(END,'\n '+name+'\t\t   '+row[3]+'\t '+price)

                #========update Quantiy in product table==========
                cur.execute('update product set quantity=%s, status=%s where pid=%s',(
                quantity,
                status,
                pid
                ))
                con.commit()
            con.close()
            self.show()
        
        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')




    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.lbl_instock.config(text=f'In Stock')
        self.var_stock.set('')
    

    def clear_all(self):
        del self.cart_list[:]
        self.var_name.set('')
        self.var_contact.set('')
        self.var_search.set('')
        self.txt_bill_area.delete('1.0', END)
        self.clear_cart()
        self.show()
        self.show_cart()
        self.carTitle.config(text=f'Cart\tTotal Product: 0 ')
        self.chk_print=0

    def update_date_time(self):
        time_ = time.strftime('%I:%M:%S')
        date_ = time.strftime('%d-%m-%Y')
        self.lbl_clock.config(text=f'Welcome to Inventory Management System\t\t Date: {str(date_)} \t\t Time: {str(time_)}')
        self.lbl_clock.after(200, self.update_date_time)


    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print', 'Please wait while printing', parent=self.root)


            new_file = tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file,'print')


        else:
            messagebox.showerror('Print', 'Please generate bill to print receipt', parent=self.root)
        

    def logout(self):
        self.root.destroy()
        os.system('python login.py')


            





if __name__ == '__main__':
    root = Tk()
    obj=billclass(root)
    root.mainloop()