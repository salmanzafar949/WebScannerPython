import os


def get_ip(url):

    command ="host " + url
   # command = "nslookup " + url
    process = os.popen(command)
    result = str(process.read())
    marker = result.find('has address') + 12
    return result[marker:].splitlines()[0]

print(get_ip('facebook.com'))