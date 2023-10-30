import tkinter as tk
import tkinter.ttk as ttk
import socket

class TcpClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TCP Client App")

        # Default values for IP address and port
        default_ip = "192.168.0.199"
        default_port = "8234"

        self.ip_label = tk.Label(root, text="Server IP:")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()
        self.ip_entry.insert(0, default_ip)  # Set default IP value

        self.port_label = tk.Label(root, text="Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()
        self.port_entry.insert(0, default_port)  # Set default port value

        self.connect_button = tk.Button(root, text="Connect to Server", command=self.connect_to_server)
        self.connect_button.pack()

        self.check_button = tk.Button(root, text="Connectivity Check", command=self.check_connectivity)
        self.check_button.pack()

        # Create four send packet text boxes and buttons
        self.packet_labels = []
        self.packet_entries = []
        self.send_buttons = []

        default_packet1 = "#1101012"
        default_packet2 = "#2101011"

        for i in range(4):
            packet_label = tk.Label(root, text=f"Send Packet {i + 1}:")
            packet_label.pack()
            self.packet_labels.append(packet_label)

            packet_entry = tk.Entry(root)
            packet_entry.pack()
            self.packet_entries.append(packet_entry)

            send_button = tk.Button(root, text=f"Send Data {i + 1}", command=lambda idx=i: self.send_string_packet(idx))
            send_button.pack()
            self.send_buttons.append(send_button)

        # Set default values for Send Packet 1 and Send Packet 2
        self.packet_entries[0].insert(0, default_packet1)
        self.packet_entries[1].insert(0, default_packet2)

        self.output_frame = ttk.Frame(root)
        self.output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.response_label = ttk.Label(self.output_frame, text="Server Response:")
        self.response_label.pack()

        self.response_text = tk.Text(self.output_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.response_text.pack(fill=tk.BOTH, expand=True)

        self.output_label = ttk.Label(root, text="")
        self.output_label.pack()

    def connect_to_server(self):
        server_ip = self.ip_entry.get()
        server_port = int(self.port_entry.get())

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((server_ip, server_port))
            self.output_label.config(text="Connected to server.")
        except Exception as e:
            self.output_label.config(text=f"Connection error: {str(e)}")

    def check_connectivity(self):
        if hasattr(self, 'client_socket'):
            self.output_label.config(text="Connected to server.")
        else:
            self.output_label.config(text="Not connected to server.")

    def send_string_packet(self, idx=0):
        if hasattr(self, 'client_socket'):
            packet_entry = self.packet_entries[idx]
            packet = packet_entry.get()
            try:
                self.client_socket.send(packet.encode('utf-8'))
                self.output_label.config(text=f"Sent packet {idx + 1}: {packet}")
                response = self.client_socket.recv(1024).decode('utf-8')
                self.display_response(response)
            except Exception as e:
                self.output_label.config(text=f"Error sending packet {idx + 1}: {str(e)}")
        else:
            self.output_label.config(text="Not connected to server.")

    def display_response(self, response):
        self.response_text.config(state=tk.NORMAL)
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)
        self.response_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TcpClientApp(root)
    root.mainloop()
