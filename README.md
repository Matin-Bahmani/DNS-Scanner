# DNS Scanner & Latency Checker

A lightweight, efficient Python tool designed to benchmark and measure the precise query latency of various public DNS servers. Instead of using generic ICMP pings, this tool calculates the exact time it takes for a DNS nameserver to resolve a domain query (DNS Query Latency), giving you a realistic overview of their performance.

---

## 🚀 Features

* **Dual-Protocol Support (IPv4 & IPv6):** Seamlessly scans and benchmarks both IPv4 and IPv6 DNS addresses simultaneously.
* **Bulk & Custom List Scanning:** Load your own custom list of IP addresses from a `.txt` file for automated batch testing.
* **Auto-Protocol Detection:** Automatically identifies whether a server is IPv4 or IPv6 and queries the correct corresponding record type (`A` for IPv4, `AAAA` for IPv6).
* **Live Dynamic UI:** Features a smooth, inline terminal loading animation to show real-time scanning progress without cluttering the final output table.
* **Real DNS Query Benchmarking:** Measures actual resolution speed using low-level DNS operations rather than just standard ICMP ping response times.
* **Smart Exception Handling:** Gracefully handles timeouts, `NXDOMAIN`, `NoAnswer`, invalid IPs, and unreachable nameservers without crashing.
* **Interactive Mode:** Allows running multiple consecutive scans or switching between lists without restarting the script.
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
* dns_scanner.py (Core)
* dns_servers.py (Database)

---

## ❓ Usage
To launch the scanner, simply execute the main script from your terminal:
```python main.py```

### How it works:
* Choose Mode: The script prompts you to choose between using the built-in global DNS list or loading a custom ```.txt``` file
* Dynamic Processing: A live inline loader spins while actively querying targets (resolving google.com)
* Clean Presentation: Outputs results dynamically in a clean tabular format showing Server Name, IP Address, Type (IPv4/IPv6), and Latency (ms)
* Smart Recommendations: Highlights the fastest DNS servers under 40ms on your network at the end of the scan

---

## 📂 Format for Custom Lists(.txt)
If you choose to load a custom list, create a simple text file with one IP address per line. Comments starting with ```#``` and blank lines are automatically ignored:
```
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
```

---

## 💡 Quick Start with Test File
To test the bulk scanning feature instantly, a pre-configured file containing 100 public and alternative DNS servers is provided in the repository.
When prompted by the script, simply enter:
```top_100_dns.txt```

---

## ✨ Output Example (v1.1.0)
```
    ____  _   _  ____     _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/    / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \     \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /    ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/    /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|  
                                                                    
Version 1.2.0
[https://github.com/Matin-Bahmani](https://github.com/Matin-Bahmani)
============================================================
Select Scan Mode:
1. Use Default Public DNS List
2. Load Custom IP/DNS List from TXT File
3. Exit
============================================================
Enter choice (1, 2 or 3): 1

Press Enter to start the scan...

Server Name              IP                            Type      Result
----------------------------------------------------------------------------
Cloudflare               1.1.1.1                       IPv4      8.5 ms
Cloudflare               2606:4700:4700::1111          IPv6      12.1 ms
Google                   8.8.8.8                       IPv4      14.2 ms
Custom_Target_1          10.0.0.99                     IPv4      No response
----------------------------------------------------------------------------
Test is completed
Recommended DNS: Cloudflare 1.1.1.1 -> 8.5 ms

Would you like to run another scan? (Y/N):
```

---

## 🔮 Changelog (v1.1.0)
* Added Bulk Scan feature supporting custom target text files ```.txt```
* Embedded ```ipaddress``` smart validation to dynamically parse and verify user-inputted IP lists
* Implemented an inline terminal loading animation (```\r``` dynamic buffer) for smoother UX
* Added a robust main menu for mode selection and graceful exits

---

## Author
* **Matin Bahmani** - [GitHub Profile](https://github.com/Matin-Bahmani)
* Feel free to fork this repository, open issues, or submit pull requests to improve the tool!