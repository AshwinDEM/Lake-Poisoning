# 🧪 Toxic Lake Monitor 🌊

A real-time web application for monitoring and classifying the toxicity of lakes using sensor data and a machine learning model. The system uses a Google Maps interface to display lake locations and their status (poisoned or clean), powered by a Flask backend.

---

## 📦 Features

- 🌍 Interactive map with lake markers and status colors.
- ⚙️ Flask backend serving lake data and status updates.
- 🧠 Machine learning model (commented) for classifying lake water quality.
- 📈 Real-time simulation: status of lakes can be randomized every second.
- 🧪 (Optional) Serial sensor input via Arduino for live monitoring.

---

## 🗂️ Project Structure
```
.
├── app.py # Main Flask server
├── templates/
│ └── index.html # Google Maps + UI
├── models/
│ ├── color_tag_model.pkl # Trained ML model (optional)
│ └── label_encoder.pkl # Label encoder for classes
├── data/
│ └── lakes.csv # Initial lake data
├── .env # Contains GOOGLE_CLOUD_API=your_api_key
├── requirements.txt # Python dependencies
└── README.md # You're reading it!
```

---

## 🚀 How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Setup environment**

Create a `.env` file:

```
GOOGLE_CLOUD_API=your_google_maps_api_key
```

3. **Run the app**

```bash
python app.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 API Endpoints

- `GET /get_lakes` — returns JSON of all lakes
- `POST /update_lake_status` — updates status of a lake

```json
{
  "lake_id": 0,
  "status": "clean"
}
```

---

## 🧠 Built With

- Python (Flask, pandas, requests)
- HTML/CSS/JavaScript
- Google Maps API
- Joblib + Scikit-learn

---

## 📌 License

MIT License

---
