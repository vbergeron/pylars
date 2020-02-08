# pylars
A declarative interface to build pipelines using pandas.

## Installation

Available on pypi :
```bash
pip install pylars
```

## Features
* Declarative and chained interface for most common operations
* Compile on the fly to a function to reuse and delay computation
* Basic schema check at each step

## Exemple
```python
import pandas
from pylars import Pylar
from pylars.dsl import _
from pylars.dsl import Count

df = pandas.DataFrame({
    "tag": ["a", "a", "b", "b"],
    "val": [1, 2, 5, 4]
})

# build a checked representation of the computation
task = (Pylar("exemple", df.schema)
        .assign(mod4=_.val % 4)
        .filter(_.tag == "a")
        .compile())

# real computation start here
task(df)
```