import hid
import psutil
import time
from threading import Event, Thread

def get_cpu_temp():
    try:
        temps = psutil.sensors_temperatures()
        k10 = temps.get('k10temp')
        if not k10:
            raise KeyError
        return k10[0].current
    except KeyError:
        return None

VENDOR_ID  = 0xAA88
PRODUCT_ID = 0x8666

try:
    device = hid.Device(VENDOR_ID, PRODUCT_ID)
except IOError:
    exit(1)

def write_to_cpu_fan_display(dev):
    temp = get_cpu_temp()
    if temp is None:
        return
    data = bytes([0, int(temp)])
    try:
        dev.write(data)
    except IOError:
        pass

def call_repeatedly(interval, func, *args, **kwargs):
    stopped = Event()
    def loop():
        while not stopped.wait(interval):
            func(*args, **kwargs)
    Thread(target=loop, daemon=True).start()
    return stopped.set

cancel = call_repeatedly(1.0, write_to_cpu_fan_display, device)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    cancel()
    device.close()
