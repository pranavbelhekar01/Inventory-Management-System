import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
class supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1070x500+200+130')
        self.root.title('Inventory Management System | Developed By Rangesh')
        self.root.config(bg='sandy brown')
        self.root.focus_force()


        #==================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.supplier_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_description = StringVar()


        # ==========Options==================
        lbl_search=Label(self.root,text='Search by Invoice No.', font=('goudy old style', 12), bg = 'sandy brown')
        lbl_search.place(x=680, y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt, font=('goudy old style', 12), bg='#CEEDC7').place(x=850, y=80, width=200)
        btn_search=Button(self.root, text='Search', command= self.search, font=('goudy old style', 12), bg='#3A4F7A', fg= 'white', cursor='hand2').place(x=410, y=6, width=150, height=30)
        

        #============= title =============
        title = Label(self.root, text='Supplier Details', font=('groudy old style', 18, 'bold'), bg='#82AAE3', fg= 'black').place(x=50, y=10, width=1000, height=40)

        #=============content=============

        #======row1==========
        lbl_supplier_invoice = Label(self.root, text='Invoice No.', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.supplier_invoice, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=180, y=80, width=180)
        
        #========row2=========
        lbl_name = Label(self.root, text='Name', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=180, y=120, width=180)
    
        #=========row3========
        lbl_contact = Label(self.root, text='Contact', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black').place(x=180, y=160, width=180)

        #==========rowtxt4============
        lbl_description = Label(self.root, text='description', font=('groudy old style', 12), bg='sandy brown', fg= 'black').place(x=50, y=200)
        self.txt_description = Text(self.root, font=('groudy old style', 12), bg='#CEEDC7', fg= 'black')
        self.txt_description.place(x=180, y=200, width=300, height=60)


        #=======buttons=======
        btn_add=Button(self.root, text='Save', command=self.add, font=('goudy old style', 12), bg='#227C70', fg= 'white', cursor='hand2').place(x=180, y=300, width=100, height=30)
        btn_update=Button(self.root, text='Update', command=self.update, font=('goudy old style', 12), bg='#82C3EC', fg= 'white', cursor='hand2').place(x=290, y=300, width=100, height=30)
        btn_delete=Button(self.root, text='Delete',command=self.delete, font=('goudy old style', 12), bg='#DC0000', fg= 'white', cursor='hand2').place(x=400, y=300, width=100, height=30)
        btn_clear=Button(self.root, text='Clear', command=self.clear, font=('goudy old style', 12), bg='#1A120B', fg= 'white', cursor='hand2').place(x=510, y=300, width=100, height=30)
       
        #====================Supplier Details==============
        supplier_frame=Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=680,y=120,width=380, height=350)
        
        scrolly = Scrollbar(supplier_frame,orient=VERTICAL)
        scrollx = Scrollbar(supplier_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(supplier_frame, columns= ('invoice','name','contact','description'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=LEFT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading('invoice', text='Invoice No.')
        self.supplierTable.heading('name', text='Name')
        self.supplierTable.heading('contact', text='Contact')
        self.supplierTable.heading('description', text='description')
        self.supplierTable['show'] = 'headings'

        self.supplierTable.column('invoice', width=90)
        self.supplierTable.column('name', width=100)
        self.supplierTable.column('contact', width=100)
        self.supplierTable.column('description', width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind('<ButtonRelease-1>', self.get_data)

        self.show()

#======================================================================================================
    def add(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.supplier_invoice.get()=='':
                messagebox.showerror('Error', 'Invoice must be required', parent=self.root)
            else:
                cur.execute('select * from supplier where invoice =%s ', (self.supplier_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'This Invoice Number already assigned, try Different ID')
                
                else:
                    cur.execute('insert into supplier(invoice,name,contact,description) values(%s,%s,%s,%s)', \
                        (self.supplier_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0', END),
    
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Supplier added Successfully', parent=self.root)
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
            cur.execute('select * from supplier')
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')


    def get_data(self,ev):
        f=self.supplierTable.focus()
        content= (self.supplierTable.item(f))
        row = content['values']
        self.supplier_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])

    def update(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.supplier_invoice.get()=='':
                messagebox.showerror('Error', 'Invoice Number must be required', parent=self.root)
            else:
                cur.execute('select * from supplier where invoice =%s ', (self.supplier_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Invoice Number')
                
                else:
                    cur.execute('update supplier set name=%s, contact=%s, description=%s where invoice=%s', (
                        
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_description.get('1.0', END),
                        self.supplier_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Supplier Updated Successfully', parent=self.root)
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
            if self.supplier_invoice.get()=='':
                messagebox.showerror('Error', 'Invoice Number must be required', parent=self.root)
            else:
                cur.execute('select * from supplier where invoice =%s ', (self.supplier_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Invalid Invoice Number')
                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op==True:
                        cur.execute('delete from supplier where invoice=%s', (self.supplier_invoice.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Supplier Details Deleted Successfully', parent=self.root)
                        self.clear()

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')



    def clear(self):
        
        self.supplier_invoice.set('')
        self.var_name.set('')
        self.var_contact.set('')
        self.txt_description.delete('1.0',END)
        self.var_searchtxt.set('')
        
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
            if self.var_searchtxt.get() =='':
                messagebox.showerror('Error', 'Invoice Number is required', parent=self.root)
            else:
                cur.execute('select * from supplier where invoice=%s',(self.var_searchtxt.get(),))
                rows = cur.fetchone()
                if rows!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END, values=rows)
                else:
                    messagebox.showerror('Error', 'No Record Found', parent=self.root)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')





if __name__ == '__main__':
    root = Tk()
    obj=supplierclass(root)
    root.mainloop()