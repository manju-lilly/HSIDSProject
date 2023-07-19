import json
import os

def analyze_json(file_path):
    global hasnested, notnested  # Declare global variables
    with open(file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        # Check if the JSON data has the desired structure
        if '_source' in data and 'body_nested' in data['_source']:
            body_nested = data['_source']['body_nested']
            # Perform analysis on the nested_body tags
            # Example: Print the nested_body content
            # print(body_nested)
            hasnested += 1
            print("count of hasnested:", hasnested)
        else:
            print("No 'body_nested' tag found in the JSON data.")
            notnested += 1
            print("count of notnested:", notnested)
    print (hasnested, notnested)


# Provide the path to your folder containing JSON files
folder_path = r"C:\Users\aksi.adiletsultan@lilly.com\Documents\fda"

# Check if the folder exists
if os.path.isdir(folder_path):
    # Get a list of files in the folder
    file_list = os.listdir(folder_path)
    hasnested = 0
    notnested = 0
    # Iterate over the files
    for file_name in file_list:
        # Check if the file is a JSON file
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            analyze_json(file_path)
        
else:
    print(f"The folder '{folder_path}' does not exist.")
