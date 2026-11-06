from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database" of events
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]


@app.after_request
def add_cors_headers(response):
    """Allow the front end (served from a different origin) to call this API."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/", methods=["GET"])
def welcome():
    """Homepage route: returns a JSON welcome message."""
    return jsonify({"message": "Welcome!"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    """Returns all events as a JSON array."""
    return jsonify(events), 200


@app.route("/events", methods=["POST"])
def add_event():
    """Accepts JSON with a 'title', stores the new event, and returns it with 201."""
    data = request.get_json(silent=True)

    # Input validation: title is required
    if not data or not str(data.get("title", "")).strip():
        return jsonify({"error": "Missing 'title' in request body"}), 400

    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"].strip()}
    events.append(new_event)
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)