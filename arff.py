import pandas as pd
import re

def isNumeric(column): 
    for item in column:
        if type(item) != float and type(item) != int and item != "?":
            return False   
    return True

df = pd.read_table("cool_file.txt")
df = df.fillna("?")
fileName = "output.txt"
writeFile = open(fileName, 'w')
pattern = r"\..*"
relation = re.sub(pattern, "", fileName)
writeFile.write("@RELATION\t" + relation + "\n")
for colName in list(df):		
    writeFile.write("@ATTRIBUTE\t" + colName)
    options = set([])
    if isNumeric(df[colName]) == True:
        writeFile.write("\tNUMERIC\n") 
    else: 
        for value in df[colName]:
            options.add(value)
        if len(options) == len(df[colName]):
            writeFile.write("\tstring\n")
        else:
            writeFile.write("\t{")
            writeFile.write(str(options.pop()))
            for o in options:
                writeFile.write("," + str(o))
            writeFile.write("}\n")
writeFile.write("@DATA\n")
for line in df.values:
    writeFile.write(str(line[0]))
    for i in range(1, len(line)):
        if " " in str(line[i]):
            writeFile.write(",'" + str(line[i]) + "'")
            continue 
        writeFile.write("," + str(line[i])) 
    writeFile.write("\n")
 
 
writeFile.close() 
