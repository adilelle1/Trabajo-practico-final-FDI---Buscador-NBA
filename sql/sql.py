import sqlite3

conn = sqlite3.connect('pruebaSQL.db')

c = conn.cursor()

# CREATE = Crea la tabla clients
c.execute("CREATE TABLE IF NOT EXISTS clients (first_name, last_name, birth, email)")


# INSERT = Agrega valores a la tabla clients
print("\nMetodo INSERT - Valores de la tabla clients")

with conn:
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Kevin', 'Harnan', 22, 'kharnan@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Alejo', 'Di Lelle', 24, 'adilelle@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Ignacio', 'Freiria', 21, 'ifreirian@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Catalina', 'Dapena', 20, 'cdapena@ucema.edu.ar'))

c.execute("SELECT * FROM clients")
print(c.fetchall())


# UPDATE = Actualiza valores de la tabla clients, en este caso cambia la edad de Alejo de 24 a 23 años
print("\nMetodo UPDATE - Actualiza la tabla clients")

with conn:
    c.execute("UPDATE clients set birth = '23' WHERE first_name = 'Alejo' AND last_name = 'Di Lelle'")

c.execute("SELECT * FROM clients WHERE last_name = 'Di Lelle'")
print(c.fetchall())


# DELETE = Borra el registro del cliente "Catalina Dapena" la tabla clients
print("\nMetodo DELETE - Elimina de la tabla clients")

with conn:
    c.execute("DELETE FROM clients WHERE first_name = 'Catalina' AND last_name = 'Dapena'")

c.execute("SELECT * FROM clients")
print(c.fetchall())

# SELECT = Selecciona en la tabla clients
print("\nMetodo SELECT - Selecciona un cliente de la tabla clients")

c.execute("SELECT * FROM clients WHERE first_name = 'Kevin' AND last_name = 'Harnan'")
print(c.fetchall())
