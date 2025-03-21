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

def create_user(nombre, telefono, email, ciudad, direccion):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuarios (nombre, telefono, email, ciudad, direccion) VALUES (?, ?, ?, ?, ?)", 
                   (nombre, telefono, email, ciudad, direccion))

    conn.commit()
    conn.close()

    print(f"Usuario {nombre} agregado correctamente.")



def read_users():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()

    if usuarios:
        print("Lista de usuarios:")
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios en la base de datos.")




def update_phone(user_id, new_phone):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE usuarios SET telefono = ? WHERE id = ?", (new_phone, user_id))

    if cursor.rowcount > 0:
        print(f"Teléfono actualizado correctamente para el usuario con ID {user_id}.")
    else:
        print(f"No se encontró el usuario con ID {user_id}.")

    conn.commit()
    conn.close()



def update_email(user_id, new_email):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (new_email, user_id))

    if cursor.rowcount > 0:
        print(f"Email actualizado correctamente para el usuario con ID {user_id}.")
    else:
        print(f"No se encontró el usuario con ID {user_id}.")

    conn.commit()
    conn.close()


def update_full(user_id, new_phone, new_email, new_city, new_address):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE usuarios 
        SET telefono = ?, email = ?, ciudad = ?, direccion = ? 
        WHERE id = ?
    """, (new_phone, new_email, new_city, new_address, user_id))

    if cursor.rowcount > 0:
        print(f"Datos actualizados correctamente para el usuario con ID {user_id}.")
    else:
        print(f"No se encontró el usuario con ID {user_id}.")

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))

    if cursor.rowcount > 0:
        print(f"Usuario con ID {user_id} eliminado correctamente.")
    else:
        print(f"No se encontró el usuario con ID {user_id}.")

    conn.commit()
    conn.close()



