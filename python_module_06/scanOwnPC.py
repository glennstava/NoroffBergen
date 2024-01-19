import nmap3

ip_adr = "45.33.32.156"

nmap = nmap3.Nmap()
results = nmap.scan_top_ports(ip_adr)

print(f"scanning ports on {ip_adr}\n")

for host in results:
    if host == ip_adr:
        for port in results[ip_adr]['ports']:
            print(port['protocol'], end='\t')
            print(port['portid'], end='\t')
            print(port['state'])