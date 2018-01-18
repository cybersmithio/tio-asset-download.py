#!/usr/bin/python
#
# Takes a Tenable.io asset data and generates a CSV report.
# The output file is called tio-asset-download.csv
#
# Example usage with environment variables:
# TIOACCESSKEY="********************"; export TIOACCESSKEY
# TIOSECRETKEY="********************"; export TIOSECRETKEY
# TIOREPOSITORY="reponame"; export TIOREPOSITORY
# ./tio-asset-download.py 
#



import json
import os
import csv
import sys
from tenable_io.api.models import Folder
from tenable_io.client import TenableIOClient
from tenable_io.exceptions import TenableIOApiException
from tenable_io.api.models import AssetList, AssetInfo, VulnerabilityList, VulnerabilityOutputList

def GenerateReport(accesskey,secretkey,filename):
	client = TenableIOClient(access_key=accesskey, secret_key=secretkey)

	#Gather the list of repositories
	resp=client.get("assets")
	respdata=json.loads(resp.text)

	with open(filename,"w") as csvfile:
        	fieldnames=['id','has_agent','last_seen','sources','ipv4','ipv6','fqdn','netbios_name','operating_system','mac_address']
        	writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
       		writer.writeheader()
		for i in respdata['assets']:
			sys.stdout.write(".")
			sys.stdout.flush()
			resp=client.get("assets/"+str(i['id']))
			extrarespdata=json.loads(resp.text)
			
			rowdict={'id':i['id'], 'has_agent': i['has_agent'], 'last_seen': i['last_seen'],'sources': i['sources'], 'ipv4': i['ipv4'], 'ipv6': i['ipv6'], 'fqdn': i['fqdn'], 'netbios_name': i['netbios_name'], 'operating_system': i['operating_system'], 'mac_address': extrarespdata['mac_address']}
			writer.writerow(rowdict)
		print("")

	csvfile.close()
	return

################################################################
# Start of program 
################################################################
#Set debugging on or off
DEBUG=True

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

if DEBUG:
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

GenerateReport(accesskey,secretkey,"tio-asset-download.csv")


