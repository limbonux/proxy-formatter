# Developed by: limbonux
# Github: https://github.com/limbonux

import requests
from requests.exceptions import ProxyError, ConnectTimeout
import socks
import socket
import urllib3

# Disable warnings about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Test URL
test_url = "http://example.com"

# Function to read proxies from a text file
def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        proxy_list = [line.strip() for line in file if line.strip()]
    return proxy_list

# Function to write working proxies to a text file
def write_proxies_to_file(file_path, working_proxies):
    with open(file_path, 'w') as file:
        for proxy in working_proxies:
            file.write(proxy + "\n")

# Function to test HTTP/HTTPS proxies
def test_http_https(proxy, protocol):
    proxy_host, proxy_port, user, password = proxy.split(':')
    proxy_url = f"{protocol}://{user}:{password}@{proxy_host}:{proxy_port}"
    
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    try:
        # Use verify=False to disable SSL cert checking for HTTPS
        response = requests.get(test_url, proxies=proxies, timeout=5, verify=False)
        if response.status_code == 200:
            print(f"{protocol} proxy works: {proxy_url}")
            return proxy_url
    except (ProxyError, ConnectTimeout):
        return None

# Function to test SOCKS proxies
def test_socks(proxy, socks_version):
    proxy_host, proxy_port, user, password = proxy.split(':')
    
    # Set up SOCKS proxy
    socks.set_default_proxy(socks_version, proxy_host, int(proxy_port), True, user, password)
    socket.socket = socks.socksocket

    try:
        sock = socket.create_connection(("example.com", 80), timeout=5)
        if sock:
            sock.close()
            socks_protocol = "socks4" if socks_version == socks.SOCKS4 else "socks5"
            proxy_url = f"{socks_protocol}://{user}:{password}@{proxy_host}:{proxy_port}"
            print(f"{socks_protocol} proxy works: {proxy_url}")
            return proxy_url
    except (socket.error, ProxyError, ConnectTimeout):
        return None

# Main function to test all proxies
def test_proxies(proxy_list):
    working_proxies = []
    for proxy in proxy_list:
        # Test for HTTP and HTTPS
        http_proxy = test_http_https(proxy, "http")
        https_proxy = test_http_https(proxy, "https")

        if http_proxy:
            working_proxies.append(http_proxy)
        elif https_proxy:
            working_proxies.append(https_proxy)
        else:
            # If HTTP/HTTPS fail, test for SOCKS4 and SOCKS5
            socks4_proxy = test_socks(proxy, socks.SOCKS4)
            socks5_proxy = test_socks(proxy, socks.SOCKS5)
            
            if socks4_proxy:
                working_proxies.append(socks4_proxy)
            elif socks5_proxy:
                working_proxies.append(socks5_proxy)

    return working_proxies

# File paths
input_file = "proxy.txt"  # Input file containing the list of proxies
output_file = "working_proxies.txt"  # Output file to store working proxies

# Read proxies from input file
proxy_list = read_proxies_from_file(input_file)

# Test and gather working proxies
working_proxies = test_proxies(proxy_list)

# Write working proxies to output file
write_proxies_to_file(output_file, working_proxies)

print(f"Working proxies have been saved to {output_file}.")
