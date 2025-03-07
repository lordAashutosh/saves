import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Generate synthetic data
np.random.seed(42)
ages = np.random.randint(0, 20, 2001)  # Car ages between 0 to 20 years
prices = 50000 * np.exp(-0.15 * ages) + np.random.normal(0, 2000, 2001)  # Price decay with age

# Create a DataFrame
data = pd.DataFrame({'age': ages, 'price': prices})

# Train-Test Split
X = data[['age']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, 'car_price_model.pkl')

# Model Accuracy
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)
print(f"Model Accuracy (R^2 Score): {accuracy}")
print(y)
print(x)