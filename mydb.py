import mysql.connector

database = mysql.connector.connect(
    hots = 'localhost',
    user = 'root',
    password = '',
    database = 'cliente',
    port = '3307',  # Puerto de XAMPP para MySQL
)

#hacer el cursor object
cursorObject = database.cursor()

#crear la base de datos
cursorObject.execute("CREATE DATABASE cliente")

print("All Done!")

