# category
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
class categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1070x500+200+130')
        self.root.title('Inventory Management System | Developed By Rangesh')
        self.root.config(bg='sandy brown')
        self.root.focus_force()


        #===========variables========
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


        #===========title===========
        lbl_title=Label(self.root, text='Manage Product Category', font=('goudy old style', 18,'bold'), bg='#91D8E4',fg='black',).pack(side=TOP, fill=X,padx=10, pady=20)
        lbl_name=Label(self.root, text='Enter Category Name', font=('goudy old style', 14,'bold'), bg='sandy brown',fg='black',).place(x=50, y=100)
        txt_name=Entry(self.root, textvariable=self.var_name, font=('goudy old style', 12), bg='lightyellow',fg='black').place(x=50, y=150,width=200)
        btn_add=Button(self.root, text='ADD', command=self.add, font=('goudy old style', 11,'bold'), bg='green',fg='white', cursor='hand2').place(x=260, y=150, width=100,height=25)
        btn_delete=Button(self.root, text='DELETE', command=self.delete, font=('goudy old style', 11,'bold'), bg='red',fg='white', cursor='hand2').place(x=370, y=150, width=80,height=25)


        #=============Category Details===========

        cat_frame=Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=550,y=100,width=500, height=100)
        
        scrolly = Scrollbar(cat_frame,orient=VERTICAL)
        scrollx = Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame, columns= ('cid', 'name'), yscrollcommand=scrolly.set, xscrollcommand=scrolly.set) ## Import for database
        scrollx.pack(side=BOTTOM, fill= X)
        scrolly.pack(side=LEFT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.heading('cid', text='Category ID')
        self.categoryTable.heading('name', text='Name')
        self.categoryTable['show'] = 'headings'

        self.categoryTable.column('cid', width=90)
        self.categoryTable.column('name', width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind('<ButtonRelease-1>', self.get_data)

        
        #===========Images==========


        #Insert Images here



        self.show()

        #============ functions============
    def add(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_name.get()=='':
                messagebox.showerror('Error', 'Category must be required', parent=self.root)
            else:
                cur.execute('select * from category where cid =%s ', (self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'This Category ID already assigned, try Different ID')
                
                else:
                    cur.execute('insert into category(name) values(%s)', (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo('Success', 'Category added Successfully', parent=self.root)
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
            cur.execute('select * from category')
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END, values=row)

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')

    def get_data(self,ev):
        f=self.categoryTable.focus()
        content= (self.categoryTable.item(f))
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
        )
        cur = con.cursor()

        try:
            if self.var_cat_id.get()=='':
                messagebox.showerror('Error', 'Please select Category name from Category list', parent=self.root)
            else:
                cur.execute('select * from category where cid =%s ', (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Please Try again!!')
                else:
                    op = messagebox.askyesno('Confirm', 'Do you really want to delete?', parent=self.root)
                    if op==True:
                        cur.execute('delete from category where cid=%s', (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo('Delete', 'Category Deleted Successfully', parent=self.root)
                        self.show()
                        self.var_cat_id.set('')
                        self.var_name.set('')

        except Exception as ex: 
            messagebox.showerror('Error', f'Error due to : {str(ex)}')



 
 


if __name__ == '__main__':
    root = Tk()
    obj=categoryclass(root)
    root.mainloop()