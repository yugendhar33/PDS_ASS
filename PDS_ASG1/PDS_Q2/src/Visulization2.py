# Set up the figure size and plot the pie chart
plt.figure(figsize=(5,5))
plt.pie(lunchCount.values, labels=lunchCount.index, autopct='%1.1f%%')
plt.title("Distribution of Lunch Types")

# Save the plot to the local file system in Google Colab
save_path = r"C:\Users\NYR\Downloads\lunch_distribution_chart.png"
plt.savefig(save_path)

# Display the plot
plt.show()

# Download the saved plot to your local machine
files.download(save_path)

#2nd code 

# Create a scatter plot between reading and writing scores
plt.scatter(df['reading score'], df['writing score'], marker='o', color='b')

# Add labels and title to the plot
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title('Relationship Between Reading and Writing Scores')

# Save the plot to the Colab environment (since you're using Colab)
save_path = r"C:\Users\NYR\Downloads\reading_vs_writing_scores.png"
plt.savefig(save_path)

# Display the plot
plt.show()

# Optional: Download the saved plot to your local machine
from google.colab import files
files.download(save_path)

#3rd code 

plt.figure(figsize=(8, 6))
plt.hist(df['writing score'], bins=30, color='orange', edgecolor='white', alpha=0.7)

# Add labels and title to the plot
plt.xlabel('Writing Score')
plt.ylabel('Frequency')
plt.title('Distribution of Writing Scores')

# Save the histogram locally in Google Colab
save_path = r"C:\Users\NYR\Downloads\writing_scores_histogram.png"
plt.savefig(save_path)

# Display the histogram
plt.show()

# Download the saved plot to the local machine
files.download(save_path)

#4th code
#Create a histogram to visualize the distribution of percentages
plt.figure(figsize=(8, 6))
ax = sns.histplot(df['Percentage'], kde=False, color='orange', bins=20)

# Add labels and title to the plot
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Distribution of Percentages')

# Save the histogram locally in Google Colab
save_path = r"C:\Users\NYR\Downloads\distribution_percentage_histogram.png"
plt.savefig(save_path)

# Display the plot
plt.show()

# Download the saved plot to the local machine
files.download(save_path)

#5th code 

# Create a hexbin joint plot to visualize the relationship between Percentage and Reading Score
joint_plot = sns.jointplot(x='Percentage', y='reading score', data=df, kind='hex', cmap='Purples')

# Add title to the plot
joint_plot.fig.suptitle('Hexbin Plot of Percentage vs Reading Score', y=1.02)

# Save the joint plot locally in Google Colab
save_path = r"C:\Users\NYR\Downloads\hexbin_plot_percentage_vs_reading_score.png"
joint_plot.savefig(save_path)

# Display the plot
plt.show()

# Download the saved plot to the local machine
files.download(save_path)
