import os
import socket
from socket import gethostbyname

def get_ip(url):

    command ="host " + url
   # command = "nslookup " + url
    process = os.popen(command)
    result = str(process.read())
    marker = result.find('has address') + 12
    return result[marker:].splitlines()[0]

def get_ip2(url):
     ip = gethostbyname(url)
     return ip
    #return socket.gethostbyname(socket.getfqdn(url))

# print(get_ip2('https://www.facebook.com'))