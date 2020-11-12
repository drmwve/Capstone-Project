import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from simple_pid import PID


class WaterBoiler:
    """
    Simple simulation of a water boiler which can heat up water
    and where the heat dissipates slowly over time
    """
    def __init__(self):
        self.water_temp = 20

    def update(self, boiler_power, dt):
        if boiler_power > 0:
            # boiler can only produce heat, not cold
            self.water_temp += 1 * boiler_power * dt

        # some heat dissipation
        self.water_temp -= 10 * dt
        return self.water_temp

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

boiler = WaterBoiler()
water_temp = boiler.water_temp
oneshot = False
pid = PID(3.5,0.6, 0.4, setpoint=water_temp, sample_time=None)
pid.output_limits = (0, 100)

# This function is called periodically from FuncAnimation
def animate(i, xs, ys, setpoint, pidvalues):
    xs.append(datetime.datetime.now().strftime('%M:%S.%f'))
    ys.append(water_temp)
    setpoint.append(pid.setpoint)
    pidvalues.append(power)
    # Limit x and y lists to 20 items
    xs = xs[-MAX_DATA_POINTS:]
    ys = ys[-MAX_DATA_POINTS:]
    pidvalues = pidvalues[-MAX_DATA_POINTS:]
    setpoint = setpoint[-MAX_DATA_POINTS:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label='measured')
    ax.plot(xs, setpoint, label='target')
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.ylabel('Temperature (deg C)')
    plt.ylim([0,100])

def desktoptest():
    global last_time, water_temp, setpoint, oneshot
    current_time = time.time()
    dt = current_time - last_time
    power = pid(water_temp)
    water_temp = boiler.update(power, dt)
    # print((pid.setpoint - water_temp) / pid.setpoint * 100)
    last_time = current_time
    if int(current_time) % 5 == 0:
        if oneshot:
            pid.setpoint = random.randint(50, 100)
            oneshot = False
    else:
        oneshot = True
    return water_temp

if __name__ == '__main__':

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, setpoint, pidvalues), interval=50)
    while True:
        plt.draw()
        plt.pause(0.001)

        desktoptest()



