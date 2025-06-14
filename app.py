from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample lake data (in a real app, you'd use a database)
lakes = {
    "lake1": {
        "name": "Lake Superior",
        "coordinates": [[47.0, -87.0], [47.5, -87.5], [48.0, -88.0]],
        "color": "#0000FF"  # Default blue
    },
    "lake2": {
        "name": "Lake Michigan",
        "coordinates": [[43.0, -87.0], [43.5, -87.5], [44.0, -88.0]],
        "color": "#0000FF"
    }
}

@app.route('/')
def index():
    # Pass the Google Maps API key (you'll need to get your own)
    return render_template('index.html', api_key="AIzaSyAPXRkKFi88KTauhfbeMteYi4ZdxEm4wu4")

@app.route('/get_lakes', methods=['GET'])
def get_lakes():
    return jsonify(lakes)

@app.route('/update_lake_color', methods=['POST'])
def update_lake_color():
    data = request.json
    lake_id = data.get('lake_id')
    color = data.get('color')
    
    if lake_id in lakes:
        lakes[lake_id]['color'] = color
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Lake not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)