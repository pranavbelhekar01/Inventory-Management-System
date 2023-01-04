import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1070x500+200+130')
        self.root.title('Inventory Management System | Developed By Rangesh')
        self.root.config(bg='sandy brown')
        self.root.focus_force()


        #========================================
        #============variables=========
        self.var_pid = StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()



        #=========Frame================

        product_frame = Frame(self.root, bd=2, relief=RIDGE, bg='#00ABB3')
        product_frame.place(x=10, y=10, width=450, height=480)


        #===============column1===============
        title = Label(product_frame, text='Manage Product Details', font=('groudy old style', 18), bg='#6C4AB6', fg= 'black').pack(side=TOP, fill=X)

        lbl_category = Label(product_frame, text='Category', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=60)
        lbl_supplier = Label(product_frame, text='Supplier', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=110)
        lbl_product = Label(product_frame, text='Name', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=160)
        lbl_price = Label(product_frame, text='Price', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=210)
        lbl_quantity = Label(product_frame, text='Quantity', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=260)
        lbl_status = Label(product_frame, text='Status', font=('groudy old style', 15), bg='#00ABB3', fg= 'white').place(x=30,y=310)

        #============column2=================
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat, values=self.cat_list, state='readonly',justify=CENTER, font=('goudy old style', 12), background='#CEEDC7')
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup, values=self.sup_list, state='readonly',justify=CENTER, font=('goudy old style', 12), background='#CEEDC7')
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name, font=('goudy old style', 12), bg='#B2B2B2').place(x=150, y=160, width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price, font=('goudy old style', 12), bg='#B2B2B2').place(x=150, y=210, width=200)
        txt_quantity=Entry(product_frame,textvariable=self.var_quantity, font=('goudy old style', 12), bg='#B2B2B2').place(x=150, y=260, width=200)

        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status, values=('Active', 'Inactive'), state='readonly',justify=CENTER, font=('goudy old style', 12), background='#CEEDC7')
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)
        

        #=======buttons=======
        btn_add=Button(product_frame, text='Save', command=self.add, font=('goudy old style', 12), bg='#227C70', fg= 'white', cursor='hand2').place(x=10, y=400, width=100, height=40)
        btn_update=Button(product_frame, text='Update', command=self.update, font=('goudy old style', 12), bg='#82C3EC', fg= 'white', cursor='hand2').place(x=120, y=400, width=100, height=40)
        btn_delete=Button(product_frame, text='Delete', command=self.delete, font=('goudy old style', 12), bg='#DC0000', fg= 'white', cursor='hand2').place(x=230, y=400, width=100, height=40)
        btn_clear=Button(product_frame, text='Clear', command=self.clear, font=('goudy old style', 12), bg='#1A120B', fg= 'white', cursor='hand2').place(x=340, y=400, width=100, height=40)

        # ==========Search Frame============
        SearchFrame = LabelFrame(self.root, text='Search Employee', bg='#FFF6BD', font=('goudy old style',12,'bold'), bd=2, relief=RIDGE)
        SearchFrame.place(x = 480, y = 10, width = 570, height=70)

        # ==========Options==================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=('Select', 'Category','Supplier','Name'), state='readonly',justify=CENTER, font=('goudy old style', 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0) # to display select word by default as selected value
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt, font=('goudy old style', 12), bg='#CEEDC7').place(x=200, y=10, width=200)
        btn_search=Button(SearchFrame, text='Search', command= self.search, font=('goudy old style', 12), bg='#3A4F7A', fg= 'white', cursor='hand2').place(x=410, y=6, width=150, height=30)




        #====================Product Details==============
        pro_frame=Frame(self.root, bd=3, relief=RIDGE)
        pro_frame.place(x=480,y=100, width= 570, height=300)
        
        scrolly = Scrollbar(pro_frame,orient=VERTICAL)
        scrollx = Scrollbar(pro_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(pro_frame, columns= ('pid','Category','Supplier','Name', 'price','quantity', 'status'), yscrollcommand=scrolly.set, xscrollcommand=scrolly.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=LEFT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading('pid', text='Product ID')
        self.productTable.heading('Category', text='Category')
        self.productTable.heading('Supplier', text='Supplier')
        self.productTable.heading('Name', text='Name')
        self.productTable.heading('price', text='Price')
        self.productTable.heading('quantity', text='Quatity')
        self.productTable.heading('status', text='Status')
        self.productTable['show'] = 'headings'

        self.productTable.column('pid', width=90)
        self.productTable.column('Category', width=100)
        self.productTable.column('Supplier', width=100)
        self.productTable.column('Name', width=100)
        self.productTable.column('price', width=100)
        self.productTable.column('quantity', width=100)
        self.productTable.column('status', width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind('<ButtonRelease-1>', self.get_data)

        self.show()

        self.fetch_cat_sup()

        

       
#======================================================================================================
    def fetch_cat_sup(self):
        self.cat_list.append('Empty') 
        self.sup_list.append('Empty')
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            cur.execute('select name from category') 
            cat = cur.fetchall()                                # this gives us a tuple [(a,), (b,)]
                                                                        # |
            if len(cat)>0:                                              # V
                del self.cat_list[:]                            # this gives us list [a, b] to pass it for drop down menu
                self.cat_list.append('Select')                          
                for i in cat:                       
                    self.cat_list.append(i[0])  
                 
            
            

            cur.execute('select name from supplier') 
            sup = cur.fetchall()
            if len(sup)>0:   
                                                                        
                del self.sup_list[:]                            # this gives us list [a, b] to pass it for drop down menu
                self.sup_list.append('Select')                          
                for i in sup:                       
                    self.sup_list.append(i[0])
            


        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def add(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        
        cur = con.cursor()
    

        try:
            if self.var_cat.get()=='Select' or self.var_cat.get()=='Empty' or self.var_sup.get()=='Select' or self.var_name.get()=='':
                messagebox.showerror('Error', 'All fields are required required', parent=self.root)
            else:
                cur.execute('select * from product where Name = %s ', (self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Product already present, try Different Product')
                
                else:
                    cur.execute('insert into product(Category,Supplier,Name, price,quantity, status) values(%s,%s,%s,%s,%s,%s)', \
                        (self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Product added Successfully', parent=self.root)
                    self.show()
    
        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def show(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            cur.execute('select * from product')
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def get_data(self,ev):
        f=self.productTable.focus()
        content= (self.productTable.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_pid.get()=='':
                messagebox.showerror('Error', 'Please select product from list', parent=self.root)
            else:
                cur.execute('select * from product where pid =%s ', (self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Product ID')
                
                else:
                    cur.execute('update product set Category=%s,Supplier=%s,Name=%s, price=%s,quantity=%s, status=%s where pid=%s', (
                        
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Employee Updated Successfully', parent=self.root)
                    self.show()
    
        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')
    

    def delete(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_pid.get()=='':
                messagebox.showerror('Error', 'Select Product From list', parent=self.root)
            else:
                cur.execute('select * from product where pid =%s ', (self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Product')
                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op==True:
                        cur.execute('delete from product where pid=%s', (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Product Deleted Successfully', parent=self.root)
                        self.clear()

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')



    def clear(self):
        self.var_cat.set('Select')
        self.var_sup.set('Select')
        self.var_name.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.var_status.set('Active')
        self.var_pid.set('')
        
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
        self.show()
    
    def search(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_searchby.get() == 'Select':
                messagebox.showerror('Error', 'Select By option', parent=self.root)
            elif self.var_searchtxt.get() =='':
                messagebox.showerror('Error', 'Search input is required', parent=self.root)
            else:
                cur.execute('select * from product where ' + self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END, values=row)
                else:
                    messagebox.showerror('Error', 'No Record Found', parent=self.root)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


        






if __name__ == '__main__':
    root = Tk()
    obj=productclass(root)
    root.mainloop()