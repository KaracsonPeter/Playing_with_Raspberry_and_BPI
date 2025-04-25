import smbus
import time

bus = smbus.SMBus(2)
HDC1080_ADDR = 40
HUMIDITY_REG = 0x05

percent_mask = 0b11111110
decimal_mask = 0b00000001

# Trigger humidity measurement
bus.write_byte(HDC1080_ADDR, HUMIDITY_REG)
time.sleep(0.1)  # Wait for measurement

bytes_to_read = 4
data = bus.read_i2c_block_data(HDC1080_ADDR, HUMIDITY_REG, bytes_to_read)
print(data)

raw_humidity = (data[0] << 8) | data[1]
humidity = (raw_humidity / 65536.0) * 100.0

print(f"Humidity: {humidity}")
