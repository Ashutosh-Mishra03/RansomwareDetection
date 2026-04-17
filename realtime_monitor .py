import time
import joblib
import numpy as np
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Simulated features
        sample = np.array([[500, 7.9, 85, 200, 150]])
        sample_scaled = scaler.transform(sample)

        prediction = model.predict(sample_scaled)

        if prediction[0] == 1:
            print("🚨 Ransomware Activity Detected!")
        else:
            print("✅ Normal Activity")

if __name__ == "__main__":
    path = "."
    observer = Observer()
    observer.schedule(MonitorHandler(), path, recursive=True)
    observer.start()

    print("👀 Monitoring started...")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
