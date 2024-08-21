import csv

def clean_csv(input_file_path, output_file_path):
    """
    Cleans a CSV file by removing leading and trailing whitespace from both headers and data fields.
    
    This function reads a CSV file, strips any leading or trailing spaces from the header names and each field in the rows,
    and writes the cleaned data to a new CSV file. It also ensures that only non-empty rows are processed.
    
    Args:
        input_file_path (str): The path to the input CSV file that needs to be cleaned.
        output_file_path (str): The path where the cleaned CSV file will be written.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there is an error in reading the input file or writing the output file.
    """
    try:
        # Open the input and output CSV files with UTF-8 encoding
        with open(input_file_path, 'r', newline='', encoding='utf-8') as infile, \
             open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            # Read the header row from the input CSV
            headers = next(reader)
            headers = [header.strip() for header in headers]  # Remove leading/trailing spaces from headers
            writer.writerow(headers)  # Write cleaned headers to the output CSV
            
            # Process each row in the input CSV
            for row in reader:
                # Only process non-empty rows (ignoring rows where all fields are empty)
                if any(field.strip() for field in row):
                    cleaned_row = [field.strip() for field in row]  # Remove leading/trailing spaces from each field
                    writer.writerow(cleaned_row)  # Write cleaned row to the output CSV
    
    except FileNotFoundError:
        # Handle case where the input file is not found
        print(f"Error: The file {input_file_path} was not found.")
    except IOError as e:
        # Handle IO errors related to file reading or writing
        print(f"Error processing files: {e}")

# Example usage of the clean_csv function
# Replace 'lookup_table.csv' with the path to your input CSV file and 'lookup_table_clean.csv' with the desired output file path
clean_csv('lookup_table.csv', 'lookup_table_clean.csv')
