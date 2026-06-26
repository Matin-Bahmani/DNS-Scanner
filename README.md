# DNS Scanner & Latency Checker

A lightweight, efficient Python tool designed to benchmark and measure the precise query latency of various public DNS servers. Instead of using generic ICMP pings, this tool calculates the exact time it takes for a DNS nameserver to resolve a domain query (DNS Query Latency), giving you a realistic overview of their performance.

---

## 🚀 Features

* **Real DNS Query Benchmarking:** Measures actual resolution speed using standard `A` record queries rather than just ICMP ping response times.
* **Smart Exception Handling:** Gracefully handles timeouts, `NXDOMAIN`, `NoAnswer`, and unreachable nameservers without crashing.
* **Averaged Latency Output:** Sends multiple attempts (default: 3) per server to calculate an accurate average response time in milliseconds ($ms$).
* **Clean CLI Interface:** Features a well-formatted ASCII art banner and structured tabular data output for easy reading.
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
* main.py
* dns_servers.py

---

## ❓ Usage
To launch the scanner, simply execute the main script from your terminal:
```python main.py```

#How it works:
*The script initializes and waits for you to press Enter.
*It fetches DNS servers defined in dns_servers.py.
*It performs active queries (resolving google.com) against each server.
*Outputs the results dynamically in a tabular format showing Server Name, IP Address, and Latency (ms) or "No response".
*Prompts you to either rerun the scan or exit.

---

## ✨ Output Example
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

Server Name              IP                Result
------------------------------------------------------------
Google Public DNS        8.8.8.8           14.2 ms
Cloudflare               1.1.1.1           8.5 ms
Unknown Server           10.0.0.99         No response
------------------------------------------------------------
Would you like to run another scan? (Y/N):
```

## Author
* **Matin Bahmani** - [GitHub Profile](https://github.com/Matin-Bahmani)
Feel free to fork this repository, open issues, or submit pull requests to improve the tool!