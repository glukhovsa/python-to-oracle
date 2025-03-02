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