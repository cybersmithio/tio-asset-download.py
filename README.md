![Logo](https://github.com/cybersmithio/tio-asset-download.py/blob/master/TenableAPI.png)

# Summary
A Python script to download the assets from Tenable.io and store in a CSV format.

# Requirements
You can download Python for Unix, Windows, and Mac at https://www.python.org/

This script requires the Tenable.io Python SDK from https://github.com/tenable/Tenable.io-SDK-for-Python/


A quick way to install the Tenable.io Python SDK is to run this command:


pip install tenable_io



This script needs the Tenable.io SDK, which can be found at https://github.com/tenable/Tenable.io-SDK-for-Python/tree/master/tenable_io

# Linux/Unix Example With Environment Variables
TIOACCESSKEY="******************"; export TIOACCESSKEY

TIOSECRETKEY="******************"; export TIOSECRETKEY

./tio-asset-download.py 

This will produce a file called tio-asset-download.csv
