import os
import sys
import time
import dns.resolver
import dns.exception
import ipaddress
from typing import Optional


# Core
def measure_dns_latency(
    server_ip: str,
    domain: str = "google.com",
    timeout: float = 2.0,
    attempts: int = 3,
) -> Optional[float]:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [server_ip]
    resolver.timeout = timeout
    resolver.lifetime = timeout

    # Speed test
    latencies = []

    record_type = "AAAA" if ":" in server_ip else "A"

    for _ in range(attempts):
        try:
            start = time.perf_counter()
            resolver.resolve(domain, record_type)
            elapsed_ms = (time.perf_counter() - start) * 1000
            latencies.append(elapsed_ms)
        except (
            dns.exception.Timeout,
            dns.resolver.NoNameservers,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoAnswer,
        ):
            continue

    if not latencies:
        return None

    return sum(latencies) / len(latencies)


# Loding line
def show_loading(message="Scanning"):

    animation = ["[■□□□□]", "[■■□□□]", "[■■■□□]", "[■■■■□]", "[■■■■■]"]
    for frame in animation:
        sys.stdout.write(f"\r⏳ {message} {frame}")
        sys.stdout.flush()
        time.sleep(0.08)

    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


# Config file
def load_custom_ips(file_path):

    if not os.path.exists(file_path):
        print(f"\nError: File '{file_path}' not found!")
        return None

    custom_servers = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for index, line in enumerate(file, 1):
                ip = line.strip()
                if not ip or ip.startswith("#"):
                    continue

                try:
                    ip_obj = ipaddress.ip_address(ip)
                    ip_version = f"IPv{ip_obj.version}"

                    custom_servers.append({
                        "name": f"Custom_Target_{index}",
                        "ip": ip,
                        "type": ip_version
                    })
                except ValueError:
                    print(f"Skipping invalid IP on line {index}: {ip}")

        return custom_servers
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# Start
if __name__ == "__main__":

    print(r"""
    ____  _   _  ____    _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/   / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \    \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|                                                                  
          """)

    # Information
    print("Version 1.2.0")
    print("https://github.com/Matin-Bahmani")

    # Loop
    while True:
        # Interactive
        print("=" * 60)
        print("Select Scan Mode:")
        print("1. Use Default Public DNS List")
        print("2. Load Custom IP/DNS List from TXT File")
        print("3. Exit")
        print("=" * 60)

        choice = input("Enter choice (1, 2 or 3): ").strip()

        if choice == "3":
            print("Thank you for using this program <3",
                  "Goodbye!")
            break
        if choice == "2":
            file_path = input(
                "Enter the path to your TXT file (e.g., targets.txt): ").strip()
            file_path = file_path.strip("'\"")
            custom_list = load_custom_ips(file_path)
            if custom_list:
                active_servers = custom_list
                print(
                    f"Successfully loaded {len(active_servers)} custom targets.")
            else:
                print("Falling back to default DNS list...")
                from dns_servers import PUBLIC_DNS_SERVERS
                active_servers = PUBLIC_DNS_SERVERS
        else:
            from dns_servers import PUBLIC_DNS_SERVERS
            active_servers = PUBLIC_DNS_SERVERS

        input("\nPress Enter to start the scan...")

        # List
        print("Testing a few sample servers...\n")

        print(f"{'Server Name':<35}{'IP':<40}{'Type':<10}{'Result'}")
        print("-" * 100)

        Best_DNS = []

        # Test servers
        for server in active_servers:
            show_loading(f"Testing {server['name']} ({server['ip']})")
            latency = measure_dns_latency(server["ip"])

            ip_type = "IPv6" if ":" in server["ip"] else "IPv4"

            if latency is not None:
                result = f"{latency:.1f} ms"

                if latency < 40:
                    Best_DNS.append({
                        "name": server["name"],
                        "ip": server["ip"],
                        "ping": result
                    })

                print(
                    f"{server['name']:<35}{server['ip']:<40}{ip_type:<10}{result}")

            else:
                result = "No response"
                print(
                    f"{server['name']:<35}{server['ip']:<40}{ip_type:<10}{result}")

        print("-" * 100 + "\n")
        print("Test is completed")

        # RECOMMENDATIONS PART
        if Best_DNS:

            ipv4_bests = [s for s in Best_DNS if ":" not in s["ip"]]
            ipv6_bests = [s for s in Best_DNS if ":" in s["ip"]]

            print("=" * 40 + " RECOMMENDATIONS " + "=" * 40)

            if ipv4_bests:
                fastest_v4 = min(
                    ipv4_bests, key=lambda x: float(x['ping'].split()[0]))
                print(
                    f"\033[1m🥇 Best IPv4 DNS: {fastest_v4['name']} [{fastest_v4['ip']}] -> {fastest_v4['ping']}\033[0m")
            else:
                print("No IPv4 DNS under 40ms found.")

            if ipv6_bests:
                fastest_v6 = min(
                    ipv6_bests, key=lambda x: float(x['ping'].split()[0]))
                print(
                    f"\033[1m🚀 Best IPv6 DNS: {fastest_v6['name']} [{fastest_v6['ip']}] -> {fastest_v6['ping']}\033[0m")
            else:
                print(
                    "No IPv6 DNS under 40ms found. (Check if IPv6 is enabled on your network)")

            print("=" * 97 + "\n")

        # Again or not?
        answer = input("Would you like to run another scan? (Y/N):")
        if answer.upper() == "Y":
            continue

        elif answer.upper() == "N":
            print("Thank you for using this program <3",
                  "Goodbye!")
            break
        else:
            print("Please enter Y or N")
