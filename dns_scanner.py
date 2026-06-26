import time
from typing import Optional

import dns.resolver
import dns.exception


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

    latencies = []

    for _ in range(attempts):
        try:
            start = time.perf_counter()
            resolver.resolve(domain, "A")
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


if __name__ == "__main__":

    print(r"""
    ____  _   _  ____    _____ ______ __    _   _ _   _  _____ ___ 
   / __ \/ | / / ___/   / ___// ____/   |  / | / / | / / ____/ __ \
  / / / /  |/ /\__ \    \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
 / /_/ / /|  /___/ /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
/_____/_/ |_//____/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|                                                                  
          """)

    print("Version 1.0.0")
    print("https://github.com/Matin-Bahmani")
    print("="*60)
    while True:
        input("Press Enter to start the scan...")
        from dns_servers import PUBLIC_DNS_SERVERS

        print("Testing a few sample servers...\n")
        print(f"{'Server Name':<25}{'IP':<18}{'Result'}")
        print("-" * 60)

        for server in PUBLIC_DNS_SERVERS[:38]:
            latency = measure_dns_latency(server["ip"])
            if latency is not None:
                result = f"{latency:.1f} ms"
            else:
                result = "No response"
            print(f"{server['name']:<25}{server['ip']:<18}{result}")

        print("-"*60)

        answer = input("Would you like to run another scan? (Y/N):")
        if answer.upper() == "Y":
            continue

        elif answer.upper() == "N":
            print("Thank you for using my program!"
                  "Goodbye!")
            break
        else:
            print("Please enter Y or N")
