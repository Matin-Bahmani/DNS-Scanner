import os
import sys
import time
import dns.resolver
import dns.exception
import ipaddress
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

# Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "accent": "bold yellow"
})
console = Console(theme=custom_theme)


# Core
def worker_test_server(server: dict, domain: str = "google.com", timeout: float = 2.0, attempts: int = 3) -> dict:

    server_ip = server["ip"]
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [server_ip]
    resolver.timeout = timeout
    resolver.lifetime = timeout

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

    # IPv4 or IPv6
    ip_type = "IPv6" if ":" in server_ip else "IPv4"

    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        return {
            "success": True,
            "name": server["name"],
            "ip": server_ip,
            "type": ip_type,
            "ping_str": f"{avg_latency:.1f} ms",
            "raw_latency": avg_latency
        }
    else:
        return {
            "success": False,
            "name": server["name"],
            "ip": server_ip,
            "type": ip_type,
            "ping_str": "Timeout",
            "raw_latency": float('inf')
        }


# Loding line
def run_parallel_scan(servers_list: list, max_threads: int = 20) -> list:

    results = []

    progress_bar = Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TaskProgressColumn(),
    )

    with progress_bar:
        scan_task = progress_bar.add_task(
            "[accent]Scanning servers in parallel...[/accent]",
            total=len(servers_list)
        )

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = {
                executor.submit(worker_test_server, server): server
                for server in servers_list
            }

            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception:
                    pass
                finally:
                    progress_bar.update(scan_task, advance=1)

    return results


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

    # Information
    console.print(r"""[bold green]
    ____  _   _  ____    _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/   / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \    \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|     

            Version 2.0.0 • Developed by Matin-Bahmani 
            Github • https://github.com/Matin-Bahmani         
                                                           
          [/bold green]""")

    # Loop
    while True:
       # Interactive Mode
        console.print("\n[bold cyan]Select Scan Mode:[/bold cyan]")
        console.print(
            "  [bold green]1.[/bold green] Use Default Public DNS List")
        console.print(
            "  [bold green]2.[/bold green] Load Custom IP/DNS List from TXT File")
        console.print("  [bold green]3.[/bold green] Exit")
        console.print("[dim]" + "=" * 45 + "[/dim]")

        choice = console.input(
            "[bold white]Enter choice (1, 2 or 3): [/bold white]").strip()

        # Conditions
        if choice == "3":
            console.print(
                "[accent]Thank you for using this program <3 Goodbye![/accent]")
            break

        if choice == "2":
            file_path = console.input(
                "[bold white]Enter the path to your TXT file (e.g., targets.txt): [/bold white]").strip()
            file_path = file_path.strip("'\"")
            custom_list = load_custom_ips(file_path)

            if custom_list:
                active_servers = custom_list
                console.print(
                    f"[success]Successfully loaded {len(active_servers)} custom targets.[/success]")
            else:
                console.print(
                    "[warning]Falling back to default DNS list...[/warning]")
                from dns_servers import PUBLIC_DNS_SERVERS
                active_servers = PUBLIC_DNS_SERVERS
        else:
            from dns_servers import PUBLIC_DNS_SERVERS
            active_servers = PUBLIC_DNS_SERVERS

        # Start scaning
        console.input(
            "\n[bold yellow]Press Enter to start the scan...[/bold yellow]\n")

        scan_results = run_parallel_scan(active_servers, max_threads=20)

        # List
        table = Table(
            title="[bold white]DNS Speed Test Results[/bold white]", show_lines=True)
        table.add_column("Server Name", style="cyan", no_wrap=True)
        table.add_column("IP Address", style="magenta")
        table.add_column("Type", justify="center")
        table.add_column("Result (Latency)", justify="right")

        Best_DNS = []

        # Test servers
        for res in scan_results:
            latency = res["raw_latency"]
            ping_str = res["ping_str"]

            if res["success"]:
                Best_DNS.append(res)
                if latency < 50:
                    colored_result = f"[bold green]{ping_str}[/bold green]"
                elif latency < 120:
                    colored_result = f"[bold yellow]{ping_str}[/bold yellow]"
                else:
                    colored_result = f"[orange3]{ping_str}[/orange3]"
            else:
                colored_result = f"[danger]{ping_str}[/danger]"

            table.add_row(res['name'], res['ip'], res['type'], colored_result)

        # Show table
        console.print(table)
        console.print("[success]Test is completed![/success]\n")

        # RECOMMENDATIONS PART
        if Best_DNS:
            ipv4_bests = [s for s in Best_DNS if ":" not in s["ip"]]
            ipv6_bests = [s for s in Best_DNS if ":" in s["ip"]]

            recommendation_text = ""

            if ipv4_bests:
                fastest_v4 = min(ipv4_bests, key=lambda x: x['raw_latency'])
                recommendation_text += f"🥇 [bold green]Best IPv4 DNS:[/bold green] {fastest_v4['name']} [{fastest_v4['ip']}] -> [bold green]{fastest_v4['ping_str']}[/bold green]\n"
            else:
                recommendation_text += "[danger]No working IPv4 DNS found.[/danger]\n"

            if ipv6_bests:
                fastest_v6 = min(ipv6_bests, key=lambda x: x['raw_latency'])
                recommendation_text += f"🚀 [bold green]Best IPv6 DNS:[/bold green] {fastest_v6['name']} [{fastest_v6['ip']}] -> [bold green]{fastest_v6['ping_str']}[/bold green]"
            else:
                recommendation_text += "[warning]No working IPv6 DNS found. (Check IPv6 settings)[/warning]"

            console.print(Panel(
                recommendation_text,
                title="[bold gold1]RECOMMENDATIONS[/bold gold1]",
                border_style="gold1",
                expand=False
            ))

        # Ask again
        answer = console.input(
            "\nWould you like to run another scan? (Y/N): ").strip()
        if answer.upper() == "Y":
            continue
        else:
            console.print(
                "[accent]Thank you for using this program <3 Goodbye![/accent]")
            break
