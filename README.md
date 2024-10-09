# 📡 Proxy Formatter

**Developed by:** limbonux  
**GitHub:** [limbonux](https://github.com/limbonux)

## ✨ Description

The Proxy Formatter is a Python script designed to test and validate the functionality of HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. It reads a list of proxies from a file, tests each one for connectivity, and saves the working proxies to a separate file. The script utilizes the `requests` library for HTTP/HTTPS requests and `socks` for SOCKS proxy connections.

### 🚀 Features
- ✅ Supports testing for HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
- 🔒 Automatically disables SSL certificate warnings for HTTPS requests.
- 📄 Outputs the list of functional proxies to a file.
- ⚙️ Easy-to-configure input and output file paths.

## 📋 Requirements
- **Python 3.x** is required.
- Required libraries: `requests`, `pysocks`, `urllib3`

You can install the required libraries using the following command:
```bash
pip install requests pysocks urllib3
```

## 🛠️ Usage

1. **Input File**:
   - Ensure that the `proxy.txt` file is located in the same directory as the script.
   - Add the list of proxies in the following format:
     ```plaintext
     proxy_host:proxy_port:username:password
     ```

2. **Run the Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script and run:
     ```bash
     python proxy.py
     ```

3. **View the Results**:
   - The script will test each proxy in the list and save the working proxies to a file named `working_proxies.txt` in the same directory.

## 📂 File Paths
- **Input file:** `proxy.txt` — Contains the list of proxies to be tested.
- **Output file:** `working_proxies.txt` — Contains the list of validated and working proxies.

## 📝 Notes
- The script uses a test URL (`http://example.com`) to check the validity of each proxy.
- Proxies that fail the connection test or timeout will not be included in the output file.

# Support My Work!

💵 If you're a fan of our project and want to support us, consider donating crypto. Your support will help us improve and expand, providing even more value to our users. Thank you for your generosity! 💵

TON:
`UQATbChkxTXjNepmCOKKH9Hv5t2cnkGfQOBF-w159gJVWJGQ`
```
