import csv
from collections import defaultdict
import sys

def load_lookup_table(file_path):
    """
    Loads the lookup table from a CSV file and returns a dictionary.
    
    The dictionary keys are tuples of (dstport, protocol), and the values are the corresponding tags.
    
    Args:
        file_path (str): The path to the lookup table CSV file.
    
    Returns:
        dict: A dictionary mapping (dstport, protocol) to tag.
    
    Raises:
        SystemExit: Exits the program if there is a FileNotFoundError or other exceptions during file loading.
    """
    lookup_table = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Extract and normalize dstport, protocol, and tag from the row
                    dstport = row['dstport'].strip()
                    protocol = row['protocol'].strip().lower()
                    tag = row['tag'].strip().lower()
                    lookup_table[(dstport, protocol)] = tag
                except KeyError as e:
                    # Handle missing columns in the CSV file
                    print(f"Error: Missing expected column in the lookup table: {e}")
                    sys.exit(1)
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"Error loading lookup table: {e}")
        sys.exit(1)
    return lookup_table

def process_flow_logs(flow_log_file, lookup_table):
    """
    Processes the flow logs and matches each log entry to a tag based on the lookup table.
    
    It also counts the occurrences of each tag and each (port, protocol) combination.
    
    Args:
        flow_log_file (str): The path to the flow log file.
        lookup_table (dict): The lookup table dictionary.
    
    Returns:
        tuple: A tuple containing two defaultdicts:
            - tag_counts: Counts of each tag.
            - port_protocol_counts: Counts of each (port, protocol) combination.
    
    Raises:
        SystemExit: Exits the program if there is a FileNotFoundError or other exceptions during file processing.
    """
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    try:
        with open(flow_log_file, 'r') as file:
            skipped_logs = 0
            for line in file:
                parts = line.split()
                if len(parts) < 12:
                    # Skip and log lines that do not have the expected number of parts
                    print(f"Skipped line (format issue): {line.strip()}")
                    print(f"Line split into {len(parts)} parts: {parts}")
                    skipped_logs += 1
                    continue
                
                try:
                    # Extract dstport and protocol, and normalize protocol to lowercase
                    dstport = parts[5].strip()
                    protocol_num = parts[7].strip()
                    protocol = 'tcp' if protocol_num == '6' else 'udp' if protocol_num == '17' else 'icmp'
                    
                    # Lookup the tag in the lookup table
                    tag = lookup_table.get((dstport, protocol), 'untagged')
                    tag_counts[tag] += 1
                    port_protocol_counts[(dstport, protocol)] += 1
                except IndexError as e:
                    # Handle any IndexErrors that might occur due to accessing invalid indices
                    print(f"Error processing line (IndexError): {line.strip()} - {e}")
                    skipped_logs += 1
                except ValueError as e:
                    # Handle any ValueErrors, e.g., when converting data types
                    print(f"Value error processing line: {line.strip()} - {e}")
                    skipped_logs += 1
                except Exception as e:
                    # Handle any other unexpected exceptions
                    print(f"Unexpected error processing line: {line.strip()} - {e}")
                    skipped_logs += 1
            # Report the number of skipped logs due to format issues
            print(f"Skipped {skipped_logs} logs due to format issues.")
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file {flow_log_file} was not found.")
        sys.exit(1)
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"Error processing flow logs: {e}")
        sys.exit(1)
    
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts):
    """
    Writes the output to two CSV files: one for tag counts and one for port/protocol combination counts.
    
    Args:
        tag_counts (defaultdict): The counts of each tag.
        port_protocol_counts (defaultdict): The counts of each (port, protocol) combination.
    
    Raises:
        SystemExit: Exits the program if there is an IOError or other exceptions during file writing.
    """
    try:
        # Write the tag counts to a CSV file
        with open('tag_counts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Tag', 'Count'])
            for tag, count in sorted(tag_counts.items()):
                writer.writerow([tag, count])
        
        # Write the port/protocol counts to a CSV file
        with open('port_protocol_counts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Port', 'Protocol', 'Count'])
            for (port, protocol), count in sorted(port_protocol_counts.items()):
                writer.writerow([port, protocol, count])
    except IOError as e:
        # Handle IO errors when writing to files
        print(f"Error writing to output file: {e}")
        sys.exit(1)
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error writing output files: {e}")
        sys.exit(1)

def main(flow_log_file, lookup_table_file):
    """
    Main function that orchestrates the loading of the lookup table, processing of flow logs, and writing of output.
    
    Args:
        flow_log_file (str): The path to the flow log file.
        lookup_table_file (str): The path to the lookup table file.
    """
    lookup_table = load_lookup_table(lookup_table_file)
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_file, lookup_table)
    write_output(tag_counts, port_protocol_counts)

if __name__ == "__main__":
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <flow_log_file> <lookup_table_file>")
        sys.exit(1)
    
    flow_log_file = sys.argv[1]
    lookup_table_file = sys.argv[2]
    
    # Run the main function with provided arguments
    main(flow_log_file, lookup_table_file)
