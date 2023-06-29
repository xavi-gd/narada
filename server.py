# server
import time
import json
import socket
from influxdb import InfluxDBClient


class MySocket:

    def __init__(self, sock=None):
        self.MSGLEN = 1024
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < self.MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            while chunk:
                bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


def receive_mb_data_via_tcp():
    _FRAME_QTY = 3
    _FRAME_LEN = 4

    host1 = "34.121.116.90"
    host2 = "192.168.1.2"
    puerto = 12345

    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((host2, puerto))
    # become a server socket
    serversocket.listen(5)

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        chunks = []
        msg = clientsocket.recv(1024)
        msg = msg.decode()
        print(msg)
        print("aceptada")
        #modules = msg.split('}')
        delimiter = "}"
        my_list = [x + delimiter for x in msg.split(delimiter) if x]
        print(my_list)

        client = InfluxDBClient(host='localhost', port=8086)
        client.create_database('abertis')
        client.get_list_database()
        client.switch_database('abertis')
        json_body = [
            {
                "measurement": "rack1",
                "tags": {
                "pack_id": "39",
                },
                "fields": {
                    "voltage": 61,
                    "current": 100,
                    "remain_capacity": 200,
                    "average_cell_temp": 120,
                    "environment_temp": 120,
                    "warning_flag": 0,
                    "protection_flag": 0,
                    "fault/status": 0,
                    "SOC": 100,
                    "circulate_number": 0,
                    "SOH": 100,
                    "PCB_Temp": 120,
                    "history_discharge_capacity": 0,
                    "cell_num": 16,
                    "cell_voltage_0": 5,
                    "cell_voltage_1": 5,
                    "cell_voltage_2": 5,
                    "cell_voltage_3": 5,
                    "cell_voltage_4": 5,
                    "cell_voltage_5": 5,
                    "cell_voltage_6": 5,
                    "cell_voltage_7": 5,
                    "cell_voltage_8": 5,
                    "cell_voltage_9": 5,
                    "cell_voltage_10": 5,
                    "cell_voltage_11": 5,
                    "cell_voltage_12": 5,
                    "cell_voltage_13": 5,
                    "cell_voltage_14": 5,
                    "cell_voltage_15": 5,
                    "temp_num": 16,
                    "temp_cell_0": 120,
                    "temp_cell_1": 120,
                    "temp_cell_2": 120,
                    "temp_cell_3": 120,
                    "temp_cell_4": 120,
                    "temp_cell_5": 120,
                    "temp_cell_6": 120,
                    "temp_cell_7": 120,
                    "temp_cell_8": 120,
                    "temp_cell_9": 120,
                    "temp_cell_10": 120,
                    "temp_cell_11": 120,
                    "temp_cell_12": 120,
                    "temp_cell_13": 120,
                    "temp_cell_14": 120,
                    "temp_cell_15": 120,
                    "full_capacity": 200,
                    "remain_charge_time": 0,
                    "remain_discharge_time": 0,
                    "cell_under_voltage_state": 0
                }
            },
            {
                "measurement": "rack1",
                "tags": {
                    "pack_id": "39",
                },
                "fields": {
                    "voltage": 61,
                    "current": 100,
                    "remain_capacity": 200,
                    "average_cell_temp": 120,
                    "environment_temp": 120,
                    "warning_flag": 0,
                    "protection_flag": 0,
                    "fault/status": 0,
                    "SOC": 100,
                    "circulate_number": 0,
                    "SOH": 100,
                    "PCB_Temp": 120,
                    "history_discharge_capacity": 0,
                    "cell_num": 16,
                    "cell_voltage_0": 5,
                    "cell_voltage_1": 5,
                    "cell_voltage_2": 5,
                    "cell_voltage_3": 5,
                    "cell_voltage_4": 5,
                    "cell_voltage_5": 5,
                    "cell_voltage_6": 5,
                    "cell_voltage_7": 5,
                    "cell_voltage_8": 5,
                    "cell_voltage_9": 5,
                    "cell_voltage_10": 5,
                    "cell_voltage_11": 5,
                    "cell_voltage_12": 5,
                    "cell_voltage_13": 5,
                    "cell_voltage_14": 5,
                    "cell_voltage_15": 5,
                    "temp_num": 16,
                    "temp_cell_0": 120,
                    "temp_cell_1": 120,
                    "temp_cell_2": 120,
                    "temp_cell_3": 120,
                    "temp_cell_4": 120,
                    "temp_cell_5": 120,
                    "temp_cell_6": 120,
                    "temp_cell_7": 120,
                    "temp_cell_8": 120,
                    "temp_cell_9": 120,
                    "temp_cell_10": 120,
                    "temp_cell_11": 120,
                    "temp_cell_12": 120,
                    "temp_cell_13": 120,
                    "temp_cell_14": 120,
                    "temp_cell_15": 120,
                    "full_capacity": 200,
                    "remain_charge_time": 0,
                    "remain_discharge_time": 0,
                    "cell_under_voltage_state": 0
                }
            }
        ]
        
        flag = client.write_points(json_body)
        print(flag)

        #client.write_points(json_body)
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        #ct = client_thread(clientsocket)
        #ct.run()


if __name__ == "__main__":
    receive_mb_data_via_tcp()
        
