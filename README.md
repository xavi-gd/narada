# narada

## Virtual Machine on Google Cloud Platform
- name: narada-server 
- image Version: Ubuntu, 20.04 LTS
- architecture: x86‑64
- public IP: 35.232.56.17

## Credentials
- user: 
- password:

---

## Node-RED

### Installation
- url: https://nodered.org/docs/getting-started/raspberrypi
- default port: 1880
- current port: 1880
- commands:
  1. `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`
- autostart on boot
  1. `sudo systemctl enable nodered.service`
  2. `sudo service nodered enable`

---

## Influx DB

### Installation
- url: https://docs.influxdata.com/influxdb/v1.8/introduction/install/
- default port: 8086
- current port: 8086
- commands:
  1. `curl -s https://repos.influxdata.com/influxdata-archive_compat.key > influxdata-archive_compat.key
echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null`
  2. `echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list`
  3. `sudo apt-get update && sudo apt-get install influxdb`
  4. `sudo service influxdb start`

---

## Python3 and pip (ppackage installer)
- url: https://www.educative.io/answers/installing-pip3-in-ubuntu
- commands:
  1. `sudo apt-get -y install python3-pip`
  2. `pip3 --version`

---

## InfluxDB on Python - library
- url: https://www.influxdata.com/blog/getting-started-python-influxdb/
- commands:
  1. `python3 -m pip install influxdb`
  2. `python3`
  3. `from influxdb import InfluxDBClient`
  
 ### INSERT and SELECT data FROM database.autogen.key
 - url: https://www.influxdata.com/blog/getting-started-python-influxdb/

---

## Grafana
- url: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
- commands:
  1. `sudo apt-get install -y apt-transport-https`
  2. `sudo apt-get install -y software-properties-common wget`
  3. `sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key`
  4. `echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list`
  5. `sudo apt-get update`
  6. `sudo apt-get install grafana`
  7. `sudo systemctl enable grafana-server.service`
  8. `sudo systemctl daemon-reload`
  9. `sudo systemctl start grafana-server`
  10. `sudo systemctl status grafana-server`
  
 ### INSERT and SELECT data FROM database.autogen.key
 - url: https://www.influxdata.com/blog/getting-started-python-influxdb/
 
