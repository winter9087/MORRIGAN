from ph_read import *
from temp_read import *
from do_read import *
from tds_read import *
from turbidity_read import *
import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import os
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c, 0x08)

temperature = read_temp()
def switch_sensor(sensor):
    if sensor == ph:
        ads.gain = 1
        chan = AnalogIn(ads, ADS.P3)
    elif sensor == TDS: 
        ads.gain = 1
        chan = AnalogIn(ads, ADS.P0)
    elif sensor == turbidity: 
        ads.gain = 1
        chan = AnalogIn(ads, ADS.P1)
    elif sensor == DO:
        ads.gain = 1
        chan = AnalogIn(ads, ADS.P2)
    else: 
        raise ValueError("Invalid sensor type passed to switch_sensor")
    
    return chan













while True:
    temp = read_temp()
    log_data("temperature", temp)
    
    ph_channel = switch_sensor("ph")
    ph_value = read_PH(ph_channel.voltage)
    log_data("PH", ph_value)
    time.sleep(15 / 60)

    TDS_channel = switch_sensor("TDS")
    EC_value = read_EC(TDS_channel.voltage)
    log_data("EC", EC_value)
    TDS_value = read_TDS(TDS_channel.voltage)
    log_data("TDS", TDS_value)
    time.sleep(15 / 60)

    turbidity_channel = switch_sensor("turbidity")
    turbidity_value = read_turbidity(turbidity_channel.voltage)
    log_data("turbidity", turbidity_value)
    time.sleep(15 / 60)
    
    DO_channel = switch_sensor("DO")
    DO_value = read_DO(DO_channel.voltage)
    log_data("DO", DO_value)
    time.sleep(15 / 60)