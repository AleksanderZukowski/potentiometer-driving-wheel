import serial
import uinput

# Create a virtual gamepad joystick
device = uinput.Device([
    uinput.ABS_X + (-5120, 5120, 0, 0),  # Define X-axis range
    uinput.ABS_Y + (0, 255, 0, 0)  # Define Y-axis range
    #uinput.BTN_JOYSTICK,            # Define joystick button
    #uinput.BTN_TRIGGER              # Define trigger button
])

# Open serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the serial port as needed

while True:
    # Read data from serial port
    data = ser.readline().strip().decode('utf-8')
    sensor_value = int(data)-511
    
    # Map sensor value to joystick X-axis range
    joystick_x = int((sensor_value*sensor_value*1/512*(-1 if sensor_value<1 else
                                                      1))*10)  # Assuming potentiometer values range from 0 to 1023
    print(sensor_value,joystick_x) 
    # Emit joystick event
    device.emit(uinput.ABS_X, joystick_x, syn=False)
    device.syn()

