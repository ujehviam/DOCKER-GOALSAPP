from flask import Flask, request, jsonify, send_from_directory
from database import init_db, get_goals, add_goal, delete_goal
import os

app = Flask(__name__)

# ----------- Serve Frontend -----------
@app.route("/")
def home():
    return send_from_directory("../Frontend", "index.html")

@app.route("/<path:filename>")
def Frontend_files(filename):
    return send_from_directory("../Frontend", filename)

# ----------- API Endpoints -----------
@app.route("/api/goals", methods=["GET"])
def api_get_goals():
    return jsonify(get_goals())

@app.route("/api/goals", methods=["POST"])
def api_add_goal():
    data = request.json
    goal_text = data.get("goal")
    if goal_text:
        add_goal(goal_text)
        return jsonify({"message": "Goal added!"}), 201
    return jsonify({"error": "Goal text required"}), 400

@app.route("/api/goals/<int:goal_id>", methods=["DELETE"])
def api_delete_goal(goal_id):
    delete_goal(goal_id)
    return jsonify({"message": f"Goal {goal_id} deleted!"})

# ----------- Run -----------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)