import os
from flask import Flask, render_template, request, jsonify
import serial
import pandas as pd
import threading
import joblib
from dotenv import load_dotenv
import time
import random
import requests

app = Flask(__name__)
load_dotenv()

api_key = os.getenv("GOOGLE_CLOUD_API")

# --- Model and Serial Setup ---
# ser = serial.Serial('COM5', 9600)
# columns = ["temperature", "pH", "Norm_R", "Norm_G", "Norm_B", "turbidity"]
# latest_data = pd.DataFrame(columns=columns)
# model = joblib.load("color_tag_model.pkl")
# le = joblib.load("label_encoder.pkl")

# --- Lake Status Setup ---
def load_lakes_from_csv(path="lakes.csv"):
    df = pd.read_csv(path)
    lakes = {}
    for _, row in df.iterrows():
        lakes[row["id"]] = {
            "name": row["name"],
            "center": [row["latitude"], row["longitude"]],
            "radius": row["radius"],
            "status": row["status"]
        }
    return lakes

lakes = load_lakes_from_csv()

# # --- Prediction Function ---
# def predict(df):
#     X = df[["Norm_R", "Norm_G", "Norm_B"]]
#     y_pred = model.predict(X)
#     predicted_tags = le.inverse_transform(y_pred)
#     return predicted_tags

# # --- Serial Reading in Background ---
# def read_serial():
#     global latest_data, lakes
#     MAX_VALUE = 32678
#     while True:
#         if ser.in_waiting:
#             try:
#                 line = ser.readline().decode('utf-8').strip()
#                 values = line.split(',')

#                 if len(values) == 6:
#                     data = [
#                         float(values[0]), float(values[1]),
#                         int(values[2]),
#                         int(values[3]),
#                         int(values[4]),
#                         int(values[5])
#                     ]
#                     latest_data = pd.DataFrame([data], columns=columns)
#                     print("Latest sensor data:", latest_data)

#                     # Predict and update lake status if necessary
#                     prediction = predict(latest_data)[0]
#                     # print(prediction)
                    
#                     # if "medium" in prediction.lower():
#                     #     prediction = "High"
#                     # elif "control" in prediction.lower():
#                     #     prediction = "Medium"

#                     if data[2] > 200:
#                         prediction = "Low"
#                         print(prediction)
#                         lakes[0]["status"] = "clean"
#                         print("Lake marked as clean")
#                         lakes.to_csv("lakes.csv")
#                     else:
#                         prediction = "High"
#                         print(prediction)
#                         lakes[0]["status"] = "poisoned"
#                         print("Lake marked as poisoned")
#                         lakes.to_csv("lakes.csv")
#                     print(prediction)                    

#             except Exception as e:
#                 print("Serial Read Error:", e)

# # Start background thread
# threading.Thread(target=read_serial, daemon=True).start()

# --- Flask Routes ---
@app.route('/')
def index():
    return render_template('index.html', api_key=api_key)

@app.route('/get_lakes', methods=['GET'])
def get_lakes():
    return jsonify(lakes)

@app.route('/update_lake_status', methods=['POST'])
def update_lake_status():
    data = request.json
    lake_id = data.get('lake_id')
    status = data.get('status')
    
    if lake_id in lakes and status in ['poisoned', 'clean']:
        lakes[lake_id]['status'] = status
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Invalid request"}), 400

def randomize_lake_status():
    while True:
        time.sleep(1)
        for lake_id in lakes:
            new_status = random.choice(['poisoned', 'clean'])
            try:
                requests.post("http://127.0.0.1:5000/update_lake_status", json={
                    "lake_id": lake_id,
                    "status": new_status
                })
            except Exception as e:
                print(f"Failed to update status for {lake_id}: {e}")



if __name__ == '__main__':
    # threading.Thread(target=randomize_lake_status, daemon=True).start()
    app.run(debug=True, use_reloader=False)
