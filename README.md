# zerosensor2
Temperature and Humidity Monitor for HTU21U &amp; Pi Zero

* zerosensor-sqlite.py will log sensor data every minute (sensor.db)
* zerosensor-nvd3.py will graph the data (dont work atm)
* zerosensor-httpd.py will start a http server on 8080


**Required Software**

* abyz pigpiod http://abyz.me.uk/rpi/pigpio/pigpiod.html
* dalexgray htu21df https://github.com/dalexgray/RaspberryPI_HTU21DF

**systemd**

* sudo cp systemd/zerosensor-httpd.service /etc/systemd/system/
* sudo cp systemd/zerosensor-sqlite.service /etc/systemd/system/
* sudo systemctl enable zerosensor-httpd 
* sudo systemctl enable zerosensor-sqlite
* sudo systemctl status zerosensor-httpd zerosensor-sqlite

if they dont work you didnt install it in /home/pi/zerosensor2
