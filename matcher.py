import pandas as pd
import os
from difflib import SequenceMatcher

# set reference file path
ref_file_path = './Cloud Vision Api/extract_raw.txt'

# list all folders
folders = os.listdir('./')

# create empty list to store results
results = []

# loop through each folder and compare with reference file
for folder in folders:
    if os.path.isdir(folder):
        extract_file_path = os.path.join(folder, 'extract_raw.txt')
        if os.path.isfile(extract_file_path):
            with open(ref_file_path, 'r') as ref_file, open(extract_file_path, 'r') as extract_file:
                ref_text = ref_file.read()
                extract_text = extract_file.read()
                # calculate text matching percentage using SequenceMatcher
                matcher = SequenceMatcher(None, ref_text, extract_text)
                percentage = matcher.ratio() * 100
                # add results to list
                results.append({'Folder': folder, 'Matching Percentage': percentage})

# create pandas dataframe from results and display
df = pd.DataFrame(results)
print(df)
