import mysql.connector as a
con = a.connect(host="localhost", user="root", password="qazwsxedc", database="abc")


def ast():
    n = input("Student Name:")
    c = input("Class:")
    r = input("Roll No:")
    b = input("Address:")
    p = input("Phone No:")
    data = (n, c, r, b, p)
    sql = 'insert into student values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">-----------------------------------------------------------------<")
    main()


def rst():
    c = input("Class:")
    r = input("Roll No:")
    data = (c, r)
    sql = "delete from student where Class=%s and Roll No=%s"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">--------------------------------------------------------------<")
    main()


def addt():
    n = input("Teacher:")
    p = input("Post:")
    s = input("Salary:")
    a = input("Address:")
    ph = input("Phone:")
    ac = input("Account:")
    data = (n, p, s, a, ph, ac)
    sql = "insert into teacher values(%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">------------------------------------------------------<")
    main()


def remt():
    n = input("Teacher Name:")
    ac = input("Account No:")
    data = (n, ac)
    sql = "delete from teacher where name = %s and acno = %s"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print(">-------------------------------------------------------------<")
    main()


def abclass():
    d = input("Date:")
    cl = input("Class:")
    ab = input("Name Of Absent Students:")
    data = (d, cl, ab)
    sql = "insert into cattendance values(%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">------------------------------------------------------------------------<")
    main()


def abteacher():
    d = input("date:")
    ab = input("Names Of Absent Teacher:")
    data = (d, ab)
    sql = "insert into tattendance valus(%s,%s)"
    c = con.cursor()
    con.commit()
    print("Data Updated")
    print(">---------------------------------------------------------------------<")
    main()


def submitf():
    n = input("Student Name:")
    c = input("Class Name:")
    r = input("Roll No:")
    m = input("Month and Year:")
    f = input("Fees:")
    d = input("Date:")
    data = (n, c, r, m, f, d)
    sql = "insert into fees values (%s,%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    print(">---------------------------------------------------------------------------<")
    main()


def pays():
    n = input("Teacher Name:")
    m = input("Month:")
    p = input("Yes/No:")
    data = (n, m, p)
    sql = "insert into salary values (%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">------------------------------------------------------------------------------<")
    main()


def dclass():
    cl = input("Class:")
    data = (cl)
    sql = "select*from student where class = %s"
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()      #[(6,6,5,6,8),(6,5,6,5,1),(5,4,7,6)]
    for i in d:
        print("NAME:", i[0])
        print("CLASS:", i[1])
        print("ROLL:", i[2])
        print("ADDRESS:", i[3])
        print("PHONE:", i[4])
        print(">---------------------------------<")
    print(">---------------------------------------------------------------------------------<M")
    main()


def dteacher():
    sql="select*from teacher"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("POST:",i[1])
        print("SALARY:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print("ACNO:",i[5])
        print(">-----------------------<")
    print(">-------------------------------------------------------------------------------------------<")
    main()

def main():
    print(""""           DAYAWATI MODI ACADMEY
                    1.ADD STUDENT            2.REMOVE STUDENT
                    3.ADD TEACHER            4.REMOVE STUDENT
                    5.CLASS ATTENDANCE       6.TEACHER ATTENDANCE
                    7.SUBMIT FEES            8.PAY SALARY
                    9.DISPLAY CLASS          10.TEACHER LIST
""")
    choice=input("Enter Task No:")
    print(">------------------------<")
    if(choice=="1"):
        ast()
    elif(choice=="2"):
        rst()
    elif(choice=="3"):
        addt()
    elif(choice=="4"):
        remt()
    elif(choice=="5"):
        abclass()
    elif(choice=="6"):
        abteacher()
    elif(choice=="7"):
        submitf()
    elif(choice=="8"):
        pays()
    elif(choice=="9"):
        dclass()
    elif(choice=="10"):
        dteacher()
    else:
        print("Wrong choice.........")
        main()

def pswd():
    p = input("Password:")
    if(p == "qazwsxedc"):
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()
