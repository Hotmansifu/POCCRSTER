import socket
import tkinter as tk
from tkinter import messagebox

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except:
        return None

def is_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return "open"
    except:
        return "closed or filtered"

def start_scan():
    host = None
    if choice.get() == 1:
        hostname = hostname_entry.get()
        host = get_ip_address(hostname)
        if host is None:
            messagebox.showerror("Error", "Unable to resolve hostname.")
            return
    elif choice.get() == 2:
        host = ip_entry.get()

    if port_choice.get() == 1:
        for port in range(1, 65535):
            result = is_open(host, port)
            if result == "open":
                result_list.insert(tk.END, "Port {} is {}".format(port, result))
            else:
                result_list.insert(tk.END, "Port {} is {}".format(port, result))
    elif port_choice.get() == 2:
        ports = ports_entry.get().split(',')
        if ports[0].strip() == '':
            messagebox.showerror("Error", "No ports entered.")
            return
        else:
            ports = [int(port) for port in ports]
            for port in ports:
                result = is_open(host, port)
                if result == "open":
                    result_list.insert(tk.END, "Port {} is {}".format(port, result))
                else:
                    result_list.insert(tk.END, "Port {} is {}".format(port, result))

root = tk.Tk()
root.title("Port Scanner")


background_image = tk.PhotoImage(file="background.gif")
background_label = tk.Label(root, image=background_image)
background_label.pack(fill="both", expand=True)

choice = tk.IntVar()

hostname_frame = tk.Frame(root)
hostname_frame.pack(pady=10)

tk.Radiobutton(hostname_frame, text="Website hostname", variable=choice, value=1).pack(side="left")
hostname_entry = tk.Entry(hostname_frame)
hostname_entry.pack(side="left", fill="x", expand=True)

ip_frame = tk.Frame(root)
ip_frame.pack(pady=10)

tk.Radiobutton(ip_frame, text="IP address", variable=choice, value=2).pack(side="left")
ip_entry = tk.Entry(ip_frame)
ip_entry.pack(side="left", fill="x", expand=True)

port_choice = tk.IntVar()
ports_description = tk.Label(root, text="Enter specific ports to be scanned (separated by commas):")
ports_description.pack(pady=10)


ports_frame = tk.Frame(root)
ports_frame.pack(pady=10)

ports_frame_label = tk.Frame(root)
ports_frame_label.pack(pady=10)


tk.Radiobutton(ports_frame_label, text="Scan specific ports", variable=port_choice, value=2).pack(side="left")

ports_entry = tk.Entry(ports_frame)
ports_entry.pack(side="left", fill="x",expand=True)

start_button = tk.Button(root, text="Start Scan", command=start_scan)
start_button.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True)

result_scrollbar = tk.Scrollbar(result_frame)
result_scrollbar.pack(side="right", fill="y")

result_list = tk.Listbox(result_frame, yscrollcommand=result_scrollbar.set)
result_list.pack(side="left", fill="both", expand=True)

result_scrollbar.config(command=result_list.yview)

root.mainloop()
