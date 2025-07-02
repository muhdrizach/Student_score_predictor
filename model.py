# Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# # Load dataset 1
# df = pd.read_csv('sp.csv')  # use your filename

# Load dataset 2
df = pd.read_csv('examscore.csv')  # use your filename

# # Features and target dataset 1
# X = df[['Hours_Studied', 'Attendance']]
# y = df['Exam_Score']

# Features and target dataset 2
X = df[['StudyHours', 'Attendance']]
y = df['Score']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# # Save model dataset 1
# joblib.dump(model, 'score_predictor.pkl')

# Save model dataset 2
joblib.dump(model, 'score_predictor_1.pkl')

from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)


from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)
