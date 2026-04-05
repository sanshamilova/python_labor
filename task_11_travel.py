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

avg = df_1.groupby('season').agg({
    'registered': 'mean',
    'casual': 'mean'
}).reset_index()
avg = avg.sort_values('season')
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(avg))
width = 0.35

bars1 = ax.bar(x - width/2, avg['registered'], width,
               label='Зарегистрированные', color='green', edgecolor='black')
bars2 = ax.bar(x + width/2, avg['casual'], width,
               label='Незарегистрированные', color='red', edgecolor='black')
plt.title("Зависимость числа поездок от сезона")
plt.xlabel("Время года")
plt.ylabel("Число поездок")
plt.show()