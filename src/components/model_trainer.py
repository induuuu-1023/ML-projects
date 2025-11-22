import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Load data
df = pd.read_csv("notebook/data/StudentsPerformance.csv")

# Features and target
X = df.drop("math score", axis=1)
y = df["math score"]

# Columns
categorical_cols = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]
numerical_cols = ["reading score", "writing score"]

# Preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(drop='first'), categorical_cols),
    ("num", StandardScaler(), numerical_cols)
])

# Full pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
pipeline.fit(X_train, y_train)

# Save pipeline
os.makedirs("artifacts", exist_ok=True)
joblib.dump(pipeline, "artifacts/pipeline.pkl")

print("Pipeline trained and saved at artifacts/pipeline.pkl")
