from tkinter import *
from tkinter import ttk
#from tkMessageBox import *
from tkinter import messagebox
import mysql.connector
from prettytable import PrettyTable

demo = mysql.connector.connect(user='root',
                               host='localhost',
                               password='tiger',
                               database='compproj')

mycursor=demo.cursor()

def sql():
     global demo,mycursor
##     mycursor.execute('CREATE DATABASE IF NOT EXISTS COMPPROJ')
##     mycursor.execute('USE COMPPROJ')

     
     mycursor.execute('''CREATE TABLE IF NOT EXISTS STD_REG(CARD_NUM INT(6) UNIQUE,FNAME VARCHAR(40),

                      LNAME VARCHAR(40),CLASS INT(2), CHECK(1<=CLASS<=12),SEC VARCHAR(2),ROLLNUM INT(2))''')
     mycursor.execute('''CREATE TABLE IF NOT EXISTS EMP_REG(CARD_NUM INT(6) AUTO_INCREMENT PRIMARY KEY,FNAME VARCHAR(40),
                      LNAME VARCHAR(40))''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS BOOKS_PURCHASED(ACC_NO INT(10) AUTO_INCREMENT PRIMARY KEY ,BILL_NO INT(10),
                      TITLE VARCHAR(50),AUTHOR VARCHAR(60),PUBLISHER VARCHAR(60),DOP DATE)''')



     mycursor.execute('''CREATE TABLE IF NOT EXISTS BOOKS_ISSUED(BOOK VARCHAR(60), NAME VARCHAR(60), ACC_NO INT(10) PRIMARY KEY,
                      CLASS INT(2),FOREIGN KEY(ACC_NO) REFERENCES BOOKS_PURCHASED(ACC_NO))''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS EMPBOOK(BOOK VARCHAR(60),FNAME VARCHAR(60),LNAME VARCHAR(60), ACC_NO INT(10)
                      PRIMARY KEY ,CARD_NUM INT(6),FOREIGN KEY(ACC_NO) REFERENCES BOOKS_PURCHASED(ACC_NO))''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS EMPBOOKR(BOOK VARCHAR(60),FNAME VARCHAR(60),LNAME VARCHAR(60), ACC_NO INT(10)
                      PRIMARY KEY ,CARD_NUM INT(6),FOREIGN KEY(ACC_NO) REFERENCES BOOKS_PURCHASED(ACC_NO))''')
     
     mycursor.execute('''CREATE TABLE IF NOT EXISTS STUBOOK(BOOK VARCHAR(60),FNAME VARCHAR(60),LNAME VARCHAR(60), ACC_NO INT(10)
                       ,CARD_NUM INT(6),FOREIGN KEY(ACC_NO) REFERENCES BOOKS_PURCHASED(ACC_NO))''')
     
     mycursor.execute('''CREATE TABLE IF NOT EXISTS STUBOOKR(BOOK VARCHAR(60),FNAME VARCHAR(60),LNAME VARCHAR(60), ACC_NO INT(10)
                       ,CARD_NUM INT(6),FOREIGN KEY(ACC_NO) REFERENCES BOOKS_PURCHASED(ACC_NO))''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS ISSUED (CARD_NUM INT(6),FNAME VARCHAR(60),LNAME VARCHAR(60),CLASS INT(2),SEC VARCHAR(2)
                      ,ROLLNUM INT(2),BOOK VARCHAR(60),ACC_NO INT(10));''')
     
     mycursor.execute('''CREATE TABLE IF NOT EXISTS ISSUED1 (CARD_NUM INT(6),FNAME VARCHAR(60),LNAME VARCHAR(60),BOOK VARCHAR(60),ACC_NO INT(10));''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS RETURNED (CARD_NUM INT(6),FNAME VARCHAR(60),LNAME VARCHAR(60),CLASS INT(2),SEC VARCHAR(2)
                      ,ROLLNUM INT(2),BOOK VARCHAR(60),ACC_NO INT(10));''')

     mycursor.execute('''CREATE TABLE IF NOT EXISTS RETURNED1 (CARD_NUM INT(6),FNAME VARCHAR(60),LNAME VARCHAR(60),BOOK VARCHAR(60),ACC_NO INT(10));''')
##     mycursor.execute('INSERT INTO BOOKS_PURCHASED VALUES (1000,100001,"OXFORD DICTIONARY","JOHN SIMPSON","OXFORD UNIVERSITY PRESS","2005-05-16")')
##     demo.commit()
def screen():
     sql()
     root=Tk()
     root.configure(background='SlateBlue3')
##root.geometry('900x900')

     Canvas1 = Canvas(root)
     root.state('zoomed')
     headingFrame1 = Frame(root,bg="yellow",bd=5) 
     headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16) 
     headingFrame2 = Frame(headingFrame1,bg="cyan") 
     headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9) 
     headingLabel = Label(headingFrame2, text="Welcome to SHS Library", fg='black') 
     headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

     btn1 = Button(root,text="Employee",bg='black', fg='white',command= lambda: Employee()) 
     btn1.place(relx=0.15,rely=0.3, relwidth=0.2,relheight=0.1)
     btn2 = Button(root,text="Student",bg='black', fg='white', command= lambda :Student()) 
     btn2.place(relx=0.45,rely=0.3, relwidth=0.2,relheight=0.1)
     btn3 = Button(root,text="Admin",bg='black', fg='white', command= lambda :admin()) 
     btn3.place(relx=0.75,rely=0.3, relwidth=0.2,relheight=0.1)

screen()

def Employee(): 
     root=Tk()
##     root.geometry('900x900')
     root.state('zoomed')

     global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1 
     
     Canvas1 = Canvas(root) 
 
     Canvas1.config(bg="ORANGE",width=340,height=300) 
     Canvas1.pack(expand=True,fill=BOTH) 
  
     headingFrame1 = Frame(root,bg="#223945",bd=5) 
     headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13) 
      
     headingFrame2 = Frame(headingFrame1,bg="#EAF0F1") 
     headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9) 
      
     headingLabel = Label(headingFrame2, text="Hello, Employee", fg='black') 
     headingLabel.place(relx=0.25,rely=0.15, relwidth=0.6, relheight=0.5) 
      
     btn5 = Button(root,text="Register",bg='green', fg='white',command=lambda:EmpRegister()) 
     btn5.place(relx=0.15,rely=0.3, relwidth=0.2,relheight=0.1) 
      
     btn6 = Button(root,text="Login",bg='cyan', fg='black', command=lambda:Login()) 
     btn6.place(relx=0.35,rely=0.3, relwidth=0.2,relheight=0.1)

     btn7 = Button(root,text="Issue book",bg='green', fg='white',command=lambda:employee_issue())
     btn7.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

     btn8 = Button(root,text="Return book",bg='cyan', fg='black',command=lambda:employee_return())
     btn8.place(relx=0.75,rely=0.3, relwidth=0.2,relheight=0.1)

     btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:screen())
     btn19.place(relx=0.45,rely=0.5, relwidth=0.2,relheight=0.1)
def employee_issue():
     
    root=Tk()
##    root.geometry('900x900')
    root.state('zoomed')

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    tkvar=StringVar(root)
    a=Label(root,text='ENTER THE BOOK NAME: ')
    b=Label(root,text='ENTER FIRST NAME: ')
    c=Label(root,text='ENTER LAST NAME: ')
    d=Label(root,text='ENTER ACC NO: ')
    e=Label(root,text='ENTER CARD NO: ')

    a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)

    book = Entry(root)
    fn = Entry(root)
    ln = Entry(root)
    ac = Entry(root)
    cn = Entry(root)

    book.grid(row = 1 , column = 2)
    fn.grid(row = 2 , column = 2) 
    ln.grid(row = 3 , column = 2)
    ac.grid(row = 4 , column = 2)
    cn.grid(row = 5 , column = 2)
    
    b = Button(root,text="SUBMIT",command=lambda : action1()) 
    b.grid(row = 7,column = 1)
    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Employee())
    btn19.grid(row=7,column=2)

    def action1():
        global demo,mycursor
        b=book.get()
        fname=fn.get()
        acc=int(ac.get())
        lname=ln.get()
        cardnum=int(cn.get())
        query='''INSERT INTO EMPBOOK(BOOK,FNAME,LNAME,ACC_NO,CARD_NUM)
              VALUES("{}","{}","{}",{},{})'''.format(b,fname,lname,acc,cardnum)
        messagebox.showinfo('','%s HAS BORROWED %s '%(fname,b,))
        #print(fname,'has borrowed ',b)
        mycursor.execute(query)
        demo.commit()
        
def employee_return():
     
    root=Tk()
##    root.geometry('900x900')
    root.state('zoomed')

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    tkvar=StringVar(root)
    a=Label(root,text='ENTER THE BOOK NAME: ')
    b=Label(root,text='ENTER FIRST NAME: ')
    c=Label(root,text='ENTER LAST NAME: ')
    d=Label(root,text='ENTER ACC NO: ')
    e=Label(root,text='ENTER CARD NO: ')

    a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    
    book = Entry(root)
    fn = Entry(root)
    ln = Entry(root)
    ac = Entry(root)
    cn = Entry(root)
    
    book.grid(row = 1 , column = 2)
    fn.grid(row = 2 , column = 2) 
    ln.grid(row = 3 , column = 2)
    ac.grid(row = 4 , column = 2)
    cn.grid(row = 5 , column = 2)
    
    b = Button(root,text="SUBMIT",command=lambda : action1()) 
    b.grid(row = 7,column = 1)
    
    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Employee())
    btn19.grid(row=7,column=2)
    def action1():
        global demo,mycursor
        b=book.get()
        fname=fn.get()
        acc=int(ac.get())
        lname=ln.get()
        cardnum=int(cn.get())
        query='''INSERT INTO EMPBOOKR(BOOK,FNAME,LNAME,ACC_NO,CARD_NUM)
              VALUES("{}","{}","{}",{},{})'''.format(b,fname,lname,acc,cardnum)
        messagebox.showinfo('','%s HAS RETURNED %s '%(fname,b,))
        #print(fname,'has borrowed ',b)
        mycursor.execute(query)
        mycursor.execute('DELETE FROM EMPBOOK WHERE ACC_NO=%s'%(acc,))

        demo.commit()

def EmpRegister(): 
    root=Tk()
##    root.geometry('900x900')
    root.state('zoomed')

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    a=Label(root,text='ENTER YOUR CARD NUM: ')
    b=Label(root,text='ENTER YOUR FIRST NAME: ')
    c=Label(root,text='ENTER YOUR LAST NAME: ')

    a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)

    c = Entry(root)
    f = Entry(root)
    l = Entry(root)

    c.grid(row = 1 , column = 2)
    f.grid(row = 2 , column = 2) 
    l.grid(row = 3 , column = 2)

    
    b = Button(root,text="SUBMIT",command=lambda : action()) 
    b.grid(row = 4,column = 1)
    
    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Employee())
    btn19.grid(row=7,column=2)
    def action():
        global demo,mycursor
        card=int(c.get())
        fn=f.get()
        ln=l.get()
        mycursor.execute("SELECT * FROM EMP_REG")
        l_emp=[i for i in mycursor.fetchall()]
        for i in l_emp:
             if fn in i and ln in i:
                  messagebox.showinfo('','%s %s YOU HAVE ALREADY BEEN REGISTERED '%(fn,ln,))
                  #print(fn,ln,'YOU HAVE ALREADY BEEN REGISTERED')
                  break
        else:
              query='''INSERT INTO EMP_REG(CARD_NUM, FNAME, LNAME)
                                 VALUES({},"{}","{}")'''.format(card,fn,ln)
              mycursor.execute(query)
              demo.commit()
              messagebox.showinfo('REGISTRATION SUCCESFUL','%s %s YOUR REGISTRATION WAS SUCCESSFUL '%(fn,ln,))
              #print(fn,ln,'YOUR REGISTRATION WAS SUCCESFUL')
             
        Canvas1.destroy()

def Login():
     root=Tk()#parent window
##     root.geometry('900x900')
     root.state('zoomed')

     global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
     a=Label(root,text='ENTER CARD NUMBER: ')
     b=Label(root,text='ENTER USER NAME: ')

     a.grid(row = 1 , column = 1)
     b.grid(row = 2 , column = 1)

     cn = Entry(root)
     fn = Entry(root)

     cn.grid(row = 1 , column = 2)
     fn.grid(row = 2 , column = 2)

     b1 = Button(root,text="SUBMIT",command=lambda : act()) 
     b1.grid(row=3,column=1) 

     btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Employee())
     btn19.grid(row=7,column=2)
     def act():
         global demo,mycursor
         cnum = int(cn.get())
         fname = fn.get()
         mycursor.execute("SELECT * FROM EMP_REG")
         l1=[i for i in mycursor.fetchall()]
         l2=[(i[0],i[1]) for i in l1]
         for i in l2:
              if i[0]==cnum and i[1]==fname:
                   #print(fname,'your login was succesful')
                   messagebox.showinfo('','%s YOUR LOGIN WAS SUCCESSFUL '%(fname,))
                   booksearch()
                   break
         else:
              messagebox.showinfo('ERROR','TRY AGAIN')

#---------------------------------------------------------------------------------------
def Student(): 
     root=Tk()
##     root.geometry('900x900')
     root.state('zoomed')

##     global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1 
##     headingFrame1.destroy() 
##     headingFrame2.destroy() 
##     headingLabel.destroy() 
##     Canvas1.destroy() 
##     btn1.destroy() 
##     btn2.destroy() 
##     btn3.destroy() 
     Canvas1 = Canvas(root) 
 
     Canvas1.config(bg="purple",width=340,height=300) 
     Canvas1.pack(expand=True,fill=BOTH) 
  
     headingFrame1 = Frame(root,bg="#223945",bd=5) 
     headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13) 
      
     headingFrame2 = Frame(headingFrame1,bg="#EAF0F1") 
     headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9) 
      
     headingLabel = Label(headingFrame2, text="Hello, Student", fg='black') 
     headingLabel.place(relx=0.25,rely=0.15, relwidth=0.6, relheight=0.5) 
      
     btn11 = Button(root,text="Register",bg='black', fg='white',command=lambda:StdRegister()) 
     btn11.place(relx=0.15,rely=0.3, relwidth=0.2,relheight=0.1) 
      
     btn21 = Button(root,text="Login",bg='white', fg='black', command=lambda:STD_Login()) 
     btn21.place(relx=0.35,rely=0.3, relwidth=0.2,relheight=0.1)

     btn12 = Button(root,text="Issue",bg='black', fg='white',command=lambda:stu_issue()) 
     btn12.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1) 

     btn13 = Button(root,text="Return",bg='white', fg='black',command=lambda:stu_return()) 
     btn13.place(relx=0.75,rely=0.3, relwidth=0.2,relheight=0.1)

     btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:screen())
     btn19.place(relx=0.45,rely=0.5, relwidth=0.2,relheight=0.1)
def StdRegister(): 
    root=Tk()
##    root.geometry('900x900')#parent window
    root.state('zoomed')

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    a=Label(root,text='ENTER YOUR CARD NUM: ')
    b=Label(root,text='ENTER YOUR FIRST NAME: ')
    c=Label(root,text='ENTER YOUR LAST NAME: ')
    d=Label(root,text='ENTER YOUR CLASS: ')
    e=Label(root,text='ENTER YOUR SECTION: ')
    f=Label(root,text='ENTER YOUR ROLL NUMBER: ')

    a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    f.grid(row = 6 , column = 1)
 

    cn = Entry(root)
    fn = Entry(root)
    ln = Entry(root)
    cl = Entry(root)
    se = Entry(root)
    rn = Entry(root)

    cn.grid(row = 1 , column = 2)
    fn.grid(row = 2 , column = 2) 
    ln.grid(row = 3 , column = 2)
    cl.grid(row = 4 , column = 2)
    se.grid(row = 5 , column = 2)
    rn.grid(row = 6 , column = 2)

    b = Button(root,text="SUBMIT",command=lambda : action())
    b1= Button(root,text="BACK",command=lambda : Student())
    b.grid(row = 7,column = 1)
    b1.grid(row = 7,column = 2)
    
    def action():
        global demo,mycursor
        card=int(cn.get())
        fname=fn.get()
        lname=ln.get()
        clas=int(cl.get())
        sec=se.get()
        rollnum=int(rn.get())
        mycursor.execute("SELECT * FROM STD_REG")
        s_emp=[i for i in mycursor.fetchall()]
        for i in s_emp:
             if fname in i and lname in i:
                  print('YOU HAVE ALREADY BEEN REGISTERED')
                  messagebox.showinfo('','YOU HAVE ALREADY BEEN REGISTERED')
                  break
        else:
             query='''INSERT INTO STD_REG(CARD_NUM, FNAME, LNAME,CLASS,SEC,ROLLNUM)
                    VALUES({},"{}","{}",{},"{}",{})'''.format(card,fname,lname,clas,sec,rollnum)
             mycursor.execute(query)
             demo.commit()
             print()
             messagebox.showinfo('','%s %s YOUR REGISTRATION WAS SUCCESFUL '%(fname,lname,))
        
        

def stu_issue():
    root=Tk()
##    root.geometry('900x900')
    root.state('zoomed')
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    tkvar=StringVar(root)
##    a=Label(root,text='ENTER THE BOOK NAME: ')
    b=Label(root,text='ENTER FIRST NAME: ')
    c=Label(root,text='ENTER LAST NAME: ')
##    d=Label(root,text='ENTER ACC NO: ')
    e=Label(root,text='ENTER CARD NUMBER: ')

    #a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    #d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    
    #book = Entry(root)
    fn = Entry(root)
    ln = Entry(root)
    #ac = Entry(root)
    cn = Entry(root)

    #book.grid(row = 1 , column = 2)
    fn.grid(row = 2 , column = 2) 
    ln.grid(row = 3 , column = 2)
    #ac.grid(row = 4 , column = 2)
    cn.grid(row = 5 , column = 2)


    global demo,mycursor
    mycursor.execute('SELECT * FROM BOOKS_PURCHASED')
    l1=[(i[0],i[2]) for i in mycursor.fetchall()]
    
    mycursor.execute('SELECT DISTINCT * FROM STUBOOK')
    l2=[(i[3],i[0]) for i in mycursor.fetchall()]

    mycursor.execute('SELECT DISTINCT * FROM EMPBOOK')
    l3=[(i[3],i[0]) for i in mycursor.fetchall()]

    mycursor.execute('SELECT DISTINCT * FROM STUBOOKR')
    l4=[(i[3],i[0]) for i in mycursor.fetchall()]

    mycursor.execute('SELECT DISTINCT * FROM EMPBOOKR')
    l5=[(i[3],i[0]) for i in mycursor.fetchall()]
     
    L1=l1+l4+l5#available
    L2=l2+l3#borrowed
    L3=[int(i[0]) for i in L1 if i not in L2]#list of accession numbers
    #print(L3)
    L4=[i[1] for i in L1 if i not in L2]#list of books
    print(L4)
    d={}
    for i in range(len(L3)):
         d[L3[i]]=L4[i]
         
    choices=L4
    popupMenu=OptionMenu(root, tkvar, *choices)
     
    Label(root, text="Choose a book").grid(row = 9, column = 1)
    popupMenu.grid(row = 11, column =1)

    b = Button(root,text="SUBMIT",command=lambda : action1()) 
    b.grid(row = 15,column = 1)

    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Student())
    btn19.grid(row = 15,column = 3)
   
    def action1():
            bookname=tkvar.get()
            for i in d:
                if d[i]==bookname:
                     accnumber=i
                     break
            print(bookname,'    ',accnumber)
            
            #tkvar.trace('w', change_dropdown)
            #root.mainloop()
            global demo,mycursor
            #b=book.get()
            fname=fn.get()
            #acc=int(ac.get())
            lname=ln.get()
            cardnum=int(cn.get())
            
            query='''INSERT INTO STUBOOK (BOOK,FNAME,LNAME,ACC_NO,CARD_NUM)
                         VALUES("{}","{}","{}",{},{})'''.format(bookname,fname,lname,accnumber,cardnum)
            
            messagebox.showinfo('','%s HAS BORROWED %s '%(fname,bookname,))
                #print(fname,'has borrowed ',b)
            mycursor.execute(query)
            demo.commit()  
    
def stu_return():
     
    root=Tk()
##    root.geometry('900x900')
    root.state('zoomed')
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    tkvar=StringVar(root)
    a=Label(root,text='ENTER THE BOOK NAME: ')
    b=Label(root,text='ENTER FIRST NAME: ')
    c=Label(root,text='ENTER LAST NAME: ')
    d=Label(root,text='ENTER ACC NO: ')
    e=Label(root,text='ENTER CARD NO: ')

    a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    
    book = Entry(root)
    fn = Entry(root)
    ln = Entry(root)
    ac = Entry(root)
    cn = Entry(root)
    
    book.grid(row = 1 , column = 2)
    fn.grid(row = 2 , column = 2) 
    ln.grid(row = 3 , column = 2)
    ac.grid(row = 4 , column = 2)
    cn.grid(row = 5 , column = 2)
    
    b = Button(root,text="SUBMIT",command=lambda : action1()) 
    b.grid(row = 7,column = 1)
    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Student())
    btn19.grid(row = 7,column = 3)
    def action1():
        global demo,mycursor
        b=book.get()
        fname=fn.get()
        acc=int(ac.get())
        lname=ln.get()
        cardnum=int(cn.get())
        query='''INSERT INTO STUBOOKR(BOOK,FNAME,LNAME,ACC_NO,CARD_NUM)
              VALUES("{}","{}","{}",{},{})'''.format(b,fname,lname,acc,cardnum)
        messagebox.showinfo('','%s HAS RETURNED %s '%(fname,b,))
        #print(fname,'has borrowed ',b)
        mycursor.execute(query)
        mycursor.execute('DELETE FROM STUBOOK WHERE ACC_NO=%s'%(acc,))
        demo.commit()
        
def STD_Login():
     root=Tk()
##     root.geometry('900x900')#parent window
     root.state('zoomed')
     global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
     a=Label(root,text='ENTER CARD NUMBER: ')
     b=Label(root,text='ENTER FIRST NAME: ')
     c=Label(root,text='ENTER CLASS: ')
     d=Label(root,text='ENTER SECTION: ')
     

     a.grid(row = 1 , column = 1)
     b.grid(row = 2 , column = 1)
     c.grid(row = 3 , column = 1)
     d.grid(row = 4 , column = 1)

     cn = Entry(root)
     fn = Entry(root)
     cl=Entry(root)
     sec=Entry(root)

     cn.grid(row = 1 , column = 2)
     fn.grid(row = 2 , column = 2)
     cl.grid(row = 3 , column = 2)
     sec.grid(row = 4 , column = 2)

     b1 = Button(root,text="SUBMIT",command=lambda : act()) 
     b1.grid(row=5,column=1) 

     btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:Student())
     btn19.grid(row=5,column=3) 
     def act():
         global demo,mycursor
         cnum = int(cn.get())
         fname = fn.get()
         clas=int(cl.get())
         sect=sec.get()
         mycursor.execute("SELECT * FROM STD_REG")
         l=[(i[0],i[1]) for i in mycursor.fetchall()]
         for i in l:
              if (i[0]==cnum) and i[1]==fname:
                   messagebox.showinfo('','%s YOUR LOGIN WAS SUCCESSFUL '%(fname))
                   print(fname,'your login was succesful')
                   booksearch()
                   break
         else:
              messagebox.showinfo('ERROR','try again ')
              print('try again')

def booksearch():
     global demo,mycursor
     mycursor.execute('SELECT * FROM BOOKS_PURCHASED')
     l1=[(i[0],i[2]) for i in mycursor.fetchall()]
    
     mycursor.execute('SELECT DISTINCT * FROM STUBOOK')
     l2=[(i[3],i[0]) for i in mycursor.fetchall()]

     mycursor.execute('SELECT DISTINCT * FROM EMPBOOK')
     l3=[(i[3],i[0]) for i in mycursor.fetchall()]

     mycursor.execute('SELECT DISTINCT * FROM STUBOOKR')
     l4=[(i[3],i[0]) for i in mycursor.fetchall()]

     mycursor.execute('SELECT DISTINCT * FROM EMPBOOKR')
     l5=[(i[3],i[0]) for i in mycursor.fetchall()]
     
     L1=l1+l4+l5#available
     L2=l2+l3#borrowed
     #print(l1,l2)
      
     book=[i for i in L1 if i not in L2]
     root=Tk()
     a=Label(root,text='ENTER THE NAME OF THE BOOK: ')
     a.grid(row = 0 , column = 1)
     b=Entry(root)
     b.grid(row = 1 , column = 1)

     b1 = Button(root,text="SUBMIT",command=lambda : act()) 
     b1.grid(row=5,column=1)

     def act():
         name=b.get()
         for i in book:
             if i[1]==name:
                  #import tkinter
                  messagebox.showinfo('','%s is available contact your librarian soon'%(name,))
                  break
             else:
                  continue
                
         else:
             #print(name,'is unavailable')
             messagebox.showinfo('','%s is unavailable '%(name,))

def admin():
     #print('WELCOME ADMIN')
     root=Tk()
##     root.geometry('900x900')
     root.state('zoomed')
##     global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1 
##     headingFrame1.destroy() 
##     headingFrame2.destroy() 
##     headingLabel.destroy() 
##     Canvas1.destroy() 
##     btn1.destroy() 
##     btn2.destroy() 
##     btn3.destroy() 
      
     Canvas1 = Canvas(root) 
 
     Canvas1.config(bg="cyan",width=340,height=300) 
     Canvas1.pack(expand=True,fill=BOTH) 
  
     headingFrame1 = Frame(root,bg="#223945",bd=5) 
     headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13) 
      
     headingFrame2 = Frame(headingFrame1,bg="#EAF0F1") 
     headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9) 
      
     headingLabel = Label(headingFrame2, text="Hello, Admin", fg='black') 
     headingLabel.place(relx=0.25,rely=0.15, relwidth=0.6, relheight=0.5) 
      
##     btn1 = Button(root,text="ISSUE BOOK",bg='black', fg='white',command=lambda:issue()) 
##     btn1.place(relx=0.0,rely=0.3, relwidth=0.5,relheight=0.1) 
      
     btn4 = Button(root,text="UPDATE STATISTICS",bg='black', fg='white', command=lambda:update()) 
     btn4.place(relx=0.15,rely=0.3, relwidth=0.2,relheight=0.1)

     btn8 = Button(root,text="DELETE STATISTICS",bg='black', fg='white', command=lambda:deletestat())
     btn8.place(relx=0.35,rely=0.3, relwidth=0.2,relheight=0.1)

     btn9 = Button(root,text="ISSUED BOOKS",bg='black', fg='white', command=lambda:issued())
     btn9.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)
     
     btn10 = Button(root,text="RETURNED BOOKS",bg='black', fg='white', command=lambda:returned())
     btn10.place(relx=0.75,rely=0.3, relwidth=0.2,relheight=0.1)

     btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:screen())
     btn19.place(relx=0.45,rely=0.5, relwidth=0.2,relheight=0.1)
def update():
    root=Tk()#parent window
##    root.geometry('900x900')
    root.state('zoomed')
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    global demo,mycursor
    #a=Label(root,text='ENTER THE ACCESSION NUMBER: ')
    b=Label(root,text='ENTER BILL NUMBER: ')
    c=Label(root,text='ENTER TITLE: ')
    d=Label(root,text='ENTER AUTHOR: ')
    e=Label(root,text='ENTER PUBLISHER: ')
    f=Label(root,text='ENTER BILLNG DATE: ')

    #a.grid(row = 1 , column = 1)
    b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    f.grid(row = 6 , column = 1)
 

    #acc = Entry(root)
    bil = Entry(root)
    tit = Entry(root)
    aut = Entry(root)
    pub = Entry(root)
    bdate = Entry(root)

    #acc.grid(row = 1 , column = 2)
    bil.grid(row = 2 , column = 2) 
    tit.grid(row = 3 , column = 2)
    aut.grid(row = 4 , column = 2)
    pub.grid(row = 5 , column = 2)
    bdate.grid(row = 6 , column = 2)

    b = Button(root,text="SUBMIT",command=lambda : action()) 
    b.grid(row = 7,column = 1)

    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:admin())
    btn19.grid(row = 7,column = 3)
    def action():
        global demo,mycursor
        #a=int(acc.get())
        b=int(bil.get())
        t=tit.get()
        au=aut.get()
        p=pub.get()
        bill_date=bdate.get()

        query='INSERT INTO BOOKS_PURCHASED(BILL_NO,TITLE,AUTHOR,PUBLISHER,DOP) VALUES({},"{}","{}","{}","{}")'.format(b,t,au,p,bill_date)
        mycursor.execute(query)
        demo.commit()
        messagebox.showinfo("","%s WITH HAS BEEN UPDATED WITH BILL NUMBER %s"%(t,b,))
        books()
        #print(t,' WITH ACCESSION NUMBER',a,'HAS BEEN UPDATED WITH BILL NUMBER',b)


def deletestat():
    root=Tk()#parent window
##    root.geometry('900x900')
    root.state('zoomed')
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    global demo,mycursor
    a=Label(root,text='ENTER THE ACCESSION NUMBER: ')
    c=Label(root,text='ENTER TITLE: ')
    d=Label(root,text='ENTER AUTHOR: ')
    e=Label(root,text='ENTER PUBLISHER: ')
    #f=Label(root,text='ENTER BILLNG DATE: ')

    a.grid(row = 1 , column = 1)
    #b.grid(row = 2 , column = 1)
    c.grid(row = 3 , column = 1)
    d.grid(row = 4 , column = 1)
    e.grid(row = 5 , column = 1)
    #f.grid(row = 6 , column = 1)
 

    acc = Entry(root)
    #bil = Entry(root)
    tit = Entry(root)
    aut = Entry(root)
    pub = Entry(root)
    #bdate = Entry(root)

    acc.grid(row = 1 , column = 2)
    #bil.grid(row = 2 , column = 2) 
    tit.grid(row = 3 , column = 2)
    aut.grid(row = 4 , column = 2)
    pub.grid(row = 5 , column = 2)
    #bdate.grid(row = 6 , column = 2)

    b = Button(root,text="SUBMIT",command=lambda : action()) 
    b.grid(row = 7,column = 1)

    btn19 = Button(root,text="BACK",bg='red', fg='black',command=lambda:admin())
    btn19.grid(row = 7,column = 3)
    def action():
        global demo,mycursor
        a=int(acc.get())
        #b=int(bil.get())
        t=tit.get()
        au=aut.get()
        p=pub.get()
        #bill_date=bdate.get()

        query="DELETE FROM BOOKS_PURCHASED WHERE ACC_NO = {}".format(a)
        #data=(a,)
        mycursor.execute(query)
        demo.commit()
        messagebox.showinfo('%s WITH ACCESSION NUMBER  HAS BEEN DELETED '%(t,))
        #print(t,' WITH ACCESSION NUMBER',a,'HAS BEEN DELETED ')

def issued():
     global demo,mycursor
     mycursor.execute('INSERT INTO ISSUED SELECT DISTINCT * FROM STD_REG NATURAL JOIN STUBOOK;')
     mycursor.execute('ALTER TABLE ISSUED1 MODIFY CARD_NUM INT(6) FIRST ;')
     mycursor.execute('INSERT INTO ISSUED1 SELECT DISTINCT * FROM EMP_REG NATURAL JOIN EMPBOOK;')
     
     demo.commit()
     admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
     cur = admin.cursor()
     cur.execute('SHOW TABLES')
     tables = ['issued','issued1']
     #print(tables)
     for table in tables:
          admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
          cur = admin.cursor()
          print("Table " + table)
          cur.execute('DESC ' + table)
          cols = [i[0] for i in cur.fetchall()]
          cur.execute('SELECT DISTINCT * FROM ' + table)
          rows = cur.fetchall()
          ptable = PrettyTable(cols)
          for i in range(len(rows)):
              ptable.add_row(rows[i])
          print(ptable)
          print()

def returned():
     global demo,mycursor
     mycursor.execute('INSERT INTO RETURNED SELECT DISTINCT * FROM STD_REG NATURAL JOIN STUBOOKR;')
     mycursor.execute('ALTER TABLE RETURNED1 MODIFY CARD_NUM INT(6) AFTER LNAME ;')
     mycursor.execute('INSERT INTO RETURNED1 SELECT DISTINCT * FROM EMP_REG NATURAL JOIN EMPBOOKR;')
     
     demo.commit()
     admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
     cur = admin.cursor()
     cur.execute('SHOW TABLES')
     tables = ['returned','returned1']
     #print(tables)
     for table in tables:
          admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
          cur = admin.cursor()
          print("Table " + table)
          cur.execute('DESC ' + table)
          cols = [i[0] for i in cur.fetchall()]
          cur.execute('SELECT DISTINCT * FROM ' + table)
          rows = cur.fetchall()
          ptable = PrettyTable(cols)
          for i in range(len(rows)):
              ptable.add_row(rows[i])
          print(ptable)
          print()

#pretty table for books available
def books():

     admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
     cur = admin.cursor()
     cur.execute('SHOW TABLES')
     tables = ['books_purchased']
     #print(tables)
     for table in tables:
          admin = mysql.connector.connect( user = 'root',
                          password = 'tiger',
                          host = 'localhost',
                          database = 'compproj')
          cur = admin.cursor()
          print("Table " + table)
          cur.execute('DESC ' + table)
          cols = [i[0] for i in cur.fetchall()]
          cur.execute('SELECT * FROM ' + table)
          rows = cur.fetchall()
          ptable = PrettyTable(cols)
          for i in range(len(rows)):
              ptable.add_row(rows[i])
          print(ptable)
          print()

#books()

##messagebox.showinfo("Information","Informative message")
##messagebox.showerror("Error", "Error message")
##messagebox.showwarning("Warning","Warning message")
