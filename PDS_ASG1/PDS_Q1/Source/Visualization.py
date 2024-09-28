# Stage 3: Data Visualization

# Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset again
cleaned_data_file_path = '/content/cleaned_participant_data.csv'  # Update with your file path
data = pd.read_csv(cleaned_data_file_path)

# Set the seaborn style
sns.set(style='whitegrid')

# Create a box plot to show grip strength by frailty status
plt.figure(figsize=(8, 5))
sns.boxplot(x='Frailty', y='Grip strength', data=data)
plt.title('Grip Strength by Frailty Status')
plt.xlabel('Frailty (0 = Non-Frail, 1 = Frail)')
plt.ylabel('Grip Strength (kg)')
plt.xticks(ticks=[0, 1], labels=['Non-Frail', 'Frail'])
plt.savefig('/content/grip_strength_boxplot.png')  # Update with your file path
plt.show()


#2nd one 

# Create a scatter plot for grip strength versus age
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Grip strength', hue='Frailty', data=data)
plt.title('Grip Strength vs. Age')
plt.xlabel('Age (years)')
plt.ylabel('Grip Strength (kg)')
plt.legend(title='Frailty', loc='upper right', labels=['Non-Frail', 'Frail'])
plt.savefig('/content/grip_strength_scatterplot.png')  # Update with your Google Drive path
plt.show()

#3rd one
# Create a regression line plot
plt.figure(figsize=(8, 5))
sns.regplot(x='Height', y='Grip strength', data=data, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Regression Line for Grip Strength vs. Height')
plt.xlabel('Height (inches)')
plt.ylabel('Grip Strength (kg)')
plt.savefig('/content/grip_strength_height_regression.png')  # Update with your Google Drive path
plt.show()
