
import argparse
import os

def add_hex_to_file(file_path, hex_string, position):
    # Convert hex string to bytes
    hex_data = bytes.fromhex(hex_string)
    
    # Read the original file content
    with open(file_path, 'rb') as f:
        original_content = f.read()
    
    # Modify content based on the specified position
    if position == "start":
        modified_content = hex_data + original_content
    elif position == "end":
        modified_content = original_content + hex_data
    elif position.isdigit():
        offset = int(position)
        modified_content = original_content[:offset] + hex_data + original_content[offset:]
    else:
        raise ValueError("Invalid position. Use 'start', 'end', or an integer for custom offset.")
    
    # Write the modified content back to the file
    with open(file_path, 'wb') as f:
        f.write(modified_content)

    print(f"Hex data added to {file_path} at position: {position}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add hex data to a file at a specified position.")
    parser.add_argument("file", help="Path to the file to modify.")
    parser.add_argument("hex", help="Hex string to add.")
    parser.add_argument("position", help="Position to add hex data ('start', 'end', or an integer for a custom offset).")

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("File not found.")
    else:
        add_hex_to_file(args.file, args.hex, args.position)
