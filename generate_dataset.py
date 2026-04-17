import pandas as pd
import numpy as np

rows = 1000

data = {
    "file_size": np.random.randint(100, 1000, rows),
    "entropy": np.random.uniform(4, 8, rows),
    "cpu_usage": np.random.randint(10, 100, rows),
    "file_changes": np.random.randint(1, 300, rows),
    "network_activity": np.random.randint(1, 200, rows),
}

df = pd.DataFrame(data)


df["label"] = ((df["entropy"] > 7) & (df["cpu_usage"] > 70) & (df["file_changes"] > 100)).astype(int)

df.to_csv("dataset.csv", index=False)

print("✅ Dataset Generated")
