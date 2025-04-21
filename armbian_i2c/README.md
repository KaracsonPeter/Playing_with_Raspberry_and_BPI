Seems like Armbian does not support Banana PI M2 Berry for I2C communication on its pins.

```bash
sudo apt install i2c-tools python3-smbus
sudo armbian-config
# Navigate: System → Hardware → enable i2cX (e.g. i2c0 or i2c1)
# This is where I cannot even find my chip A40i-H. The closest to it is R40 but it also has limited options.
# In /dev there's only i2c-0 and i2c-1, but I do not have such options in the kernel.
sudo i2cdetect -y 1  # use correct bus number

python3 armbian_i2c_test.py
```