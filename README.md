![Logo] (https://github.com/cybersmithio/tio-asset-download.py/blob/master/TenableAPI.png)

# Summary
A Python script to download the assets from Tenable.io and store in a CSV format.

# Requirements
This script needs the Tenable.io SDK, which can be found at https://github.com/tenable/Tenable.io-SDK-for-Python/tree/master/tenable_io

# Usage Example With Environment Variables
TIOACCESSKEY="******************"; export TIOACCESSKEY

TIOSECRETKEY="******************"; export TIOSECRETKEY

./tio-asset-download.py 

This will produce a file called tiocs-asset-download.csv
