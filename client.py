# client
import time
import json
import socket


def read_unsent_mb_data():
    # Abrir el archivo en modo de lectura
    archivo = open("/home/xavier_garrigos_tempelgroup/unsent_data/unsent_data_4_frames.txt", "r")
    #archivo = open("C:\\Users\\BATECNIC01\\PycharmProjects\\Modbus\\4_frames.txt", "r")

    # Leer y mostrar el contenido del archivo
    contenido = archivo.read()
    # Cerrar el archivo
    archivo.close()

    contenido = contenido.strip()

    return contenido


def read_new_mb_data():
    mb_data = "{\"time\":444,\"values\":[4984,10000,1000,560,600,0,0,2048]}"

    return mb_data


def send_mb_data_via_tcp(unsent_mb_data, new_mb_data):
    host1 = "34.121.116.90"
    host2 = "192.168.1.2"
    puerto = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host2, puerto))
    msg = unsent_mb_data + new_mb_data
    cliente_socket.sendall(msg.encode('utf-8'))
    print(msg)


if __name__ == "__main__":
    unsent_mb_data = read_unsent_mb_data()
    new_mb_data = read_new_mb_data()
    send_mb_data_via_tcp(unsent_mb_data, new_mb_data)
