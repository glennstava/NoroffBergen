import nmap3

"""
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.0.1")

print(results)
"""

ip_devices = "192.168.0.1/24"

nmap = nmap3.NmapScanTechniques()
results = nmap.nmap_ping_scan(ip_devices)

print("\n\nStarting subnet scan\n")
print(f'{"Host".ljust(15)}{"MAC".center(30)}{"State".rjust(15)}')
print("-"*60)

for host in results: 
    
    if host != "stats" and host != "runtime" and host != 'task_results':
        
        device_information = results[host]
        
        if device_information["macaddress"] != None:
            mac_address = device_information["macaddress"]["addr"]
        else:
            mac_address = "none"
            continue
            
        state = device_information["state"]["state"]

        print(f"{host.ljust(15)}{mac_address.center(30)}{state.rjust(15)}")
    
    else:
        if host == "stats":
            print("-"*60)
            print()
            print(f"The scan was completed with NMAP version {results[host]['version']}")
            print(f"and the command used was {results[host]['args']}")
            print("Completed the subnet scan")