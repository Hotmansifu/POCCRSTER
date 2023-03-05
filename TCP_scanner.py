import argparse
import socket
import threading
import tkinter as tk

class PortScannerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TCP Port Scanner")

        # Input frame
        input_frame = tk.Frame(self.master)
        input_frame.pack(padx=10, pady=10)

        tk.Label(input_frame, text="Target Host:").grid(row=0, column=0)
        self.host_entry = tk.Entry(input_frame)
        self.host_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Target Ports:").grid(row=1, column=0)
        self.ports_entry = tk.Entry(input_frame)
        self.ports_entry.grid(row=1, column=1)

        # Button
        tk.Button(self.master, text="Scan", command=self.run_scan).pack(pady=10)

        # Output frame
        output_frame = tk.Frame(self.master)
        output_frame.pack(padx=10, pady=10)

        tk.Label(output_frame, text="Scan Results:").grid(row=0, column=0)
        self.results_text = tk.Text(output_frame, width=50, height=10)
        self.results_text.grid(row=1, column=0)

    def run_scan(self):
        host = self.host_entry.get()
        port_list = self.ports_entry.get().split(",")  # Make a list from port numbers

        # Check if required arguments are present before running the scan
        if not host or not port_list:
            self.results_text.insert(tk.END, "Error: Target host and ports are required.")
            return

        self.results_text.delete(1.0, tk.END)  # Clear any previous results

        # Attempt to resolve target IP
        try:
            target_ip = socket.gethostbyname(host)
        except OSError:
            self.results_text.insert(tk.END, "Error: Could not resolve target host.")
            return

        try:
            target_name = socket.gethostbyaddr(target_ip)
            self.results_text.insert(tk.END, "Scan Results for: {}\n".format(target_name[0]))
        except OSError:
            self.results_text.insert(tk.END, "Scan Results for: {}\n".format(target_ip))

        # Scan each port in a separate thread and display results in the GUI
        for port in port_list:
            t = threading.Thread(target=self.connection_scan, args=(target_ip, int(port)))
            t.start()

    def connection_scan(self, target_ip, target_port):
        """Attempts to create a socket connection with the given IP address and port.
        If successful, the port is open. If not, the port is closed.
        """
        try:
            conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn_socket.connect((target_ip, target_port))
            conn_socket.send(b'Banner_query\r\n')
            self.results_text.insert(tk.END, "[+] {}/tcp open\n".format(target_port))
        except OSError:
            self.results_text.insert(tk.END, "[-] {}/tcp closed\n".format(target_port))
        finally:
            conn_socket.close()  # Ensure the connection is closed


if __name__ == '__main__':
    root = tk.Tk()
    ex = PortScannerGUI(root)
    root.mainloop()
