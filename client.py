# client
import time
import json
import socket


def read_unsent_mb_data():
    # Abrir el archivo en modo de lectura
    # archivo = open("/home/xavier_garrigos_tempelgroup/unsent_data/unsent_data_4_frames.txt", "r")
    archivo = open("C:\\Users\\BATECNIC01\\PycharmProjects\\Modbus\\4_frames.txt", "r")

    # Leer y mostrar el contenido del archivo
    contenido = archivo.read()
    print(contenido)

    # Cerrar el archivo
    archivo.close()

    objetos_json_str = contenido.split('$')
    objetos_json = [json.loads(objeto_str) for objeto_str in objetos_json_str]
    return objetos_json_str

def read_new_mb_data():
    new_mb_data = "{\"time\":444,\"values\":[4984,10000,1000,560,600,0,0,2048]}"
    return new_mb_data

def send_mb_data_via_tcp(unsent_mb_data, new_mb_data):
    FRAME_QTY = 3
    FRAME_LEN = 4
    host = "localhost"
    puerto = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, puerto))
    cliente_socket.sendall(new_mb_data.encode())


if __name__ == "__main__":
    unsent_mb_data = read_unsent_mb_data()
    print
    new_mb_data = read_new_mb_data()
    send_mb_data_via_tcp(unsent_mb_data, new_mb_data)
