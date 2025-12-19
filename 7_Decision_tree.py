import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns



# Load the dataset
df = pd.read_csv('loan_approval.csv', delimiter=',')



# Convert boolean target variable to string
df['loan_approved'] = df['loan_approved'].astype(str)



# Encode the target variable
label_encoder = LabelEncoder()
df['loan_approved'] = label_encoder.fit_transform(df['loan_approved'])



# Separate features and target
X = df.drop(columns=['loan_approved', 'name', 'city'])
y = df['loan_approved']



# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Train the Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)



# Make predictions
y_pred = clf.predict(X_test)



# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(
    y_test,
    y_pred,
    target_names=label_encoder.classes_
)



# Print evaluation results
print("Accuracy:", accuracy)
print("\nClassification Report:\n", class_report)



# Visualize the Decision Tree (top 3 levels)
plt.figure(figsize=(20, 10))

plot_tree(
    clf,
    feature_names=X.columns,
    class_names=label_encoder.classes_,
    filled=True,
    max_depth=3
)

plt.title("Decision Tree Visualization (Top 3 Levels)")
plt.show()



# Plot the Confusion Matrix
plt.figure(figsize=(6, 5))

sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=label_encoder.classes_,
    yticklabels=label_encoder.classes_
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()



"""
Output:

Accuracy: 1.0

Classification Report:
              precision    recall  f1-score   support

       False       1.00      1.00      1.00       217
        True       1.00      1.00      1.00       183

    accuracy                           1.00       400
   macro avg       1.00      1.00      1.00       400
weighted avg       1.00      1.00      1.00       400
"""
