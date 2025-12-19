import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score



# Load the dataset
df = pd.read_csv('Real estate.csv', delimiter=',')



# Select only numeric columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])



# Separate independent and dependent variables
X = numeric_df.drop(columns=['house price of unit area'])
y = numeric_df['house price of unit area']



# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Train the Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)



# Make predictions
y_pred = model.predict(X_test)



# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)



print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared Score (R²):", r2)



# Display regression equation
intercept = model.intercept_
coefficients = model.coef_

print("\nRegression Line Equation:")
print(f"y = {intercept:.4f}", end='')

for feature, coef in zip(X.columns, coefficients):
    sign = " + " if coef >= 0 else " - "
    print(f"{sign}{abs(coef):.4f}*({feature})", end='')

print("\n")



# Plot Actual vs Predicted values
plt.figure(figsize=(7, 5))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.7,
    edgecolor='k'
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linewidth=2
)

plt.title('Actual vs Predicted House Price')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.grid(True)
plt.show()



# Plot regression line using one feature (example: first feature)
feature_to_plot = X.columns[0]

plt.figure(figsize=(7, 5))

plt.scatter(
    X_test[feature_to_plot],
    y_test,
    label='Actual',
    alpha=0.6
)

y_feature_pred = model.predict(X_test)

plt.scatter(
    X_test[feature_to_plot],
    y_feature_pred,
    label='Predicted',
    alpha=0.6
)

plt.title(f'Regression Line using Feature: {feature_to_plot}')
plt.xlabel(feature_to_plot)
plt.ylabel('House Price of Unit Area')
plt.legend()
plt.grid(True)
plt.show()



"""
Output:

Mean Squared Error (MSE): 55.42976176163538
Mean Absolute Error (MAE): 5.385270702159246
R-squared Score (R²): 0.6695884228951919

Regression Line Equation:
y = -2783.3124 - 0.0058*(No) - 0.2675*(house age)
    - 0.0046*(distance to the nearest MRT station)
    + ... (remaining feature coefficients)
"""
