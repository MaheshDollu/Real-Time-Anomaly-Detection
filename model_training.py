import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle
import numpy as np
import os

# 📂 Ensure model directory exists
if not os.path.exists('model'):
    os.makedirs('model')

# 📊 Simulate historical transaction data (1000 records)
data = {
    'amount': np.random.uniform(10, 5000, 1000),  # Random amounts between 10 and 5000
}

df = pd.DataFrame(data)

# 🧠 Train Isolation Forest model
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(df[['amount']])

# 💾 Save model to a pickle file
with open('model/isolation_forest.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'model/isolation_forest.pkl'")
