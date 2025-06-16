import psutil
import time

while True:
    battery = psutil.sensors_battery()
    print(f"Battery: {battery.percent}% | Plugged In: {battery.power_plugged}")
    time.sleep(5)  # refresh every 5 seconds
