import board
import busio
import digitalio
import time
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c)

pin14 = mcp.get_pin(14)
pin11 = mcp.get_pin(11)

pin14.direction = digitalio.Direction.OUTPUT
pin11.direction = digitalio.Direction.OUTPUT

while True:
    try:
        pin14.value = True
        time.sleep(.5)
        pin14.value = False
        time.sleep(.5)
        pin11.value = True
        time.sleep(.5)
        pin11.value = False
        time.sleep(.5)
    except KeyboardInterrupt:
        pin14.value = False
        pin11.value = False
        print("Done !")
        break