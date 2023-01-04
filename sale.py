 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
class salesclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1070x500+200+130')
        self.root.title('Inventory Management System | Developed By Rangesh')
        self.root.config(bg='sandy brown')
        self.root.focus_force()

        #===========variables========
        self.var_invoice=StringVar()
        self.var_name=StringVar()
        self.bill_list=[]


        #===========title===========
        lbl_title=Label(self.root, text='View Customer Bills', font=('goudy old style', 18,'bold'), bg='#91D8E4',fg='black',).pack(side=TOP, fill=X,padx=10, pady=20)
        lbl_invoice=Label(self.root, text='Invoice No.', font=('goudy old style', 14,'bold'), bg='sandy brown',fg='black',).place(x=50, y=100)
        txt_invoice=Entry(self.root, textvariable=self.var_invoice, font=('goudy old style', 12), bg='lightyellow',fg='black').place(x=160, y=100,width=190)
        btn_search=Button(self.root, text='Search',command=self.search, font=('goudy old style', 11,'bold'), bg='green',fg='white', cursor='hand2').place(x=360, y=100, width=100,height=25)
        btn_delete=Button(self.root, text='Clear', command=self.clear, font=('goudy old style', 11,'bold'), bg='red',fg='white', cursor='hand2').place(x=470, y=100, width=100,height=25)


        #============Bill List===============
        sales_Frame = Frame(self.root, bd=3,relief=RIDGE)
        sales_Frame.place(x=50, y=140,width=200,height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.sales_list=Listbox(sales_Frame, font=('goudy old style', 14), bg='white', yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind('<ButtonRelease-1>', self.get_data)

        #============Bill Area=============
        bill_Frame = Frame(self.root, bd=3,relief=RIDGE)
        bill_Frame.place(x=280, y=140,width=292,height=330)

        lbl_title2=Label(bill_Frame, text='Customer Bill Area', font=('goudy old style', 18,'bold'), bg='#91D8E4',fg='black',).pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area=Text(bill_Frame, bg='lightyellow', yscrollcommand=scrolly2.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)


        self.show()




#=================================functions=================================================
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':          # .txt
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        index_=self.sales_list.curselection()           #givevs index of file
        file_name=self.sales_list.get(index_)
        self.bill_area.delete('1.0',END)
        file = open(f'bill/{file_name}','r')
        for i in file:
            self.bill_area.insert(END, i)
        
        file.close()
    
    def search(self):
        if self.var_invoice.get()=='':
            messagebox.showerror('Error', 'Invoice Number is required', parent = self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                file = open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0', END)
                for i in file:
                    self.bill_area.insert(END, i)
                
                file.close()
            else:
                messagebox.showerror('Error', 'Invalid Invoice Number', parent=self.root)

    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)








if __name__ == '__main__':
    root = Tk()
    obj=salesclass(root)
    root.mainloop()