import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv("student_data.csv")

# 2. Basic check
print(df.head())
print(df.info())

# 3. Cleaning
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# 4. Visualization
sns.histplot(df[df.columns[0]])
plt.show()