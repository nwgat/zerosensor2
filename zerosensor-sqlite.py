# zerosensor sqlite
# http://nwgat.ninja

import sys
import arrow
import time
import HTU21DF
import sqlite3

while True:
	# create db
        db = sqlite3.connect('sensor.db')
        cursor = db.cursor()

	# sensor reading
	temp = HTU21DF.read_temperature()
	time.sleep(1)
	hum = HTU21DF.read_humidity()

	# arrow on time
	local = arrow.now()

	# keeping time (standard)
	st = arrow.now()

        # keeping time (unix time)
        ut = local.timestamp

	#print temp, hum, ut, st

	# insert into sqlite db
	db.execute("""CREATE table IF NOT EXISTS data (temp int, hum int, ut int)""")
	db.execute("INSERT INTO data (temp, hum, ut) values (?, ?, ?)",
            (temp, hum, ut))
        db.commit()
	db.close()

	# time delay for reading from sensors
	time.sleep(60)
	#time.sleep(4)
