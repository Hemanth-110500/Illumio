# Illumio
Take Home Assessment


## Overview: 
This project consists of three main Python scripts designed to process flow log data and clean CSV and log files:

main.py: Processes flow log data and tags each log entry based on a lookup table. It generates output files containing the counts of each tag and each port/protocol combination.

clean_csv.py: Cleans a CSV file by removing leading and trailing whitespace from headers and data fields. It ensures that only non-empty rows are processed and written to the cleaned output file.

clean_flowlogs.py: Cleans a flow log file by removing leading and trailing whitespace from each line and discarding empty lines. The cleaned flow log is written to a new output file.

## Prerequisites: 
Before running the scripts, ensure you have the following:

Python 3.x: The scripts are written in Python and require Python 3.x to run.

Required Libraries: The scripts use the built-in Python libraries (csv, collections, sys), so no additional installations are required.

CSV Files: The main.py and clean_csv.py scripts require input CSV files to operate.

Flow Log File: The main.py and clean_flowlogs.py scripts require a flow log file to process.

## Directory Structure:

Your project directory should be structured as follows:

  FlowLogProcessing/


├── main.py

├── clean_csv.py

├── clean_flowlogs.py

├── lookup_table.csv

├── vpc_flowlogs.txt

├── cleaned_vpc_flow_logs.txt

└── lookup_table_clean.csv

main.py: Script to process flow logs and generate tag counts and port/protocol combination counts.

clean_csv.py: Script to clean a CSV file by removing unnecessary whitespace.

clean_flowlogs.py: Script to clean a flow log file by removing unnecessary whitespace.

lookup_table.csv: The lookup table used by main.py to tag flow logs.

vpc_flowlogs.txt: The raw flow log file to be cleaned and processed.

cleaned_vpc_flow_logs.txt: The cleaned version of the vpc_flowlogs.txt file generated by clean_flowlogs.py.

lookup_table_clean.csv: The cleaned version of the lookup_table.csv file generated by clean_csv.py.

## Scripts Usage: 

main.py

Description
The main.py script processes flow log data by matching each log entry with a tag from a lookup table. The script generates two output CSV files:

tag_counts.csv: Contains the counts of each tag.
port_protocol_counts.csv: Contains the counts of each port/protocol combination.

Command-Line Arguments:

<flow_log_file>: Path to the input flow log file (e.g., vpc_flowlogs.txt).
<lookup_table_file>: Path to the lookup table CSV file (e.g., lookup_table.csv).
