import pandas as pd
import re

columnNames = []
dataList = []
pattern = r"@[Aa][Tt][Tt][Rr][Ii][Bb][Uu][Tt][Ee]\s+([^\s]*)\s+.*"
with open("diabetes.arff") as dataFile:
    for line in dataFile: 
        line = line.rstrip("\n")
    
        if line.startswith("@ATTRIBUTE") or line.startswith("@attribute"):  
            columnNames.append(re.sub(pattern, r"\1", line)) 
            continue
        elif line.startswith("@") or line.startswith("%") or line == "":
            continue

        line = line.replace("?", "") 
        dataList.append(line.split(","))      
data = pd.DataFrame(dataList, columns = columnNames)
print(data.columns)
print(data.values)







