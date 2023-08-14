import pandas as pd
import matplotlib.pyplot as plt
# Code to create a Pie Chart that shows the percentage of Completed on time by Quarter than year
df = pd.read_csv('Completed_by_Employee.csv')
df['Week End'] = pd.to_datetime(df['Week End'])
df['Year'] = df['Week End'].dt.year
filtered_df = df[df['Year'].isin([2023,2024])]
grouped_df = filtered_df.groupby([filtered_df['Week End'].dt.to_period('Q').rename('Quarter'),
                                  filtered_df['Year']]).agg({'Tasks Completed on Time': 'sum'}).reset_index()
data_2023 = grouped_df[grouped_df['Year'] == 2023]
data_2024 = grouped_df[grouped_df['Year'] == 2024]

plt.figure(figsize=(8, 8))
plt.pie(data_2023['Tasks Completed on Time'], labels=data_2023['Quarter'].astype(str), autopct='%1.1f%%', startangle=90)
plt.title('Tasks Completed On Time By Quarter 2023')

plt.figure(figsize=(8,8))
plt.pie(data_2024['Tasks Completed on Time'], labels=data_2024['Quarter'].astype(str), autopct='%1.1f%%', startangle=90)
plt.title('Tasks Completed On Time By Quarter 2024')


# Put that same information in a Bar Chart
# Create a figure and axis
filtered_df = df[df['Year'].isin([2023, 2024])]
bar_chart_set_up = (filtered_df.groupby([filtered_df['Week End'].dt.to_period('Q').rename('Quarter'),
                                         filtered_df['Year']])
                    .agg({'Tasks Completed on Time': 'sum'}).reset_index())
x = bar_chart_set_up
data_2023 = x[x['Year'] == 2023]
data_2024 = x[x['Year'] == 2024]
Bar_2023 = data_2023.plot.bar(x='Quarter', y='Tasks Completed on Time', rot=0)
Bar_2024 = data_2024.plot.bar(x='Quarter', y='Tasks Completed on Time', rot=0)



