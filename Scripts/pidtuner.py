import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simple_pid import PID
from w1thermsensor import *
from gpiozero import PWMOutputDevice

MAX_DATA_POINTS = 30
HEATING_ELEMENT_GPIO = 12

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

tempsensor = W1ThermSensor.get_available_sensors()[0]
heatingelement = PWMOutputDevice(HEATING_ELEMENT_GPIO)
temperature = 0
pid = PID(5/100, 0.2/100, 0.35/100, setpoint=0, sample_time=None)
pid.output_limits = (0, 1)

# This function is called periodically from FuncAnimation
def animate(i, xs, ys, setpoint, pidvalues):
    xs.append(datetime.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temperature)
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
    ax.plot(xs, pidvalues)
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')

if __name__ == '__main__':

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, setpoint, pidvalues), interval=1000)
    while True:
        plt.draw()
        plt.pause(0.001)
        # Add x and y to lists
        temperature = tempsensor.get_temperature(W1ThermSensor.DEGREES_F)
        heatingelement.value = pid(temperature)



