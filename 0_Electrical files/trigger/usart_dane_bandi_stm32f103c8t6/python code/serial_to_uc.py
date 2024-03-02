import serial

# Define the serial port and baud rate
ser = serial.Serial('COM5', 115200)  # Change 'COM1' to the appropriate serial port on your system

# Define your packets (replace these with your actual packet data)
packets = [
    b'0500',
]

try:
    # Send the packets
    for packet in packets:
        ser.write(packet)
        print(f'Sent: {packet.decode()}')
    
    # Close the serial port
    ser.close()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    ser.close()