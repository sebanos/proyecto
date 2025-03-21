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


def menu():
    while True:
        print("\n📌 Menú de Usuarios")
        print("1. Crear un nuevo usuario")
        print("2. Mostrar todos los usuarios")
        print("3. Actualizar solo teléfono")
        print("4. Actualizar solo email")
        print("5. Actualizar todos los datos excepto ID y nombre")
        print("6. Eliminar usuario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            ciudad = input("Ciudad: ")
            direccion = input("Dirección: ")
            create_user(nombre, telefono, email, ciudad, direccion)

        elif opcion == "2":
            read_users()

        elif opcion == "3":
            user_id = input("ID del usuario: ")
            new_phone = input("Nuevo teléfono: ")
            update_phone(user_id, new_phone)

        elif opcion == "4":
            user_id = input("ID del usuario: ")
            new_email = input("Nuevo email: ")
            update_email(user_id, new_email)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            new_phone = input("Nuevo teléfono: ")
            new_email = input("Nuevo email: ")
            new_city = input("Nueva ciudad: ")
            new_address = input("Nueva dirección: ")
            update_full(user_id, new_phone, new_email, new_city, new_address)

        elif opcion == "6":
            user_id = input("ID del usuario a eliminar: ")
            delete_user(user_id)

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
