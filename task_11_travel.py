import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_1 = pd.read_csv("5 train.csv")
df_1["datetime"] = pd.to_datetime(df_1["datetime"])

df_1['hour'] = df_1['datetime'].dt.hour
weekend_data = df_1[df_1['workingday'] == 0]
hourly_counts = weekend_data.groupby('hour')['count'].sum().reset_index()
max_hour = hourly_counts.loc[hourly_counts['count'].idxmax()]
print(f"Час суток с максимальным числом поездок в выходные: {max_hour['hour']}:00")
print(f"Количество поездок: {max_hour['count']}")