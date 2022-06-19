import sqlite3

conn = sqlite3.connect('pruebaSQL.db')

c = conn.cursor()

# CREATE = creacion de la tabla clients
c.execute("CREATE TABLE IF NOT EXISTS clients (first_name, last_name, birth, email)")

# INSERT = agregar valores a la tabla clientes
with conn:
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Kevin', 'Harnan', 22, 'kharnan@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Alejo', 'Di Lelle', 24, 'adilelle@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Ignacio', 'Freiria', 21, 'ifreirian@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Catalina', 'Dapena', 20, 'cdapena@ucema.edu.ar'))

c.execute("SELECT * FROM clients")
print(c.fetchall())

# UPDATE = agregar valores a la tabla clientes
with conn:
    c.execute("UPDATE clients set birth = '23' WHERE first_name = 'Alejo' AND last_name = 'Di Lelle'")

c.execute("SELECT * FROM clients")
print(c.fetchall())

# DELETE = borrar el registro del cliente "Catalina Dapena" la tabla clientes
with conn:
    c.execute("DELETE FROM clients WHERE first_name = 'Catalina' AND lastname = 'Dapena'")

c.execute("SELECT * FROM clients")
print(c.fetchall())
