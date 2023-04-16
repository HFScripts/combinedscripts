from subdomain_discovery import run_subdomain_discovery
from port_scanner import scan_ports_for_domains
from services import run_services
from extractURLs import extract_urls
import asyncio

no_cloudflare = "none"
cloudflare = "none"
subdomains ="none"

securitytrails_api_key = "API_KEY"
shodan_api_key = "API_KEY"
virustotal_api_key = "API_KEY"
domain = "openai.com"

no_cloudflare, cloudflare = run_subdomain_discovery(domain, securitytrails_api_key, shodan_api_key, virustotal_api_key)
ports = [80, 443, 8080, 8888, 22]  # List of specific ports to scan
site_ports = scan_ports_for_domains(no_cloudflare, ports)
print(f"\n{site_ports}\n")
subdomains = no_cloudflare
run_services(site_ports, subdomains)

extracted_urls = asyncio.run(extract_urls(site_ports, subdomains))
print(f"\n{extracted_urls}")


