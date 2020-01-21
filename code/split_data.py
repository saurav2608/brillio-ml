import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(40)

# Read the wine-quality csv file from the data folder 
data = pd.read_csv('./data/df.csv')


# Split the data into training and test sets. (0.75, 0.25) split.
train, test = train_test_split(data)

train.to_csv('./data_trg/train.csv')
test.to_csv('./data_trg/test.csv')