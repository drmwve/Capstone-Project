import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simple_pid import PID
from w1thermsensor import W1ThermSensor, Unit, Sensor
from gpiozero import PWMOutputDevice

MAX_DATA_POINTS = 30
HEATING_ELEMENT_GPIO = 25

# Create figure for plotting
start_time = time.time()
last_time = start_time
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
pidvalues = []
setpoint = []
power = 0

tempsensor = W1ThermSensor(Sensor.DS18B20, "3c01d607c246")
heatingelement = PWMOutputDevice(HEATING_ELEMENT_GPIO)
temperature = 0
pid = PID(40/100, 1/100, 3/100, setpoint=135, sample_time=None)
pid.output_limits = (0, 1)

# This function is called periodically from FuncAnimation
def animate(i, xs, ys, setpoint, pidvalues):
    xs.append(datetime.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temperature)
    setpoint.append(pid.setpoint)
    pidvalues.append(heatingelement.value)
    # Limit x and y lists to 20 items
    xs = xs[-MAX_DATA_POINTS:]
    ys = ys[-MAX_DATA_POINTS:]
    pidvalues = pidvalues[-MAX_DATA_POINTS:]
    setpoint = setpoint[-MAX_DATA_POINTS:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label='measured')
    ax.plot(xs, setpoint, label='target')
    #ax.plot(xs, pidvalues)
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')

if __name__ == '__main__':

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, setpoint, pidvalues), interval=1000)
    while True:

        # Add x and y to lists
        temperature = tempsensor.get_temperature(Unit.DEGREES_F)

        if temperature < pid.setpoint: 
            heatingelement.value = pid(temperature)
        else:
            heatingelement.value = 0
            pid._integral = 0
        plt.draw()
        plt.pause(0.001)
        print(heatingelement.value)



