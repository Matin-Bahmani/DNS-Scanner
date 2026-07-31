# DNS Scanner & Latency Checker

A modern, blazing-fast, multi-threaded DNS speed testing and benchmarking tool written in Python. It features a beautiful terminal user interface (TUI) powered by the `rich` library and supports live server scraping.


## 🚀 Features

*   **Multi-threaded Engine**: Tests dozens of DNS servers concurrently in seconds.
*   **Live Web Scraper**: Fetches fresh, verified DNS lists automatically from the web.
*   **Custom IP Lists**: Easily loads and validates targets from any `.txt` file.
*   **Modern Rich UI**: Interactive progress bar, color-coded tables, and best DNS panels.
*   **Dual Protocol Support**: Auto-detects IPv4/IPv6 and recommends the fastest servers.
*   **Robust Error Handling**: Prevents crashes during missing files or network issues.

## 📦 Requirements & Installation

### 1. Requirements
Make sure you have Python 3.6 or higher installed on your system.

### 2. Install Dependencies
This version introduces visual and networking upgrades. Install the required libraries using `pip`:
```pip install dnspython```


## 🧬 Project Structure
Ensure your local repository has the following files in the same directory:
* dns_scanner.py (Core)
* dns_servers.py (Database)


## ❓ Usage
Clone this repository, navigate to the directory, and run the script:
```python dns_scanner.py```

### How it works:
* Choose Mode: The script prompts you to choose between using the built-in global DNS list or loading a custom ```.txt``` file
* Dynamic Processing: A live inline loader spins while actively querying targets (resolving google.com)
* Clean Presentation: Outputs results dynamically in a clean tabular format showing Server Name, IP Address, Type (IPv4/IPv6), and Latency (ms)
* Smart Recommendations: Highlights the fastest DNS servers under 40ms on your network at the end of the scan


## 🎮 Scan Modes Available
Upon launching, the interactive CLI menu will present you with 4 options:
* Use Default Public DNS List (Offline): Quickly benchmarks the built-in, offline list of major public servers (from your dns_servers.py file)
* Load Custom IP/DNS List from TXT File: Point the tool to any text file containing IP addresses (one IP per line). It automatically skips empty lines and comments (#)
* Fetch & Scan Live DNS from the Internet (Auto): Scrapes the top 50 active nameservers directly from the web and tests them in real-time
* Exit: Safely closes the utility


## 📂 Format for Custom Lists(.txt)
If you choose to load a custom list, create a simple text file with one IP address per line. Comments starting with ```#``` and blank lines are automatically ignored:
```
# My Custom DNS Targets
1.1.1.1
8.8.8.8
# IPv6 is also supported!
2606:4700:4700::1111
```


## 💡 Quick Start with Test File
To test the bulk scanning feature instantly, a pre-configured file containing 100 public and alternative DNS servers is provided in the repository.
When prompted by the script, simply enter:
```top_100_dns.txt```


## ✨ Output Example (v2.0.1)
```
    ____  _   _  ____     _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/    / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \     \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /    ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/    /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|  
                                                                    
             Version 2.0.1 • Developed by Matin-Bahmani
             Github • https://github.com/Matin-Bahmani

Select Scan Mode:
  1. Use Default Public DNS List (Offline)
  2. Load Custom IP/DNS List from TXT File
  3. Fetch & Scan Live DNS from the Internet (Auto)
  4. Exit
=============================================
Enter choice (1, 2, 3 or 4): 3

⠋ Fetching fresh DNS servers from public-dns.info...
[✓] Successfully retrieved 50 fresh DNS servers from the web!

Press Enter to start the scan...

Scanning servers in parallel... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%

                         DNS Speed Test Results                          
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Server Name     ┃ IP Address          ┃  Type  ┃     Result (Latency) ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ Online_Server_1 │ 1.1.1.1             │  IPv4  │              38.2 ms │
├─────────────────┼─────────────────────┼────────┼──────────────────────┤
│ Online_Server_2 │ 8.8.8.8             │  IPv4  │              72.5 ms │
├─────────────────┼─────────────────────┼────────┼──────────────────────┤
│ Online_Server_3 │ 10.0.0.99           │  IPv4  │              Timeout │
└─────────────────┴─────────────────────┴────────┴──────────────────────┘
[✓] Test is completed!

┌── RECOMMENDATIONS ─────────────────────────────────────────────────────┐
│ 🥇 Best IPv4 DNS: Online_Server_1 [1.1.1.1] -> 38.2 ms                 |
└────────────────────────────────────────────────────────────────────────┘

Would you like to run another scan? (Y/N):
```


## Author
* **Matin Bahmani** - [GitHub Profile](https://github.com/Matin-Bahmani)
* Feel free to fork this repository, open issues, or submit pull requests to improve the tool!