from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('pytest')
print(client.get_list_database())
client.switch_database('pytest')
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "Float_value": 0.64,
            "Int_value": 3,
            "String_value": "Text",
            "Bool_value": True
        }
    }
]
flag = client.write_points(json_body)
if not flag:
    print("ERROR in the client write.write_points")
if flag:
    print("Write points TRUE\n")
results = client.query('SELECT * FROM pytest.autogen.cpu_load_short')

print(results)
points = results.get_points(tags={'user':'Carol'})
for point in points:
    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
