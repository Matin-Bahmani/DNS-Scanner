# DNS Scanner

A modern, blazing-fast, multi-threaded DNS speed testing and benchmarking tool written in Python. It features a beautiful terminal user interface (TUI) powered by the `rich` library and supports live server scraping with custom target domain testing.


## 🚀 Features

*   **Multi-threaded Engine**: Tests dozens of DNS servers concurrently in seconds.
*   **Custom Target Domain**: Test DNS resolution speed against any domain (defaults to `google.com`).
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
```
dns-scanner/
├── data/
│   ├── dns_servers.py      # Default DNS database
│   └── top_100_dns.txt     # Bulk DNS test targets
├── src/
│   └── main.py             # Core application entry
├── LICENSE
├── README.md
└── requirements.txt
```

## ❓ Usage
Clone this repository, navigate to the directory, and run the script:
```python src/main.py```

### How it works:
* Choose Mode: The script prompts you to choose between using the built-in global DNS list or loading a custom ```.txt``` file
* Select Domain: Enter a custom target domain (e.g., cloudflare.com) or press Enter for ```google.com```
* Dynamic Processing: Real-time progress bar with concurrent server testing
* Clean Presentation: Displays latency results in a clear tabular format (IPv4/IPv6)
* Smart Recommendations: Highlights the fastest IPv4 and IPv6 DNS servers on your network


## 🎮 Scan Modes Available
* Use Default Public DNS List (Offline): Benchmarks the built-in offline list ```data/dns_servers.py```
* Load Custom IP/DNS List from TXT File: Loads targets from custom text files ```data/top_100_dns.txt```
* Fetch & Scan Live DNS from the Internet (Auto): Fetches and benchmarks fresh public servers in real time
* Exit: Safely closes the utility


## 📂 Format for Custom Lists(.txt)
Create a text file with one IP address per line. Empty lines and comments ```#``` are ignored:
```
# My Custom DNS Targets
1.1.1.1
8.8.8.8
# IPv6 is also supported!
2606:4700:4700::1111
```


## 💡 Quick Start with Test File
To test bulk scanning immediately, enter the path to the included test file when prompted:
```data/top_100_dns.txt```


## ✨ Output Example (v2.0.1)
```
    ____  _   _  ____     _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/    / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \     \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /    ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/    /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|  
                                                                    
             Version 2.1.0 • Developed by M.Matin-Bahmani
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

Enter domain to test against(Press Enter for 'google.com'): youtube.com
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