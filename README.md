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

# TODO: add arff->pd example
```

### Pandas Dataframe &harr; GCT

```python
# TODO: add examples
```