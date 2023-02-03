import socket
import datetime

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

choice = input("Do you want to scan a website (w) or an IP address (i)? ")

if choice == 'w':
    hostname = input("Enter a website hostname: ")
    host = get_ip_address(hostname)
    if host is None:
        print("Unable to resolve hostname.")
    else:
        port_choice = input("Do you want to scan all possible ports (a) or specific ones (s)? ")
        if port_choice == 'a':
            print("Scanning host", host, "...")
            for port in range(1, 65535):
                result = is_open(host, port)
                if result == "open":
                    print("Port", port, "is", result)
                else:
                    print("Port", port, "is", result)
            print("Scan completed on", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif port_choice == 's':
            ports = input("Enter a list of ports separated by comma: ")
            if ports.strip() == '':
                print("No ports entered.")
            else:
                ports = [int(port) for port in ports.split(',')]
                print("Scanning host", host, "...")
                for port in ports:
                    result = is_open(host, port)
                    if result == "open":
                        print("Port", port, "is", result)
                    else:
                        print("Port", port, "is", result)
                print("Scan completed on", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print("Invalid choice.")

elif choice == 'i':
    host = input("Enter an IP address: ")
    port_choice = input("Do you want to scan all possible ports (a) or specific ones (s)? ")
    if port_choice == 'a':
        print("Scanning host", host, "...")
        for port in range(1, 65535):
            result = is_open(host, port)
            if result == "open":
                print("Port", port, "is", result)
            else:
                print("Port", port, "is", result)
    elif port_choice == 's':
        ports = input("Enter a list of ports separated by comma: ")
        if ports.strip() == '':
            print("No ports entered.")
        else:
            ports = [int(port) for port in ports.split(',')]
            print("Scanning host", host, "...")
            for port in ports:
                result = is_open(host, port)
                if result == "open":
                    print("Port", port, "is", result)
                else:
                    print("Port", port, "is", result)
    else:
        print("Invalid choice.")

else:
    print("Invalid choice.")
