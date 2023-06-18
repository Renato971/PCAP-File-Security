import socket
import re
from datetime import datetime
from Port_Scanner import *
f = open('CyberSecurity2022.pcap', 'rb')
print(f.read())
f.close()
f = open('CyberSecurity2022.pcap', 'rb')
out = open('out.txt', 'a+')
magic = bytes(f.read(4)).hex()

print("  __  __   _____   _____    _____ ")
print(" |  \/  | |  __ \  |  __ \  |  __ \ ")
print(" | \  / | | |  | | | |__) | | |__) | ")
print(" | |\/| | | |  | | |  _  /  |  _  / ")
print(" | |  | | | |__| | | | \ \  | | \ \ ")
print(" |_|  |_| |______| |__\ \_\ |__\ \_\  ")
print("\n")
#task 2*******************************************************************
def convert_date(value):
    value = value.split()
    converted = value[0][6:8] + value[0][4:6] + value[0][2:4] + value[0][0:2]
    date = datetime.fromtimestamp(int(converted, 16))
    return date


def convert_size(value):
    value = value.split()
    converted = value[0][6:8] + value[0][2:4] + value[0][0:2]
    return converted
# ************************************************************************
# task 1 *****************************************************************
if magic == 'd4c3b2a1':

    majornumber = f.read(2)
    major = bytearray(majornumber)
    major.reverse()

    minornumber = f.read(2)
    minor = bytearray(minornumber)
    minor.reverse()

    times = f.read(4)
    time = bytearray(times)
    time.reverse()

    accutal = f.read(4)
    acc = bytearray(accutal)
    acc.reverse()

    snap = f.read(4)
    snaplen = bytearray(snap)
    snaplen.reverse()

    networks = f.read(4)
    network = bytearray(networks)
    network.reverse()
    seconds = int.from_bytes(f.read(4), byteorder="little")
    micro = int.from_bytes(f.read(4), byteorder="little")
else:
    major = f.read(2)
print('The Magic Number. is: ' + magic)
print('Major Version: ' + bytes(major).hex())
print('Minor Version: ' + bytes(minor).hex())
print('Timezone: ' + bytes(time).hex())
print('Accuracy of Timestamps: ' + (acc).hex())
print('Snap Length: ' + bytes(snaplen).hex())
print('Network: ' + (network).hex())


with open('CyberSecurity2022.pcap', 'rb') as f:
    content = f.read().hex()
    global_header = content[:48]
    print("Global Header :", len(global_header) / 2)
    packet_header = content[48:80]
# Task 1 end ********************************************
    fields = {
        "Reserved One": global_header[16:24],
        "Reserved Two": global_header[24:32],
        "HW Length": global_header[32:40],
        "Link Type": global_header[40:48]
    }
    fields_packets = {
        "Timestamp in Seconds": packet_header[:8],
        "Timestamp in Nanoseconds": packet_header[8:16],
        'Date': convert_date(packet_header[:8]),
        "Captured Packet Length": convert_size(packet_header[16:24]),
        "Original Packet Length": packet_header[24:32],
        'Timestamp': packet_header[:8],
        #'MacAddress': packet_header
    }

    print("-" * 500)
    print('Global Header: \n')
    for key, value in fields.items():
        print(f"{key}: {value}")
    print("-" * 500)
    print('Packet Header: \n')
    for key, value in fields_packets.items():
        print(f"{key}: {value}")
    print("-" * 500)
    print('Packet Data: \n')
    packet_data = content[80: ((int(fields_packets['Captured Packet Length'], 16) * 2) + 80)]
    print(f"Raw Hexadecimal: \n {packet_data} Bytes\n: {bytearray.fromhex(packet_data)}")
f.close()
print('\n')
print("-" * 500)
#Task 1 ending •••••••••••••••••••••••••••••••••••••••••••••••••••••••
sites = []
# task 3 *************************************************************
file = open('CyberSecurity2022.pcap', 'rb')
for line in file:
    string = line.decode('ISO-8859-1')
    xyz = re.findall(".top", string)
    if (xyz):
        if len(string) <50:
            if string not in sites:
                sites.append(string)

for site in sites:
    if "Origin" in site:
        site = site.replace("\n", "")
        print("The Suspected Website is ", site.replace("Origin: ",""))

    file = open('CyberSecurity2022.pcap', 'rb')
    x = file.read()
    decoded = x.decode("iso-8859-1")

    searchengines = ["www.google.com", "www.yahoo.com", "www.ask.com", "www.bing.com",
                     "www.aol.com", "www.baidu.com", "www.wolframalpha.com",
                     "www.duckduckgo.com", "www.yandex.ru"]

    searchenginesfound = []

    for i in searchengines:
        if i in decoded:
            searchenginesfound.append(i)

    if searchenginesfound.__len__() == 0:
        print("Search engine not found")
    elif searchenginesfound.__len__() == 1:
        print("Search Engine used: ", searchenginesfound)
    elif searchenginesfound.__len__() > 1:
        print("Search Engines used: ", searchenginesfound)
print("seconds :",seconds)
print("micro seconds:", micro)
file.close()
#Task 3 end*******************************************
#Task 1 ************************************

file = "CyberSecurity2022.pcap"
def magicNo():
    pcap =open(file,"rb")
    magic= pcap.read(4)
    magicNo=macAdd(magic)
print("magic Number: ", magic)
if magicNo == ("d4:c3:b2:a1"):
    global end
    end = 'little'
    print("little endain found")
else:
    print("big endian found")

pcapfile=open('CyberSecurity2022.pcap', "rb")
header = pcapfile.read(24)
print("Global header length:    bytes", len(header))

m1 = str().replace("X", "")
m2 = m1.replace("\\", "")
m3 = m2.replace("\'", "")

if m3 == "bd4c3b2a1":
    endianness = "big endian - no need to reverse the following bytes"
else:
    endianness = "little endian - reversing current bytes"
print(m3, endianness)
pcapfile.close()
#Task 1 ending******************************************************
import Second2

choice1 = '0'
while choice1 == '0':
    print("Would you like to access one of our extra features?")
    print("-" * 100)
    print("1 = Access a Port Scanner")  # scan a preferred IP (user input)
    print("2 = Access a GUI")  # run a port scan again
    print("3 = Exit to terminal")  # end
    print("-" * 100)
    choice1 = input("Option Selection: ")  # user choice
    if choice1 == '1':
        print(feature1()) # prints the "def" code from the other file
    elif choice1 == '2':
        import CyberSecUI

    elif choice1 == '3':
        sys.exit()  # exits the code/ finishes
#Extra Features section Ended!


