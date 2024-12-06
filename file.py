# File Read & Write Challenge 🖋️
def modify_and_write_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.readlines()  # Read all lines from the file

        # Modify the content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to {output_file} successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Error Handling Lab 🧪
def main():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the name of the file to read from: ")
    output_filename = input("Enter the name of the file to write to: ")

    # Call the function to modify and write the file
    modify_and_write_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
