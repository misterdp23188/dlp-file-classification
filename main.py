import os, subprocess, re

collectedData = []
failedFiles = []


fileDirectory = 'C:/MDE/TestFiles/'
exePath = 'C:/MDE/Tools/DisplayExtendedAttribute.exe'
outputFilename = 'output.csv'

"""
# ask user for filepaths / directories

fileDirectory = input("File directory absolute path: ")
exePath = input("Executable path: ")
outputFilename = input("Output filename / path: ")

if exePath == "":
    exePath = "C:/MDE/Tools/DisplayExtendedAttribute.exe"

"""

# regular expressions for parsing the output later
regex1 = r'PolicyName\s*:\s*(.*)\n'
regex2 = r'RuleName\s*:\s*(.*)\n'
regex3 = r'File Sensitive\s*:\s*(TRUE|FALSE)'


for filename in os.listdir(fileDirectory):
    print('-----------------------------------------------------------------------------')
    data = {
    
    }
    # run command for file and capture output
    output = subprocess.run([exePath, fileDirectory + filename], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    
    # parse output
    policyNameMatch = re.search(regex1, output)
    ruleNameMatch = re.search(regex2, output)
    fileSensitiveMatch = re.search(regex3, output)
    data["filename"] = filename
    if policyNameMatch:
        data["policyName"] = policyNameMatch.group(1).replace("\r", "")
    if ruleNameMatch:
        data["ruleName"] = ruleNameMatch.group(1).replace("\r", "")
    if fileSensitiveMatch:
        data["fileSensitive"] = fileSensitiveMatch.group(1)
    
    try:
        print(f'{filename}: {data["policyName"]}, {data["ruleName"]}, {data["fileSensitive"]}')
    except:
        failedFiles.append(filename)
        data["policyName"] = "Unsupported".upper()
        data["ruleName"] = "Unsupported".upper()
        data["fileSensitive"] = "Unsupported".upper()
    
    collectedData.append(data)
    
    
# create csv file from output
allData = "Filename, Policy Name, Rule Name, File Sensitive\n"

for x in collectedData:
    data = f"{x["filename"]},{x["policyName"]},{x["ruleName"]}, {x["fileSensitive"]}\n"
    allData += data


if len(failedFiles) > 0:
    print('---------------------------------------------------------------------------------------------------')
    print("\nFiletype unsupported for the following files:")
    for x in failedFiles:
        print(x)


f = open(outputFilename, 'w')
f.write(allData)
f.close()