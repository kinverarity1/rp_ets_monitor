import sqlite3

db = sqlite3.connect('data.db')

cursor = db.cursor()

cursor.execute("""
CREATE TABLE "sensor_readings" (
	"id"	INTEGER NOT NULL UNIQUE,
	"sensor_timestamp"	TEXT NOT NULL,
	"sensor"	TEXT NOT NULL,
	"sensor_value"	NUMERIC NOT NULL,
	"posted_to_api"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""
)