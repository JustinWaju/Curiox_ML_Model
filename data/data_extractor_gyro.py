from mpu9250_i2c import *
import math
import RPi.GPIO as GPIO
import time
import os

# © 2023 Maximilian Kaiser

led = 4
button = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(1)  # delay necessary to allow mpu9250 to settle

results = []

def userHomePath():
    return os.path.expanduser("~") + "/"

def writeToFile(result):
    with open(userHomePath() + "Desktop/sensordata_real.txt", "a") as file:
        file.write(f"{result}\n")
    print('{}'.format('-' * 30))
    print("WROTE COMPLETE RESULT TO FILE")
    print('{}'.format('-' * 30))

def getSensorValues():
    try:
        ax, ay, az, gx, gy, gz = mpu6050_conv()  # read and convert mpu6050 data
    except Exception as e:
        print(f"Exception occurred: {e}")

    # Adjust for the change in orientation (90 degrees on the X-Axis)
    roll = math.atan2(-ay, az)
    pitch = math.atan2(ax, math.sqrt(ay * ay + az * az))
    yaw = 180 * math.atan(gz / math.sqrt(gx * gx + gy * gy)) / math.pi

    print('{}'.format('-' * 30))
    print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(ax, ay, az))
    print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(gy, gx, gz))  # Swapped gx and gy
    print('roll: {0:2.2f}'.format(roll))
    print('pitch: {0:2.2f}'.format(pitch))

    axr = round(ax, 2)
    ayr = round(ay, 2)
    azr = round(az, 2)
    gyr = round(gy, 2)
    gxr = round(gx, 2)
    gzr = round(gz, 2)
    roll_r = round(roll, 2)
    pitch_r = round(pitch, 2)

    values = [str(axr), str(ayr), str(azr), str(gxr), str(gyr), str(gzr), str(roll_r), str(pitch_r)]
    return [values]

def recordMovement(channel):
    global results
    time.sleep(0.5)
    while True:
        GPIO.output(led, GPIO.HIGH)
        if len(results) == 10:
            results.append(choice)
            writeToFile(results)
            results = []
            break

        values = getSensorValues()
        results.extend(values)
    GPIO.output(led, GPIO.LOW)

GPIO.add_event_detect(button, GPIO.RISING, callback=recordMovement, bouncetime=1000)

print("Enter the type of the movement you want to record (e.g. throw-forward):")
choice = input("->")

value = 0
while True:
    try:
        value += 1
        time.sleep(1)
                
    except KeyboardInterrupt as e:
        print("interrupted by user.")
        GPIO.cleanup()
        exit(0)
