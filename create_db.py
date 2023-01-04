# database
import mysql.connector
def create_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'IMS'
    )

    # employee table
    cur=con.cursor()
    cur.execute('''create table employee(
        eid int primary key,
        name varchar(40), 
        email varchar(40), 
        gender varchar(20), 
        contact varchar(20), 
        dob varchar(20), 
        doj varchar(20), 
        pass varchar(20), 
        utype varchar(20), 
        address varchar(60), 
        salary varchar(20))''')
    con.commit()

    # supplier table
    # cur=con.cursor()
    # cur.execute('''create table supplier(
    #     invoice int primary key,
    #     name varchar(20),  
    #     contact varchar(20), 
    #     description varchar(60))''')
    # con.commit()


    # Category Table
    # cur=con.cursor()
    # cur.execute('''create table category(
    #     cid int primary key auto_increment,
    #     name varchar(20) 
    #     )''')
    # con.commit()


    #product table
    # cur=con.cursor()
    # cur.execute('''create table product(
    #     pid int primary key auto_increment,
    #     Category varchar(20),
    #     Supplier varchar(20),
    #     Name varchar(20),
    #     price varchar(20),
    #     quantity varchar(20),
    #     status varchar(20)
        
    #     )''')
    # con.commit()
    



create_db()