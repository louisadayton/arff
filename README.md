# Pandas to X

Converts a pandas dataframe to and from different formats, including:

- [ARFF](https://www.cs.waikato.ac.nz/ml/weka/arff.html)
- [GCT](http://software.broadinstitute.org/cancer/software/genepattern/file-formats-guide#GCT)
- More to come...

## Requirements

- Python >=3.5
- Pandas >=0.22.0

## Examples

### Pandas Dataframe &harr; ARFF

```python
import pandas as pd
df = pd.read_table("cool_file.txt", sep="\t")

import arff
arff.toARFF(df, "output_file.arff")
```
```python
import pandas as pd

import arff_to_pandas
arff_to_pandas.arffToPandas("input_file.csv)
```

### Pandas Dataframe &harr; GCT

```python
import pandas as pd
df = pd.read_table("input_file.csv")

import gct
gct.toGCT(df, "output_file.gct")
```

```python
import pandas as pd

import gct_to_pandas
gct_to_pandas.gctToPandas("input_file.csv")
```


## Other

This is part of the [ShapeShifter](https://github.com/srp33/ShapeShifter) project.