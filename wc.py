from pathlib import Path
import os
import string

OUTPUT_FILE = "summary.log"

def read_file(inp_path, flg):
    data = ''
    if flg == 1:
        with open(inp_path) as fh:
            data = fh.read()
    elif flg == 2:
        with open(inp_path) as fh:
            data = fh.readlines()

    return data

def char_count(data):
    return len(data)

def punctuation_count(data):
    count = 0
    for char in data:
        if char in string.punctuation:
            count += 1

def main():
    # Read the path from the user
    inp_path = input("Enter the filepath: ")

    # check if path exists & is not a directory
    if not os.path.exists(inp_path):
        print("The file does not exist")


    p = Path(inp_path)

    # Open the file and read it
    data = read_file(inp_path,1)

    # summary
    summary = {}
    summary["Number of characters"] = char_count(data)
    summary["Number of punctuation"] = punctuation_count(data)

    # Add other counts


    with open(OUTPUT_FILE, "a+") as fh:
        fh.write(f"Summary of {p.name} \n")
        fh.write("-"*60+"\n")

        for k, v in summary.items():
            fh.write(f"{k}: {v}\n")
        
if __name__ == '__main__':
    main()