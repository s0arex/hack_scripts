#!/usr/local/bin/python

import os
import sys
import netifaces
import random
import time

usedAddresses = [""]

############################
# Generate a new address
############################
def randomMacAddress():
   mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), 
      random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
   return ':'.join(map(lambda x: "%02x" % x, mac))
 
def randomUnusedMacAddress():
	#print(",".join(usedAddresses))
	newAddress = ""
	while(newAddress in usedAddresses):
		newAddress = randomMacAddress()
 		
	usedAddresses.append(newAddress)
	
	print("----> " + newAddress)
	
	return newAddress
 	
 	
############################
# Hack the address
############################  
def changeAddress(ifg):
	while True:
		address = randomUnusedMacAddress()
		print("Changing the mac for interface '" + ifg + "'" + " " + address)
		os.system("sudo ifconfig en0 ether " + address)
	
		os.system("sudo ifconfig en0 down")
		os.system("sudo ifconfig en0 up")
	
		print("Done!!")
		time.sleep(60 * 30)


################
# Main code
################
print("Hello Python")

options = netifaces.interfaces()

print("Select an interface to hack your mac address: ")

for i in range(len(options)):
	print(str(i) + " " + options[i])

ifg = raw_input("Choose the number of the interface: ")

if( (not ifg.isdigit()) or int(ifg) >= len(options)):
	sys.exit("Invalid index '" +ifg +"'")
	
	
inteface_name = options[int(ifg)]
print("Do you really want to change the mac address for interface: " + inteface_name + "?")
confirmation = raw_input("[y/N]: ")

if confirmation in ['y', 'Y'] :
	changeAddress(inteface_name)
else:
	print("Operation aborted")


