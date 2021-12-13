import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston

boston = load_boston()
boston_df = pd.DataFrame(data = boston.data, columns = boston.feature_names)
boston_df['MEDV'] = boston.target

# Line chart
boston_df = boston_df.sort_values(by = ["AGE"])
plt.plot(boston_df['AGE'][:20], boston_df['MEDV'][:20], color = 'blue', marker = "o")
plt.title('Line chart demo')
plt.xlabel('Age')
plt.ylabel('Med. Value')
plt.show()

# Scatter plot
plt.scatter(boston_df['TAX'][:100], boston_df['MEDV'][:100], color = 'green', marker = "o")
plt.title('Scatter plot demo')
plt.xlabel('Tax')
plt.ylabel('Med. Value')
plt.show()

labels = ['0 - 10', '10 - 20', '20 - 30', '30 - 40', '> 40']
data = pd.cut(boston_df['MEDV'], bins = [0, 10, 20, 30, 40, 50], labels = labels, include_lowest = True).value_counts()
ordered_data = [data[label] for label in labels]

# Bar graph
plt.bar(labels, ordered_data)
plt.xlabel('Median values')
plt.ylabel('Number of records')
plt.title('Bar graph demo')
plt.show()

# Pie chart
plt.pie(ordered_data, labels = labels, autopct='%1.1f%%')
plt.title('Median values')
plt.show()

# Histogram
plt.hist(boston_df['MEDV'], bins = 25)
plt.xlabel('Med. Value')
plt.ylabel('No. of records')
plt.title('Histogram demo')
plt.show()

# Heatmap
corr_mat = boston_df.corr().round(2)
sns.set(rc = {'figure.figsize': (11.7, 8.27)})
sns.heatmap(data = corr_mat, annot = True)
plt.title('Heatmap demo')
plt.show()