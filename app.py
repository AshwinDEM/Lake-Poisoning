from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lake data with center+radius format
lakes = {
    "lake1": {
        "name": "Lake Erie (Western Basin)",
        "center": [41.7, -82.8],  # [latitude, longitude]
        "radius": 15000,           # in meters
        "status": "poisoned"       # or "clean"
    },
    "lake2": {
        "name": "Lake Michigan (Near Chicago)",
        "center": [41.9, -87.6],
        "radius": 10000,
        "status": "clean"
    },
    "lake3": {
        
        "name": "Ulsoor Lake",
        "center": [12.981472, 77.619214],  # Decimal degrees
        "radius": 500,  # in meters (adjust as needed)
        "status": "clean"  # or "poisoned"
    }
}

@app.route('/')
def index():
    return render_template('index.html', api_key="AIzaSyAPXRkKFi88KTauhfbeMteYi4ZdxEm4wu4")

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

if __name__ == '__main__':
    app.run(debug=True)