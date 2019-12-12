# Read the wine-quality csv file from the URL
import pandas as pd
import logging

csv_url =\
    'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
try:
    data = pd.read_csv(csv_url, sep=';')
except Exception as e:
    logger.exception(
        "Unable to download training & test CSV, check your internet connection. Error: %s", e)

data.to_csv('~/data_trg/df.csv')