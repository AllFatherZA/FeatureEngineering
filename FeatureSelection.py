import pandas as pd
import numpy as np
import talib as ta
import seaborn as sns
import matplotlib.pyplot as plt
from ta.utils import dropna
from ta import add_all_ta_features

# Load stock price data from CSV file
df = pd.read_csv('GasPrices2023.csv')

# Calculate technical indicators using TA-Lib
df = add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True)


def plot_corr_heatmap(df):
    corr_matrix = df.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=False, cmap="viridis")
    plt.title("Correlation Matrix Heatmap")
    plt.show()
def drop_correlated_features(data, threshold):
    # Calculate the correlation matrix
    corr_matrix = data.corr().abs()

    # Create a mask for the upper triangle of the correlation matrix
    upper_mask = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find features with a correlation above the threshold
    to_drop = [column for column in upper_mask.columns if any(upper_mask[column] > threshold)]

    # Drop the correlated features
    data = data.drop(to_drop, axis=1)

    return data

plot_corr_heatmap(df)
df=drop_correlated_features(df,0.5)
plot_corr_heatmap(df)