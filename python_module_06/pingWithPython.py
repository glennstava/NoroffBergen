import subprocess

# Creates a process to ping python.org by sending 4
# Internet Control Message Protocol (ICMP) messages.

process = subprocess.Popen(['ping', '-c 4', 'noroff.no'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True)

# Continuously run the loop

while True:

    # Retrieve the output from the Popen object's stdout object
    # strip() removes a string's starting and ending whitespaces.
    print(process.stdout.readline().strip())
    
    # Test if the process has ended. While active it will return a result of None.
    if process.poll() is not None:

        # Read the last output from stdout and displays each line to the console window.
        for output in process.stdout.readlines():
            print(output.strip())
            
        # End the loop if the process has completed.
        break