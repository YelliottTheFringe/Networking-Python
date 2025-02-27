import subprocess

alive=[]

def get_ip_addresses():
    prefix = '192.168.9.'
    ip_addresses = []
    for i in range(10, 300):
        ip_address = prefix + str(i)
        ip_addresses.append(ip_address)
    return ip_addresses

def get_alive_status(host):
    ALIVE = False
    command = 'ping ' + host + ' -n 1 -w 500'

    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = p.stdout.read().decode()
    if 'TTL=' in output:
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
    
 