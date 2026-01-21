import numpy as np

def preprocess(df):
    """
    Simple preprocessing:
    - Use first column only
    - Convert to numpy array
    """
    X = df.iloc[:, 0].values.reshape(-1, 1)
    return X
