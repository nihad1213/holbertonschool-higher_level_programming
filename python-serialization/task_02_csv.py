#!/usr/bin/python3
"""
    Module containing functions that takes CSV and converts to JSON
"""
import csv
import json


def convert_csv_to_json(filename):
    """Function to convert CSV to JSON"""

    try:
        # Reading the csv file
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            # Changing content to list
            data = list(reader)

        # Writing content as JSON to the file
        json_filename = 'data.json'
        with open(json_filename, 'w') as file:
            json.dump(data, file, indent=4)
            return True

    # Exception handling
    except Exception as e:
        print("An error occurred:", e)
        return False


csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
