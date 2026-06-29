# DNS Scanner & Latency Checker

A lightweight, efficient Python tool designed to benchmark and measure the precise query latency of various public DNS servers. Instead of using generic ICMP pings, this tool calculates the exact time it takes for a DNS nameserver to resolve a domain query (DNS Query Latency), giving you a realistic overview of their performance.

---

## 🚀 Features

* **Dual-Protocol Support (IPv4 & IPv6):** Seamlessly scans and benchmarks both IPv4 and IPv6 DNS addresses simultaneously.
* **Auto-Protocol Detection:** Automatically detects whether a server is IPv4 or IPv6 and queries the correct corresponding record type (`A` for IPv4, `AAAA` for IPv6).
* **Real DNS Query Benchmarking:** Measures actual resolution speed using low-level DNS operations rather than just standard ICMP ping response times.
* **Smart Exception Handling:** Gracefully handles timeouts, `NXDOMAIN`, `NoAnswer`, and unreachable nameservers without crashing.
* **Averaged Latency Output:** Sends multiple attempts (default: 3) per server to calculate an accurate average response time in milliseconds (ms).
* **Upgraded CLI Interface:** Features a well-formatted ASCII art banner, structured tabular data output with clear type classification, and a smart recommendation engine.
* **Interactive Mode:** Allows running multiple consecutive scans without restarting the script.

---

## 🛠️ Requirements & Installation

### 1. Prerequisites
Make sure you have Python 3.7+ installed on your system.

### 2. Install Dependencies
This project relies on the `dnspython` library for low-level DNS operations. Install it via pip:
```pip install dnspython```

---

## 🧬 Project Structure
Ensure your local repository has the following files in the same directory:
* main.py (Core Execution script)
* dns_servers.py (Database list of public DNS addresses)

---

## ❓ Usage
To launch the scanner, simply execute the main script from your terminal:
```python main.py```

### How it works:
* The script initializes and waits for you to press Enter.
* It fetches all modern IPv4 and IPv6 DNS servers defined in dns_servers.py.
* It performs active queries (resolving google.com) using the appropriate record type.
* Outputs the results dynamically in a clean tabular format showing Server Name, IP Address, Type (IPv4/IPv6), and Latency (ms).
* At the end, if any server responds under 40ms, it highlights the Recommended Best DNS for your network.
* Prompts you to either rerun the scan or exit.

---

## ✨ Output Example (v1.1.0)
```
    ____  _   _  ____     _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/    / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \     \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /    ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/    /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|  
                                                                    
Version 1.0.0
(https://github.com/Matin-Bahmani)
============================================================
Press Enter to start the scan...
Testing a few sample servers...

Server Name              IP                            Type      Result
---------------------------------------------------------------------------
Cloudflare               1.1.1.1                       IPv4      8.5 ms
Cloudflare IPv6          2606:4700:4700::1111          IPv6      12.1 ms
Google                   8.8.8.8                       IPv4      14.2 ms
Unknown Server           10.0.0.99                     IPv4      No response
---------------------------------------------------------------------------

Test is completed
Recommended DNS: Cloudflare 1.1.1.1 -> 8.5 ms

Would you like to run another scan? (Y/N):
```

---

## 🚀 Changelog (v1.1.0)
* Added full IPv6 scanning support via dynamic AAAA record resolution.
* Expanded the DNS database in dns_servers.py to include verified global IPv6 addresses.
* Refactored the UI table layout to display a dedicated Type column.
* Optimized spacing to accommodate long IPv6 string addresses cleanly.

---

## Author
* **Matin Bahmani** - [GitHub Profile](https://github.com/Matin-Bahmani)
* Feel free to fork this repository, open issues, or submit pull requests to improve the tool!