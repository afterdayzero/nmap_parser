# nmap_parser

This program uses the nmap library to scan a host or a list of hosts and generate an HTML report with the scan results.

## Prerequisites
Python 3.x
The nmap library (pip install nmap)

## Usage
To run the program, use the following command:
`python scan.py`
You will be prompted to choose between a single target or a list of targets.

## Single target
If you choose to scan a single target, you will be prompted to enter the host to scan.

Enter the host to scan: example.com

## List of targets
If you choose to scan a list of targets, you will be prompted to enter the name of the file containing the list of hosts.

Enter the name of the file containing the list of hosts: hosts.txt
The file should contain one host per line.

## Output
The program will generate an HTML report in the report folder. The report will contain a summary section for each host, showing the number of open ports found, and a table with the details for each port.

The report will be opened automatically in your default web browser.
