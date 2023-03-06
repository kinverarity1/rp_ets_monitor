import bme680
import time
import sqlite3
from mics6814 import MICS6814

db = sqlite3.connect('data.db')

gas_wired = 0
multi_wired = 1
pm_wired = 0

if gas_wired:
    gas = MICS6814(0x6f)

if multi_wired:
    sensor = bme680.BME680(0x76)
    #sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    #sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)

while True:
    record = {}

    if gas_wired:
        readings = gas.read_all()
        print(type(readings))
        print(readings)

    if multi_wired:
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            record['bme680_temp_c'] = sensor.data.temperature
            record['bme680_pressure'] = sensor.data.pressure
            record['bme680_humidity_pc'] = sensor.data.humidity
            record['bme680_gas_resist_kohms'] = sensor.data.gas_resistance / 1000

    if record:
        print(record)

    time.sleep(1)
