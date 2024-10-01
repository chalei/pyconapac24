#not finished yet

import machine
import time
import json

# Initialize UART interface (replace with correct UART port and baud rate)
uart = machine.UART(1, baudrate=921600, tx=43, rx=44)
uart.init(baudrate=921600, rxbuf=32 * 1024)

# Send an AT command
def send_at_command(command, timeout=2000):
    uart.write(command + '\r\n')  # Send command with CRLF ending
    time.sleep_ms(timeout)  # Wait for the response (adjust timeout as needed)
    response = uart.read().decode('utf-16')  # Read the response from the device
    json_data = json.loads(response)
    print('Response:', response)
    print('Sliced:', json_data)
    return response if response else b'No response'

# Example: Send AT command to check if the device is responding
#response = send_at_command('AT+NAME?')
while True:
    send_at_command('AT+INVOKE=1,0,1')
