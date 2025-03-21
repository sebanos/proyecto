import sqlite3  


conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL,
    email TEXT NOT NULL,
    ciudad TEXT NOT NULL,
    direccion TEXT NOT NULL
)
""")


conn.commit()
conn.close()

print("Base de datos y tabla creadas correctamente.")

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()


usuarios = [
    ("Carlos Pérez", "1234567890", "carlos@gmail.com", "Bogotá", "Calle 10 #5-30"),
    ("Ana Gómez", "9876543210", "ana@hotmail.com", "Medellín", "Carrera 45 #12-50"),
    ("Luis Fernández", "3216549870", "luis@yahoo.com", "Cali", "Av. Siempre Viva 742"),
    ("María Rodríguez", "6549873210", "maria@gmail.com", "Cartagena", "Cll 25 #6-89"),
    ("Javier Suárez", "7894561230", "javier@outlook.com", "Bucaramanga", "Cra 9 #15-20"),
    ("Laura Méndez", "8529637410", "laura@live.com", "Pereira", "Cll 18 #4-56")
]


cursor.executemany("INSERT INTO usuarios (nombre, telefono, email, ciudad, direccion) VALUES (?, ?, ?, ?, ?)", usuarios)


conn.commit()
conn.close()

print("Usuarios insertados correctamente.")


def mostrar_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(usuario)

    conn.close()

mostrar_usuarios()
