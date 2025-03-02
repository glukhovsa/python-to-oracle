import cx_Oracle
from pprint import pprint as pp

# data to connect to the database
db_user = "SYS"
db_password = "root"
db_host = "localhost"
db_port = 1521
db_service_name = "FREE"
db_mode = cx_Oracle.SYSDBA


# connection to database
dsn_con = cx_Oracle.makedsn(
    db_host, 
    db_port, 
    service_name=db_service_name
)
connection = cx_Oracle.connect(
    user=db_user,
    password=db_password,
    dsn=dsn_con,
    mode=db_mode,
    encoding="UTF-8",
)

connection.ping()
print("Connection to DataBase is good")

print("Your SQL request or command", end=" >> ")
request = input()
cur = connection.cursor()

while request != "exit":

    #login with another user
    if request == "login":
        print("Your name", end=" # ")
        db_user = input()
        print("Your password", end=" # ")
        db_password = input()
        print("Is you admin & (y/n)", end=" # ")
        is_SYSDBA = input()
        print("Your service name", end=" # ")
        db_service_name = input()

        while is_SYSDBA != 'y' and is_SYSDBA != 'n':
            print("Is you admin & (y/n)", end=" # ")
            is_SYSDBA = input()

        dsn_con = cx_Oracle.makedsn(
            db_host, 
            db_port, 
            service_name=db_service_name
        )

        if is_SYSDBA == 'y':
            db_mode = cx_Oracle.SYSDBA
        else:
            db_mode = None
        
        #print new login data
        print('-'*40)
        print("Your login data:\nYour name is", db_user, "\nYour password is", db_password, "\nYour service name is", db_service_name)
        if db_mode is None:
            print("You are normal user")
        else:
            print("You are admin")
        print('-'*40)
        
        print("Your SQL request or command", end=" >> ")
        request = input()

    #reconnection to database
    if request == "reconnect":
        cur.close()
        connection.close()

        dsn_con = cx_Oracle.makedsn(
            db_host, 
            db_port, 
            service_name=db_service_name
        )
        if db_mode is None:
            connection = cx_Oracle.connect(
                user=db_user,
                password=db_password,
                dsn=dsn_con,
                encoding="UTF-8",
            )
        else:
            connection = cx_Oracle.connect(
                user=db_user,
                password=db_password,
                dsn=dsn_con,
                mode = db_mode,
                encoding="UTF-8",
            )
        
        connection.ping()
        print("Connection to DataBase is good")
        print("Your SQL request or command", end=" >> ")
        request = input()
        cur = connection.cursor()
    
    result = cur.execute(request)
    if result != None:  
        for row in result:
            if row == 'ROOT':
                print ("SCOTT")
            else:
                print(row)
    print("Your SQL request or command", end=" >> ")
    request = input()

cur.close()
connection.close()
