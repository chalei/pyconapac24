import machine
import time
import json

# Initialize UART interface
uart = machine.UART(1, baudrate=921600, tx=43, rx=44)
uart.init(baudrate=921600, rxbuf=32 * 1024)

# Function to send AT command and parse the response
def send_at_command(command, timeout=2000):
    uart.write(command + '\r\n')  # Send command with CRLF ending
    time.sleep_ms(timeout)  # Wait for the response (adjust timeout as needed)
    
    response = uart.read()  # Read the response from the device
    if response:
        try:
            response_decoded = response.decode('utf-8')  # Decode response
            print('Raw Response:', response_decoded)

            # Split response by newline or other delimiter if necessary
            json_objects = response_decoded.split('\n')

            for obj in json_objects:
                obj = obj.strip()  # Remove extra whitespace or newline
                if obj:  # Skip empty strings
                    try:
                        json_data = json.loads(obj)
                        print('Parsed JSON:', json_data)
                        
                        # Check if the JSON object contains 'boxes'
                        if "data" in json_data and "boxes" in json_data["data"]:
                            boxes = json_data["data"]["boxes"]
                            print("Boxes:", boxes)
                            # You can now access individual boxes here
                            # For example, accessing the first box:
                            if len(boxes) > 0:
                                first_box = boxes[0]
                                print("First box:", first_box)
                                print("total detection: ", len(boxes))

                    except ValueError:
                        print('Invalid JSON format:', obj)

            return json_objects
        
        except:
            # If decoding fails, return the raw byte response
            print('Failed to decode the response.')
            return response  # Return raw byte response
    else:
        print('No response received.')
        return b'No response'

# Example: Send AT command to invoke a command (replace with the desired AT command)
while True:
    response = send_at_command('AT+INVOKE=1,0,1')
    print('Processed Response:', response)
    time.sleep(2)  # Pause before the next command
