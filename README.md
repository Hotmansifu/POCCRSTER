## PortScanner
A simple python script for scanning open ports on a target host.

# Requirements
Python 3.x
pip (for installing the required packages)
### Usage
Clone the repository using ```git clone https://github.com/Hotmansifu/PortScanner.git```
*Navigate into the repository using cd PortScanner
*Install the required packages using 
```pip install socket```
```pip install datetime```
*Run the script using python port_scanner.py -H [target_host] -p [port_range]
### Options
-H or --host: The target host that you want to scan.
-p or --port: The range of ports that you want to scan. By default, it scans the common ports (1-1024).
### Example
```python port_scanner.py -H google.com -p 22,80,443```
### Output
The script will output the list of open ports on the target host.

### Suggestions
We welcome all suggestions and improvements. If you have any ideas or thoughts on how to make this script better, please feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License.



