import subprocess

def run_services(site_ports, subdomains):
    unique_lines = set()

    # Loop through each domain and port combination
    for domain, ports in site_ports.items():
        for port in ports:
            url = f"http://{domain}:{port}"
            command = ['whatweb', url]
            result = subprocess.run(command, capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if domain in line and "The plain HTTP request was sent to HTTPS port" not in line and line not in unique_lines:
                    print(line)
                    unique_lines.add(line)

    # Loop through each subdomain
    for subdomain in subdomains:
        url = f"http://{subdomain}"
        command = ['whatweb', url]
        result = subprocess.run(command, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if subdomain in line and "The plain HTTP request was sent to HTTPS port" not in line and line not in unique_lines:
                print(line)
                unique_lines.add(line)
