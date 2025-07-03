from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["github_events"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook received:", data)

    # Handle GitHub's ping test
    if "zen" in data:
        return jsonify({"message": "Ping received"}), 200

    # Handle push event
    if "commits" in data:
        author = data.get("pusher", {}).get("name")
        to_branch = data.get("ref", "").split("/")[-1]

        payload = {
            "author": author,
            "from_branch": None,
            "to_branch": to_branch,
            "timestamp": datetime.utcnow(),
            "action_type": "push"
        }
        collection.insert_one(payload)
        return jsonify({"message": "Push stored"}), 200

    # Handle pull request event
    if "pull_request" in data:
        pr = data["pull_request"]
        author = pr["user"]["login"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]

        payload = {
            "author": author,
            "from_branch": from_branch,
            "to_branch": to_branch,
            "timestamp": datetime.utcnow(),
            "action_type": "pull_request"
        }
        collection.insert_one(payload)
        return jsonify({"message": "PR stored"}), 200

    return jsonify({"message": "Unhandled event"}), 200

@app.route("/api/events", methods=["GET"])
def get_events():
    events = list(collection.find().sort("timestamp", -1))
    for event in events:
        event["_id"] = str(event["_id"])
    return jsonify(events)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)