from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('narada')
print(client.get_list_database())
client.switch_database('narada')