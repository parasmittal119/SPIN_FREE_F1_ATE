import serial
import time


serial_port = 'COM6'

ser = serial.Serial(serial_port, baudrate=9600, timeout=1)


def send_command(command):
    ser.write(command.encode())
    time.sleep(0.1)

#
# send_command("AUTOSET")
# send_command(":MEASure:SOURce1 CH1")
# send_command(":MEASure:RMS?")
# vrms_measurement = ser.readline().decode().strip()

ser.write(b':MEASure:RMS?')

ser.close()

# print(f"VRMS Measurement: {vrms_measurement} V")
