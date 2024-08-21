# Illumio
Take Home Assessment


Overview
This project consists of three main Python scripts designed to process flow log data and clean CSV and log files:

main.py: Processes flow log data and tags each log entry based on a lookup table. It generates output files containing the counts of each tag and each port/protocol combination.

clean_csv.py: Cleans a CSV file by removing leading and trailing whitespace from headers and data fields. It ensures that only non-empty rows are processed and written to the cleaned output file.

clean_flowlogs.py: Cleans a flow log file by removing leading and trailing whitespace from each line and discarding empty lines. The cleaned flow log is written to a new output file.

Prerequisites
Before running the scripts, ensure you have the following:

Python 3.x: The scripts are written in Python and require Python 3.x to run.

Required Libraries: The scripts use the built-in Python libraries (csv, collections, sys), so no additional installations are required.

CSV Files: The main.py and clean_csv.py scripts require input CSV files to operate.

Flow Log File: The main.py and clean_flowlogs.py scripts require a flow log file to process.
