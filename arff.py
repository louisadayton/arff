import pandas as pd


def isNumeric(column): 
    for item in column:
        if type(item) != float and type(item) != int:
            return False   
    return True

df = pd.read_table("cool_file.txt")

writeFile = open("output.txt", 'w')

for colName in list(df):		
    writeFile.write("@ATTRIBUTE\t" + colName)
    options = set([])
    if isNumeric(df[colName]) == True:
        writeFile.write("\tNUMERIC\n") 
    else:
        writeFile.write("\t{")
        for value in df[colName]:
            options.add(value)
        writeFile.write(str(options.pop()))
        for o in options:
            writeFile.write("," + str(o))
        writeFile.write("}\n")
writeFile.write("\n") 
writeFile.close() 
