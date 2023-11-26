import socket
import uuid
import os
import re

HNAME=1
IP=2
MAC=3
ARP=4
ROUT=5
QUIT=6



def get_user_choice():
    print("Network Toolkit Menu")
    print("_____________________________________")
    print("1. Display the Host Name")
    print("2. Display the IP Address")
    print("3. Display the MAC Address")
    print("4. Display the ARP Table")
    print("5. Display the Routing Table")
    print("6. Quit")
    print()
    
    choice = int(input("Enter your choice: "))
    
    return choice

def choicefun(choice):
   
    while choice > QUIT or choice < HNAME:
        
        choice = int(input("Please enter a valid number: "))
        print()
        
    return choice

def get_hostname(host):
    host=socket.gethostname()
    print("\n The host name is: ", host)
    #return host

def get_ipaddr(ipv4):
    ipv4=socket.gethostbyname()
    print("\n The IPv4 address of the system is: ", ipv4)
    #return ipv4

def get_mac(ele):
    print ("The MAC address is : ", end="") 
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
    for ele in range(0,8*6,8)][::-1]))

def get_arp(line):
    print("ARP Table")
    with os.popen('arp -a') as f:
        data=f.read()
    for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
        print(line)
    return line

def __pyroute2_get_host_by_ip(ip):
    print("Routing table\n: ")
    table=os.popen('route table')
    print(table)

def main():
    counter=False
    while counter==False:
        choice = get_user_choice()
        choicefun(choice)         
        if str(choice) == "6":            
            counter==True
        elif str(choice) == "1":
            get_hostname()
        elif str(choice) == "2":
            get_ipaddr()
        elif str(choice) == "3":
           get_mac() 
        elif str(choice)== "4":
            get_arp()
        elif str(choice) == "5":
            __pyroute2_get_host_by_ip()

main()
