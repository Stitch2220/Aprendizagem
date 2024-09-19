import pandas as pd
from scipy.io.arff import loadarff

data = loadarff('breast.w.arff')
df = pd.DataFrame(data[0])

print(df)