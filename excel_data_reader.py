import os
# import pandas lib as pd
import pandas as pd
from pathlib import Path

from configparser import ConfigParser

config = ConfigParser()
config.read('configurations.ini')

# Remove dirty output file if it already exists
try:
    os.remove(config.get("Settings","outputfilepath"))
except OSError:
    pass

# iterate to read all xlsx files in filesFolder path
inputFilesFolder = config.get('Settings', 'inputdatafilesfolder')
print("Reading excel files from folder: ", inputFilesFolder)

filteredXlsFiles = Path(inputFilesFolder).glob('*.xlsx')
columns = list(config.get("Settings","columnstoextract").split(","))
excl_files_list = []
not_req_sheets = []

for filename in filteredXlsFiles:
    print("Reading : ", filename)
    xl = pd.ExcelFile(filename)
    for sheet_name in xl.sheet_names:
        if sheet_name not in not_req_sheets:
            df = pd.read_excel(filename,sheet_name=sheet_name)
            excl_files_list.append(df)

result = pd.concat(excl_files_list, ignore_index=True)
print(result)
output = (result
  .groupby(config.get("Settings","sumOverColumns"), sort=True, as_index=False)
  .sum())
print(output)
output.to_excel(config.get("Settings","outputfilepath"), index=False, columns=columns)
print("Final result can be found at : ", filename)
