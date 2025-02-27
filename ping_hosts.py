import subprocess

alive=[]

def get_ip_addresses():
    prefix = '192.168.9.' # Change this file to current network
    ip_addresses = []
    for i in range(4, 300): #avoid the first four devices, they are networking devices.
        ip_address = prefix + str(i)
        ip_addresses.append(ip_address)
    return ip_addresses

def get_alive_status(host):
    ALIVE = False
    command = 'ping ' + host + ' -n 1 -w 500' # pings the dang thing

    p = subprocess.Popen(command, stdout=subprocess.PIPE) # uses subprocess to process the ping
    output = p.stdout.read().decode() # OUTPUT!
    if 'TTL=' in output: # TTL tells you it is a device and it is alive (and what device)
        ALIVE = True
        print('ALIVE')
    return ALIVE

def main():
    ip_addresses = get_ip_addresses()
    for addr in ip_addresses:
        is_alive = get_alive_status(addr)
        if is_alive:
            print(addr + ' is ALIVE')
            alive.append(addr)
            

if __name__ == '__main__':
    main()
    
 
