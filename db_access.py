from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.create_database('test')
print(client.get_list_database())
client.switch_database('test')
json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-30T8:02:00Z",
        "fields": {
            "duration": 129
        }
    }
]
flag = client.write_points(json_body)
if not flag:
    print("ERROR in the client write.write_points")

results = client.query('SELECT "duration" FROM "test"')
#results = client.query('SELECT * FROM "test"')
print(results)
points = results.get_points(tags={'user':'Carol'})
for point in points:
    print("Time: %s, Duration: %i" % (point['time'], point['duration']))
