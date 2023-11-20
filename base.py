import sqlite3
import pandas as pd
import socket
import time
import threading

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM main_menu_databasehumidity")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO main_menu_databasehumidity(data_date, data_value)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def insertar_datos(database, columna1, columna2):
    conexion = sqlite3.connect(database)
    cursor = conexion.cursor()

    table = ['temperature', 'humidity', 'nutrients', 'phosphorus'][int(columna2[0])]
    
    consulta = "INSERT INTO main_menu_database"+table+" (data_date, data_value) VALUES (?, ?)"

    valores = (columna1, columna2[1:])

    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        #print("Datos insertados correctamente. \n")

    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")

    finally:
        conexion.close()

def receive_data(client_socket, client_address):
    database = r"db.sqlite3"
    conn = create_connection(database)

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string

        with conn:
            # select_task_by_priority(conn, 1)
            insertar_datos("db.sqlite3", time.strftime("%H:%M:%S"), request)
            #select_all_tasks(conn) #Leer base de datos

        print(f"Received: {request}")

        response = "accepted".encode("utf-8") 
        client_socket.send(response)


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8001

    server.bind((server_ip, port))
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")
   
    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        threading.Thread(target=receive_data, args=(client_socket, client_address)).start()
    # close connection socket with the client
    # client_socket.close()
    # print("Connection to client closed")
    # close server socket
    # server.close()


if __name__ == '__main__':
    run_server()
