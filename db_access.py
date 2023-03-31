from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('abertis')
print(client.get_list_database())
client.switch_database('abertis')
json_body = [
    {
        "measurement": "rack1",
        "tags": {
            "id": 39,
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "current_voltage": 0.64,
            "SOC": 54,
            "SOH": 47
        }
    },
{
        "measurement": "rack1",
        "tags": {
            "id": 40,
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "current_voltage": 0.23,
            "SOC": 100,
            "SOH": 99
        }
    }
]
flag = client.write_points(json_body)
if not flag:
    print("ERROR in the client write.write_points")
if flag:
    print("Write points TRUE\n")
results = client.query('SELECT * FROM abertis..rack1')

print(results)
points = results.get_points(tags={'user':'Carol'})
for point in points:
    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
