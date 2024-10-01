import machine
import time
import json

class SSCMA:
    def __init__(self, uart_port=1, baudrate=921600, tx=43, rx=44):
        self.uart = machine.UART(uart_port, baudrate=baudrate, tx=tx, rx=rx)
        self.uart.init(baudrate=baudrate, rxbuf=32 * 1024)

    def send_at_command(self, command, timeout=2000):
        """Send an AT command and return parsed JSON response"""
        self.uart.write(command + '\r\n')  # Send command with CRLF ending
        time.sleep_ms(timeout)  # Wait for the response
        
        response = self.uart.read()  # Read the response
        if response:
            try:
                response_decoded = response.decode('utf-8')  # Decode the response
                print('Raw Response:', response_decoded)
                
                # Split response by newline if there are multiple JSON objects
                json_objects = response_decoded.split('\n')

                parsed_jsons = []
                for obj in json_objects:
                    obj = obj.strip()  # Clean up any extra spaces or newlines
                    if obj:  # Avoid empty strings
                        try:
                            json_data = json.loads(obj)
                            parsed_jsons.append(json_data)
                        except ValueError:
                            print('Invalid JSON format:', obj)

                return parsed_jsons if parsed_jsons else None

            except:
                print('Failed to decode the response.')
                return None
        else:
            print('No response received.')
            return None

    def get_boxes(self, response_data):
        """Extract boxes from the JSON response"""
        boxes = []
        if response_data:
            for json_data in response_data:
                if "data" in json_data and "boxes" in json_data["data"]:
                    boxes.extend(json_data["data"]["boxes"])
        return boxes

# Create an instance of the SSCMA class
def create_sscma():
    return SSCMA()
