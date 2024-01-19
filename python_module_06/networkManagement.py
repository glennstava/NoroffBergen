import argparse
import nmap3

def scanningHost(hostAdr):
    
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(hostAdr)
#    print(results)

#    print(f"scanning ports on {hostAdr}\n")

    for host in results:
#        print(host)
    
        if host == hostAdr:
            for port in results[hostAdr]['ports']:
                print(port['protocol'], end='\t')
                print(port['portid'], end='\t')
                print(port['state'])
    
    print("\n---\nEbd of scan")

scanningHost("10.53.2.72")
"""
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--IPaddress", metavar = "IPaddress", required = True, help = "IP-adress")
    args = parser.parse_args()

    scanningHost(args.IPaddress)
"""
