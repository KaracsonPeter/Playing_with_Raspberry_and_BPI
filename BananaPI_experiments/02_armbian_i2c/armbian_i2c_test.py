import smbus
import time

bus = smbus.SMBus(2)  # bus number

# Read example
address = 0
while address <= 127:
        try:
                data = bus.read_byte(address)
                print(f"Received: {data} from addr {address}")
                time.sleep(0.1)

        except:
                print(f"Could not find device under {address}")
        address += 1
        