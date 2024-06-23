## Description
This tool reads extended attributes of multiple files consecutively and writes the results to an output file, this allows you to test the classification of multiple files with automation.

## Prerequisites
* Python version 3.0 or higher installed

## Usage
Simply edit the variables defined in the beginning of the program to include the correct directories and desired paths. After ensuring these variables are defined correctly, you may just run the program as is.
### Example running as a python script:
```
python main.py
```
### Sample Output File
output.csv
```
Filename, Policy Name, Rule Name, File Sensitive
2020.xlsx,Employee Privacy - Devices (NEW),Employee Privacy RULE - Devices Only (NEW), TRUE
2021.xlsx,Employee Privacy - Devices (NEW),Employee Privacy RULE - Devices Only (NEW), TRUE
2022.xlsx,Employee Privacy - Devices (NEW),Employee Privacy RULE - Devices Only (NEW), TRUE
22024-SoToxa.docx,DefaultPolicy,DefaultRule, FALSE
ah2.pdf,DefaultPolicy,DefaultRule, FALSE
AH2_NegativeComplete.xlsx,DefaultPolicy,DefaultRule, FALSE
AH2_PositiveComplete.xlsx,AH2 - Patient Privacy (Devices),AH2-DevicesRULE-HIGH, TRUE
Alberta Area Employee Roster.xlsx,Employee Privacy - Devices (NEW),Employee Privacy RULE - Devices Only (NEW), TRUE
APR_Leavers0424.xlsx,Employee Privacy - Devices (NEW),Employee Privacy RULE - Devices Only (NEW), TRUE
cat.jpg,UNSUPPORTED,UNSUPPORTED, UNSUPPORTED
Company Health Profile.xlsx,DefaultPolicy,DefaultRule, FALSE
```

## Final Remarks
This tool is intented for use as a Microsoft Purview Endpoint Dlp File Classication Tester.


