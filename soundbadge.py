import badger2040
from pimoroni_i2c import PimoroniI2C
from time import sleep_ms
from math import log

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}

L_I2C_ADDR = 0x38
L_CMD_GET_VALUE = b"\x05"
L_CMD_LED_ON = b"\x01"
L_CMD_LED_OFF = b"\x00"

B_LED_BRIGHTNESS = 0x19
B_LED_PULSE_GRANULARITY = 0x1A
B_LED_PULSE_CYCLE_TIME = 0x1B
B_LED_PULSE_OFF_TIME = 0x1D
B_I2C_ADDRESS = 0x6F
    
NORMAL_IMAGE = bytearray(int(badger2040.WIDTH * badger2040.HEIGHT / 8))
ABNORMAL_IMAGE = bytearray(int(badger2040.WIDTH * badger2040.HEIGHT / 8))

try:
    open("loudness_normal.bin", "rb").readinto(NORMAL_IMAGE)
except OSError:
    try:
        import normal_image
        NORMAL_IMAGE = bytearray(normal_image.data())
        del normal_image
    except ImportError:
        pass
try:
    open("loudness_abnormal.bin", "rb").readinto(ABNORMAL_IMAGE)
except OSError:
    try:
        import abnormal_image
        ABNORMAL_IMAGE = bytearray(abnormal_image.data())
        del abnormal_image
    except ImportError:
        pass

i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
display = badger2040.Badger2040()
display.led(255)
display.update_speed(badger2040.UPDATE_FAST)
display.image(NORMAL_IMAGE, badger2040.WIDTH, badger2040.HEIGHT, 0, 0)
display.update()
display.font("sans")
display.thickness(2)
display.update_speed(badger2040.UPDATE_TURBO)
sleep_ms(100)
display.led(0)

def get_loudness_value():
    i2c.writeto(L_I2C_ADDR, L_CMD_GET_VALUE)
    data = []
    data = i2c.readfrom(L_I2C_ADDR, 2)
    adc_value_l = data[0]
    adc_value_h = data[1]
    adc_value = adc_value_h << 8
    adc_value |= adc_value_l
    adc_value &= 0b0000001111111111
    db = 16.801 * log(adc_value / 1023.0) + 9.872
    return db

def turnon_loudness_led():
    i2c.writeto(L_I2C_ADDR, L_CMD_LED_ON)
    
def turnoff_loudness_led():
    i2c.writeto(L_I2C_ADDR, L_CMD_LED_OFF)

def turnon_button_led(brightness):
    i2c.writeto(B_I2C_ADDRESS, bytes([B_LED_BRIGHTNESS, brightness, B_LED_PULSE_CYCLE_TIME, 0, 0, B_LED_PULSE_OFF_TIME, 0, 0, B_LED_PULSE_GRANULARITY, 1]))

def turnoff_button_led():
    i2c.writeto(B_I2C_ADDRESS, bytes([B_LED_BRIGHTNESS, 0, B_LED_PULSE_CYCLE_TIME, 0, 0, B_LED_PULSE_OFF_TIME, 0, 0, B_LED_PULSE_GRANULARITY, 1]))

while True:
    avg_db = 0
    for num in range(5):
        db = get_loudness_value()
        avg_db += db
        turnon_loudness_led()
        sleep_ms(50)
        turnoff_loudness_led()
        sleep_ms(50)
    avg_db /= 5
    if (avg_db > 2):
        turnon_button_led(128)
        display.update_speed(badger2040.UPDATE_FAST)
        display.image(ABNORMAL_IMAGE, badger2040.WIDTH, badger2040.HEIGHT, 0, 0)
        display.text("{:+.1f}".format(avg_db), 240, 30, 0.5)
        display.update()
        sleep_ms(2900)
        turnoff_button_led()
        sleep_ms(100)
        display.image(NORMAL_IMAGE, badger2040.WIDTH, badger2040.HEIGHT, 0, 0)
        display.update()
        display.update_speed(badger2040.UPDATE_TURBO)
    else:
        display.pen(15)
        display.clear()
        display.pen(0)
        display.text("{:+.1f}".format(avg_db), 240, 30, 0.5)
        display.partial_update(240, 16, 48, 24)
