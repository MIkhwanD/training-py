import os
import time

# jika gpio belum diaktifkan 
# os.system("echo 4 > /sys/class/gpio/export")
# os.system("echo out > /sys/class/gpio/gpio4/direction")

while True:
    try:
        os.system("echo 1 > /sys/class/gpio/gpio4/value")
        os.system("cat /sys/class/gpio/gpio4/value")
        time.sleep(1)
        os.system("echo 0 > /sys/class/gpio/gpio4/value")
        os.system("cat /sys/class/gpio/gpio4/value")
        time.sleep(1)

    except KeyboardInterrupt:
        os.system("echo 0 > /sys/class/gpio/gpio4/value")
        print("Programm Stopped")
        break

