from flask import Flask, render_template, request, jsonify
from your_python_file import readPatientsFromFile, displayStats

app = Flask(__name__)

DATA_FILE = "patients.txt"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats", methods=["POST"])
def stats():
    patient_id = int(request.json["patientId"])
    patients = readPatientsFromFile(DATA_FILE)

    # Example: calculate average temperature only
    temps = []
    if patient_id == 0:
        for visits in patients.values():
            for v in visits:
                temps.append(v[1])
    else:
        for v in patients.get(patient_id, []):
            temps.append(v[1])

    if not temps:
        return jsonify({"result": "No data found"})

    avg_temp = sum(temps) / len(temps)
    return jsonify({"result": f"Average Temperature: {avg_temp:.2f} °C"})

if __name__ == "__main__":
    app.run(debug=True)
