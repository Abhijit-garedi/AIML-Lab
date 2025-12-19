import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA



# Load the dataset
df = pd.read_csv("data.csv", delimiter=',')



# Separate features and target
X = df.drop(columns=["Target"])
y = df["Target"]



# Keep only numeric columns
X = X.select_dtypes(include=[np.number])



# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)



# Explained variance
explained_variance = pca.explained_variance_ratio_

print("Explained Variance Ratio:", explained_variance)
print("Total Variance Explained:", np.sum(explained_variance))



# Create DataFrame with PCA components
pca_df = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2"]
)

pca_df["Target"] = y.values



# Display first 10 rows
print("\nMerged PCA Data (first 10 rows):")
print(pca_df.head(10))



# Save PCA-transformed data
pca_df.to_csv("pca_transformed_data.csv", index=False)
print("\nPCA transformed data saved as 'pca_transformed_data.csv'.")



# Plot PCA results
plt.figure(figsize=(10, 6))



for target in y.unique():
    idx = y == target

    plt.scatter(
        X_pca[idx, 0],
        X_pca[idx, 1],
        label=target,
        alpha=0.6
    )



plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Projection (2D) of Dataset")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



"""
Output:

Explained Variance Ratio: [0.17666395 0.0988699 ]
Total Variance Explained: 0.275533843404266

Merged PCA Data (first 10 rows):
        PC1       PC2    Target
0 -6.101294 -0.296791   Dropout
1 -0.254507 -1.106861  Graduate
2 -3.954380  0.446635   Dropout
3  0.421885 -0.958326  Graduate
4  0.405696  2.791055  Graduate
5  0.939409  4.967883  Graduate
6  1.374645 -2.000275  Graduate
7 -3.384482  1.493693   Dropout
8  0.301539 -2.251745  Graduate
9 -0.208504 -0.550056   Dropout

PCA transformed data saved as 'pca_transformed_data.csv'.
"""
