import mysql.connector












database = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'hamza2121'
)


cursorobject = database.cursor()

cursorobject.execute('CREATE DATABASE hamza')
print("hello world")