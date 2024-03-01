import DataLoader
import json


# Load JSON data from file
with open('dataset.json') as f:
    json_data = json.load(f)


DataLoader = DataLoader

def main():
    # Format data into individual rows for event 5580
    formatted_rows = DataLoader.format_data_into_rows(json_data)
    # Print formatted rows
    for row in formatted_rows:
        print(row)
    

if __name__ == '__main__':
    main()
    