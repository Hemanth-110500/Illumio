def clean_flow_log_file(input_file, output_file):
    """
    Cleans a flow log file by removing leading and trailing whitespace from each line
    and discarding empty lines.
    
    This function reads a flow log file line by line, removes any leading or trailing whitespace,
    and writes the cleaned lines to a new output file. Empty lines are ignored.
    
    Args:
        input_file (str): The path to the input flow log file that needs to be cleaned.
        output_file (str): The path where the cleaned flow log file will be written.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there is an error in reading the input file or writing the output file.
    """
    try:
        # Open the input and output files
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Process each line in the input file
            for line in infile:
                cleaned_line = line.strip()  # Remove leading and trailing whitespace
                if cleaned_line:  # Check if the line is not empty after cleaning
                    outfile.write(cleaned_line + '\n')  # Write the cleaned line to the output file
    
    except FileNotFoundError:
        # Handle case where the input file is not found
        print(f"Error: The file {input_file} was not found.")
    except IOError as e:
        # Handle IO errors related to file reading or writing
        print(f"Error processing files: {e}")

if __name__ == "__main__":
    # Example usage of the clean_flow_log_file function
    # Replace 'vpc_flowlogs.txt' with the path to your input log file
    # Replace 'cleaned_vpc_flow_logs.txt' with the desired output file path
    input_file = 'vpc_flowlogs.txt'
    output_file = 'cleaned_vpc_flow_logs.txt'
    
    # Call the function to clean the flow log file
    clean_flow_log_file(input_file, output_file)
