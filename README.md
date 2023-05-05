  # Script setup
re  This script takes the number of excel files from a folder, reads required columns' information and aggregates the information based on a certain criteria. (eg. Company name in given data)
1. Download python from https://www.python.org/downloads/ and install
2. Run cmd as admin
3. Run command ```pip install pandas```
4. Run command ```pip install xlrd```
5. Run command ```pip install openpyxl```
6. Add variables in main.py for inputDataFilesFolder (directory where .xlxs files are present), columnsToExtract (which columns do you want to extract), sumOverColumns (Column to group by and sum), outputFilePath (where you want to generate the final output excel file)
7. Run ```cd <cloned_repo_code_folder>```
8. Run ```py main.py```
9. Run  ```py excel_data_reader.py```
10. Make sure to close the input and output excel file windows from excel app to avoid permission denied error.
11. Output would be generated at specified outputFilePath.
