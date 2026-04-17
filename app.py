from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model + scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        data = [
            float(request.form['file_size']),
            float(request.form['entropy']),
            float(request.form['cpu_usage']),
            float(request.form['file_changes']),
            float(request.form['network_activity'])
        ]

        sample = scaler.transform([data])
        prediction = model.predict(sample)[0]

        result = "Ransomware ⚠️" if prediction == 0 else "Safe ✅"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)