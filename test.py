import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

# Define the data
data = {
    'Performance Metric': [
        'Computational Power\n(FLOPS)',
        'Parallel Processing\n(Threads)',
        'High-Speed',
        'Power Efficiency',
        'Flexibility & Customizability\n(Scale 1-10)',
        'Development Time\n(Months)',
        'Cost Effectiveness\n(Scale 1-10)'
    ],
    'ARM': [5, 4, 8, 8, 6, 9, 8],
    'CISC': [6, 3, 7, 4, 4, 9, 7],
    'GPU': [9, 10, 4, 3, 6, 6, 5],
    'FPGA': [7, 8, 7, 7, 9, 5, 6],
    'SoM': [8, 9, 7, 8, 8, 7, 7],
    'SoC': [7, 7, 9, 7, 8, 5, 8],
    'ASIC': [10, 9, 10, 10, 3, 2, 2]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Performance Metric', inplace=True)

# Define the legend (score to performance mapping)
legend = {
    (0, 3): 'Very Low',
    (4, 6): 'Moderate',
    (7, 9): 'High',
    (10, 10): 'Very High'
}

# Function to map scores to performance levels
def map_performance(score):
    for range, performance in legend.items():
        if range[0] <= score <= range[1]:
            return performance

# Apply the mapping function to the DataFrame
df_legend = df.applymap(map_performance)

# Define the custom color map (red -> white -> blue)
colors = ['red', 'white', 'blue']  # Colors for Very Low, Moderate, Very High
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

# Set up the matplotlib figure
plt.figure(figsize=(12, 6))

# Create the heatmap
ax = sns.heatmap(df, annot=df_legend, fmt='', cmap=cmap, linewidths=.5, cbar_kws={'label': 'Performance Score'})

# Highlight the 'SoM' column with a red border
col_index = df.columns.get_loc('SoM')  # Get the column index of 'SoM'
for y in range(len(df.index)):
    rect = Rectangle((col_index + 0.5, y + 0.5), 1, 1, linewidth=2, edgecolor='red', facecolor='none')
    ax.add_patch(rect)

# Customize the heatmap
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title('Embedded Devices Performance Matrix with SoM Highlighted', pad=20)  # Title at the bottom with padding

# Show the plot
plt.tight_layout()
plt.show()
