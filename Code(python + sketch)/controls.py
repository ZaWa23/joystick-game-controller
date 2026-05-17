import serial
import pyautogui
import time

arduino = serial.Serial('COM3', 9600)

X_CENTER = 510
Y_CENTER = 510
DEADZONE = 80

last_time = 0
COOLDOWN = 0.25

while True:
    data = arduino.readline().decode().strip()

    try:
        raw_x, raw_y = map(int, data.split(","))

        vertical = raw_x      # UP/DOWN
        horizontal = raw_y    # LEFT/RIGHT

    except:
        continue

    now = time.time()

    if now - last_time > COOLDOWN:

        # LEFT / RIGHT → uses Y axis
        if horizontal < Y_CENTER - DEADZONE:
            pyautogui.press('left')
            last_time = now

        elif horizontal > Y_CENTER + DEADZONE:
            pyautogui.press('right')
            last_time = now

        # UP / DOWN → uses X axis
        elif vertical < X_CENTER - DEADZONE:
            pyautogui.press('down')
            last_time = now

        elif vertical > X_CENTER + DEADZONE:
            pyautogui.press('up')
            last_time = now
