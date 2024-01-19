import ping3
import platform

print(ping3.ping('noroff.no'))

def ping(host):
    # Create a ping object
    ping_obj = ping3.ping()

    # Ping the host
    response = ping_obj.ping(host)

    if response is not None:
        print(f"Ping to {host} successful. Round-trip time: {response} ms")

    else:
        print(f"Ping to {host} failed. Host may be unreachable.")

target_host = 'www.noroff.no'
ping(target_host)

"""
if __name__ == "__main__":
    target_host = 'www.noroff.no'

    if platform.system().lower() == "windows":
        target_host = "-n 4 " + target_host  # Perform 4 ping requests on Windows
    else:
        target_host = "-c 4 " + target_host  # Perform 4 ping requests on Unix-like systems

    ping(target_host)
"""