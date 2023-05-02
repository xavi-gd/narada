# narada

## Virtual Machine on Google Cloud Platform
- name: narada-server
- type: e2-micro
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

---

## Table Scheme
payment,device=mobile,product=Notepad,method=credit billed=33,licenses=3i 1434067467100293230

`rack1,module_id=39 key_1=1,key_2=2,key_3=3,key_4=4,key_5=5,key_6=6,key_7=7,key_8=8,key_9=9,key_10=10,key_11=11,key_12=12,key_13=13,key_14=14,key_15=15,key_16=16,key_17=17,key_18=18,key_19=19,key_20=20,key_21=21,key_22=22,key_23=23,key_24=24,key_25=25,key_26=26,key_27=27,key_28=28,key_29=29,key_30=30,key_31=31,key_32=32,key_33=33,key_34=34,key_35=35,key_36=36,key_37=37,key_38=38,key_39=39,key_40=40,key_41=41,key_42=42,key_43=43,key_44=44,key_45=45,key_46=46,key_47=47,key_48=48,key_49=49,key_50=50,key_51=51`

VM
/SdT)O=*Md=$|FG

RDP Windows server
rcwE|Se5S0fxt2A
 
