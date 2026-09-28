import pandas as pd
import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])
print("NumPy array:", numbers)

# Create a Pandas DataFrame
data = {
    "Name": ["Ritesh", "Ram", "Sita"],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print("\nStudent Data:")
print(df)