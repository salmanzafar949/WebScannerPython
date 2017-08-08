from general import *
from domain_name import *
from  ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import time
ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    print("Scanning Started...........")
    time.sleep(1)
    print("Scanning.........")
    ip_addr = get_ip2(domain_name)
    #print(ip_addr)
    nmap = get_nmap('-F', ip_addr)
    robots_txt = get_robots_txt(url)
    whois = get_whois(url)
    create_report(name, url, domain_name, ip_addr, nmap, robots_txt, whois)
    print("Scanning Completed")

def create_report(name, fullurl, domain_name, ip_addr, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/fullurl.txt', domain_name)
    write_file(project_dir + '/ip_addr.txt', ip_addr)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)

gather_info('Google', 'https://www.google.com.pk/')