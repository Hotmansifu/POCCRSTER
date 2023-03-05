import argparse
import socket
import threading


def connection_scan(target_ip, target_port):
    """Attempts to create a socket connection with the given IP address and port.
    If successful, the port is open. If not, the port is closed. In addition, a byte literal is sent to the target; the
    result is captured and printed as a system banner.
    """
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((target_ip, target_port))
        conn_socket.send(b'Banner_query\r\n')
        results = conn_socket.recv(100)
        print("[+] {}/tcp open".format(target_port))
        print("[+] {}".format(str(results)))  # Print banner grab results
    except OSError:
        print("[-] {}/tcp closed".format(target_port))
    finally:
        conn_socket.close()  # Ensure the connection is closed


def port_scan(target, port_num):
    """Scan indicated ports for status.
    First, it attempts to resolve the IP address of a provided hostname, then enumerates through the ports. Threads are
    used to call the connection_scan() function.
    """
    try:
        target_ip = socket.gethostbyname(target)
    except OSError:
        print("[^] Cannot resolve {}: Unknown host".format(target))
        return  # Exit scan if target IP is not resolved

    try:
        target_name = socket.gethostbyaddr(target_ip)
        print('[*] Scan Results for: {}'.format(target_name[0]))
    except OSError:
        print('[*] Scan Results for: {}'.format(target_ip))

    t = threading.Thread(target=connection_scan, args=(target_ip, int(port_num)))
    t.start()


def argument_parser():
    """Allow user to specify target host and port."""
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports to "
                                                 "scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", required=True, help="Host IP address")
    parser.add_argument("-p", "--ports", required=True, help="Comma-separated port list, such as '25,80,8080'")
    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary
    return var_args


if __name__ == '__main__':
    user_args = argument_parser()
    host = user_args["host"]
    port_list = user_args["ports"].split(",")  # Make a list from port numbers
    for port in port_list:
        port_scan(host, port)
