# narada

## narada-server Virtual Machine on Google Cloud Platform
- Image Version: Ubuntu, 20.04 LTS
- Architecture: x86‑64

## credentials

## Node-RED

### Installation
- url: https://nodered.org/docs/getting-started/raspberrypi
- commands:
1. `bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`

## Influx DB

### Installation
- url: https://docs.influxdata.com/influxdb/v1.8/introduction/install/
- commands:
1. `curl -s https://repos.influxdata.com/influxdata-archive_compat.key > influxdata-archive_compat.key`
2. `echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null`
3. `echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list`
