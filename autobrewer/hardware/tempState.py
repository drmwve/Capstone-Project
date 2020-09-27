from w1thermsensor import W1ThermSensor
import time

while True:     #this loop will keep displaying the temperature for all sensor with their respective IDs'            
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()*1.8+32))
        time.sleep(0.5)