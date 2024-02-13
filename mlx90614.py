import board
import adafruit_mlx90614
import time

i2c = board.I2C()  # uses board.SCL and board.SDA
mlx = adafruit_mlx90614.MLX90614(i2c)

# temperature results in celsius
while True:
    try:
        ambient_temp = f"{mlx.ambient_temperature:.2f}"
        object_temp = f"{mlx.object_temperature:.2f}"
        print("Ambient :", ambient_temp, " ", "Object :", object_temp)
        time.sleep(0.5)
    except KeyboardInterrupt:
        break

