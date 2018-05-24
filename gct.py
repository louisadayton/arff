import pandas as pd

df = pd.read_table("allaml.dataset.gct.txt")
df = df.fillna("")
fileName = "output.gct"

writeFile = open(fileName, 'w')
writeFile.write("#1.2\n")
writeFile.write(str(len(df.index))) 
writeFile.write("\t" + str(len(df.columns[2:])) + "\n")
for col in df.columns:
    writeFile.write(str(col) + "\t")
writeFile.write("\n")
for line in df.values:
    for word in line:
        writeFile.write(str(word) + "\t")
    writeFile.write("\n")
writeFile.close()	
