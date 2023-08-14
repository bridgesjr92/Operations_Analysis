# Questions to answer
# Figure out the average productive and non-productive ours for each month of year, Use Bar chart
import pandas as pd
import matplotlib.pyplot as plt

Utilization = pd.read_csv('Time_Utilization.csv')
Utilization['Date'] = pd.to_datetime(Utilization['Date'])
# Filtering the data for the year 2023
filtered_data = Utilization[Utilization['Date'].dt.year == 2023]
# Grouping and aggregating the data
result = filtered_data.groupby([filtered_data['Date'].dt.month.rename('month'), filtered_data['Date'].dt.year.rename('year')]).agg({
    'Non-Productive Hours': 'mean',
    'Productive Hours': 'mean'
}).reset_index()
# Sorting the result by 'Productive_Hours' in descending order
result = result.sort_values(by='Productive Hours', ascending=False)
print(result)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
# Define the bar width and positions
bar_width = 0.35
bar_positions = result['month']
# Plot 'Non_Productive_Hours' and 'Productive_Hours' as double bars
ax.bar(bar_positions - bar_width/2, result['Non-Productive Hours'], width=bar_width, label='Non Productive Hours')
ax.bar(bar_positions + bar_width/2, result['Productive Hours'], width=bar_width, label='Productive Hours')
# Set labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Average Hours')
ax.set_title('Average Non Productive Hours vs. Productive Hours')
# Set x-axis ticks and labels
ax.set_xticks(bar_positions)
ax.set_xticklabels(result['month'])
# Add legend
ax.legend()
# Show the plot
plt.show()