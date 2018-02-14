#!/usr/bin/python
#
# Takes a Tenable.io asset data and generates a CSV report.
# The output file is called tio-asset-download.csv
#
# Example usage with environment variables:
# TIOACCESSKEY="********************"; export TIOACCESSKEY
# TIOSECRETKEY="********************"; export TIOSECRETKEY
# ./tio-asset-download.py
#
# This script requires the Tenable.io Python SDK to be installed.
# If this is not already done, then run pip install tenable_io
#

import json
import os
import csv
import sys
from tenable_io.client import TenableIOClient

def GenerateAssetCSV(accesskey,secretkey,filename):
	#Create the connection to Tenable.io
	client = TenableIOClient(access_key=accesskey, secret_key=secretkey)

	#Gather the list of assets
	resp=client.get("assets")
	respdata=json.loads(resp.text)

	#Open the file that will become a CSV
	with open(filename,"w") as csvfile:
		#Create the header of the CSV file
		fieldnames=['id','has_agent','last_seen','sources','ipv4','ipv6','fqdn','netbios_name','operating_system']

		#Create a CSV writer and associate with the file handle
		writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
		#Write the CSV headers
		writer.writeheader()

		#Loop through all the downloaded assets and write them into the CSV file
		for i in respdata['assets']:
			rowdict={'id':i['id'], 'has_agent': i['has_agent'], 'last_seen': i['last_seen'],'sources': i['sources'], 'ipv4': i['ipv4'], 'ipv6': i['ipv6'], 'fqdn': i['fqdn'], 'netbios_name': i['netbios_name'], 'operating_system': i['operating_system']}
			writer.writerow(rowdict)

	#Close the file
	csvfile.close()
	return(True)

################################################################
# Start of program 
################################################################

# First we need the Tenable.io Access Key and Secret key.
# This program will check the environment variables first,
# the command line second, and finally it will prompt the user
# for the keys if it cannot find them elsewhere.

#Pull as much information from the environment variables
# as possible, and where missing then initialize the variables.
if os.getenv('TIOACCESSKEY') is None:
        accesskey=""
else:
        accesskey=os.getenv('TIOACCESSKEY')

if os.getenv('TIOSECRETKEY') is None:
        secretkey=""
else:
        secretkey=os.getenv('TIOSECRETKEY')

print "Connecting to cloud.tenable.com with access key",accesskey,"to report on assets"

#Pull information from command line.  If nothing there,
# and there was nothing in the environment variables, then ask user.
if len(sys.argv) > 1:
        accesskey=sys.argv[1]
else:
        if accesskey == "":
                accesskey=raw_input("Access key:")

if len(sys.argv) > 2:
	secretkey=sys.argv[2]
else:
	if secretkey == "":
        	secretkey=raw_input("Secret key:")

#Download the asset list into a CSV
GenerateAssetCSV(accesskey,secretkey,"tio-asset-download.csv")


