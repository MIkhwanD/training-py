import board
import adafruit_mlx90614
import time

i2c = board.I2C()  # uses board.SCL and board.SDA
mlx = adafruit_mlx90614.MLX90614(i2c)

# temperature results in celsius
print("Ambent Temp: ", "         Object Temp:")

while True:
    try:
        print(mlx.ambient_temperature, "   ", mlx.object_temperature)
        time.sleep(.5)
    except KeyboardInterrupt:
        break