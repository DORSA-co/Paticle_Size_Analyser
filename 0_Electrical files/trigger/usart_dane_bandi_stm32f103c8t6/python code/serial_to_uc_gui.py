import serial
import tkinter as tk

# Function to send packets
def send_packets(event=None):
    try:
        entered_number = packet_entry.get("1.0", "end-1c").strip()
        if not entered_number.isdigit():
            raise ValueError("Invalid input. Please enter a number.")
        
        # Pad the entered number with zeros to make it 4 digits
        padded_number = entered_number.zfill(4)
        
        packet_data = padded_number.encode()
        ser.write(packet_data)
        sent_label.config(text=f'Sent: {packet_data.decode()}')

        # Clear the text entry widget after sending
        packet_entry.delete("1.0", "end")
    except Exception as e:
        pass

# Function to toggle "Always on Top" status
def toggle_always_on_top():
    window.attributes("-topmost", not window.attributes("-topmost"))

# Function to close the serial port and the application
def close_application():
    try:
        ser.close()
    except:
        pass
    window.destroy()

# Create a Tkinter window
window = tk.Tk()
window.title("Serial Packet Sender")

# Create and configure a label
sent_label = tk.Label(window, text="", padx=10, pady=10)
sent_label.pack()

# Create a multiline text entry widget for packets
packet_entry = tk.Text(window, height=4, width=40)
packet_entry.pack(pady=10)

# Bind the Enter key to send_packets function
packet_entry.bind("<Return>", send_packets)

# Create a button to send packets
send_button = tk.Button(window, text="Send Packet", command=send_packets)
send_button.pack()

# Create a button to toggle "Always on Top" status
always_on_top_button = tk.Button(window, text="Always on Top", command=toggle_always_on_top)
always_on_top_button.pack()

# Create a button to close the application
close_button = tk.Button(window, text="Close", command=close_application)
close_button.pack()

# Open the serial port (default COM port changed to COM3)
ser = serial.Serial('COM3', 115200)  # Change 'COM3' to the appropriate serial port on your system

# Run the Tkinter main loop
window.mainloop()