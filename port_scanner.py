import socket
from typing import List, Dict, Tuple

def get_unique_ips(domain_list: List[str]) -> List[str]:
    unique_ips = set()
    for domain in domain_list:
        try:
            ip = socket.gethostbyname(domain)
            unique_ips.add(ip)
        except socket.gaierror:
            print(f"Unable to resolve {domain}")
    return list(unique_ips)

def is_port_open(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            return result == 0
    except socket.error:
        print(f"Error connecting to {ip} on port {port}")
        return False

def scan_ports(ip: str, port_range: Tuple[int, int]) -> List[int]:
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        if is_port_open(ip, port):
            open_ports.append(port)
    return open_ports

def scan_ports_list(ip: str, ports: List[int]) -> List[int]:
    open_ports = []
    for port in ports:
        if is_port_open(ip, port):
            open_ports.append(port)
    return open_ports

def get_port_map(unique_ips: List[str], ports: List[int]) -> Dict[str, List[int]]:
    ip_ports = {}
    for ip in unique_ips:
        open_ports = scan_ports_list(ip, ports)
        if open_ports:
            ip_ports[ip] = open_ports
    return ip_ports

def scan_ports_for_domains(domain_list: List[str], ports: List[int]) -> Dict[str, List[int]]:
    unique_ips = get_unique_ips(domain_list)
    ip_ports = get_port_map(unique_ips, ports)

    domain_ports = {}
    for domain in domain_list:
        try:
            ip = socket.gethostbyname(domain)
            if ip in ip_ports:
                domain_ports[domain] = ip_ports[ip]
        except socket.gaierror:
            print(f"Unable to resolve {domain}")
    return domain_ports
