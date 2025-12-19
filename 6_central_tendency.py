import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the CSV file
df = pd.read_csv('/data.csv', delimiter=',')



# Compute Central Tendency Measures
numeric_columns = [
    "Admission grade",
    "Age at enrollment",
    "Curricular units 1st sem (grade)",
    "Curricular units 2nd sem (grade)",
    "Unemployment rate",
    "Inflation rate",
    "GDP"
]



mean_vals = df[numeric_columns].mean()
median_vals = df[numeric_columns].median()
mode_vals = df[numeric_columns].mode().iloc[0]



print("=== Mean ===\n", mean_vals)
print("\n=== Median ===\n", median_vals)
print("\n=== Mode ===\n", mode_vals)



# Set plot aesthetics
sns.set(style="whitegrid")
plt.figure(figsize=(16, 20))



# 1. Pie Plot – Target Distribution
plt.subplot(3, 2, 1)

target_counts = df["Target"].value_counts()

plt.pie(
    target_counts,
    labels=target_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("pastel")
)

plt.title("Target Distribution (Graduate vs Dropout)")



# 2. Box Plot – Semester Grades
plt.subplot(3, 2, 2)

sns.boxplot(
    data=df[
        [
            "Curricular units 1st sem (grade)",
            "Curricular units 2nd sem (grade)"
        ]
    ]
)

plt.title("Boxplot of Semester Grades")



# 3. Histogram – Age at Enrollment
plt.subplot(3, 2, 3)

sns.histplot(
    df["Age at enrollment"],
    bins=20,
    kde=False
)

plt.title("Histogram of Age at Enrollment")



# 4. Scatter Plot – Admission Grade vs 1st Sem Grade
plt.subplot(3, 2, 4)

sns.scatterplot(
    x="Admission grade",
    y="Curricular units 1st sem (grade)",
    data=df,
    alpha=0.6
)

plt.title("Admission Grade vs 1st Sem Grade")



# 5. Density Plot – 1st Semester Grades
plt.subplot(3, 2, 5)

sns.kdeplot(
    df["Curricular units 1st sem (grade)"],
    fill=True
)

plt.title("Density Plot of 1st Semester Grades")



plt.tight_layout()
plt.show()



"""
Output:

=== Mean ===
Admission grade                    126.978119
Age at enrollment                   23.265145
Curricular units 1st sem (grade)    10.640822
Curricular units 2nd sem (grade)    10.230206
Unemployment rate                   11.566139
Inflation rate                       1.228029
GDP                                  0.001969
dtype: float64

=== Median ===
Admission grade                    126.100000
Age at enrollment                   20.000000
Curricular units 1st sem (grade)    12.285714
Curricular units 2nd sem (grade)    12.200000
Unemployment rate                   11.100000
Inflation rate                       1.400000
GDP                                  0.320000
dtype: float64

=== Mode ===
Admission grade                    130.00
Age at enrollment                   18.00
Curricular units 1st sem (grade)     0.00
Curricular units 2nd sem (grade)     0.00
Unemployment rate                    7.60
Inflation rate                       1.40
GDP                                  0.32
Name: 0, dtype: float64
"""
