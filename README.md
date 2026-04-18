AI Ransomware Detection System

An intelligent machine learning-based system designed to detect ransomware activity by analyzing file behavior and system patterns in real-time.

---

 Overview

Ransomware is a major cybersecurity threat that encrypts user data and demands payment.
This project uses **machine learning and behavioral analysis** to identify suspicious activity such as:

* Rapid file modifications
* High entropy levels
* Abnormal CPU usage
* Unusual network activity

---

 Features

Machine Learning-based detection
 Real-time analysis of file behavior
 Flask-based web interface
 Lightweight and easy to run
User-friendly input system

---

##  Tech Stack

* **Python** 
* **Flask** 
* **Scikit-learn** 
* **Pandas & NumPy** 
* **HTML / CSS** 

---

##  Project Structure

```
RansomwareDetection/
│── app.py                # Flask web app
│── train_model.py        # Model training script
│── generate_dataset.py   # Dataset generator
│── realtime_monitor.py   # Monitoring script
│── requirements.txt      # Dependencies
│── templates/
│     └── index.html      # UI page
│── model.pkl             # Trained model
│── scaler.pkl            # Data scaler
│── dataset.csv           # Dataset
```

---

## How to Run

###  Install dependencies

```bash
pip install -r requirements.txt
```

### 2️ Train the model (optional)

```bash
python train_model.py
```

### 3️ Run the web app

```bash
python app.py
```

### 4️ Open in browser

```
http://127.0.0.1:5000
```



##  Demo

(Add screenshots here for better presentation)



##  Note

This project is for **educational purposes only** and demonstrates how machine learning can be applied in cybersecurity.


##  Future Improvements

* Real-time system monitoring integration
* Deep learning-based detection
* Cloud deployment
* API-based detection system



## developed by:

**Ashutosh Mishra**
📧 [13ashutoshmishra@gmail.com](mailto:13ashutoshmishra@gmail.com)
🔗 GitHub: https://github.com/Ashutosh-Mishra03

---

