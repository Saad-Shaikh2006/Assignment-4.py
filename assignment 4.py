# Attempt to open and read the file
try:
    with open("sample.txt", "r") as file:
        # Print each line after stripping extra whitespace
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: 'sample.txt' not found. Please check that the file exists and the name is correct.")
