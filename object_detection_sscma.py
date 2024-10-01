import time
from AISSCMA import create_sscma

# Create an instance of the SSCMA class
sscma = create_sscma()

# Example function to detect objects and print the number of objects detected
def detect_objects():
    # Send the AT command to invoke the detection (modify the AT command as needed)
    response_data = sscma.send_at_command('AT+INVOKE=1,0,1', timeout=2000)
    
    # Extract the boxes from the response
    boxes = sscma.get_boxes(response_data)
    
    # Print out the number of objects detected (length of boxes array)
    if boxes:
        print("Number of objects detected:", len(boxes))
    else:
        print("No objects detected.")

# Main loop to repeatedly check for objects (or call once if needed)
while True:
    detect_objects()
    time.sleep(1)  # Wait for 5 seconds before the next command
