from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# sample data
tasks: list = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build an API", "done": False},
]


@app.route("/")
def hello() -> str:
    return "Hello World!"


@app.route("/api/tasks", methods=["GET"])
def get_tasks() -> Response:
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def add_task():
    new_task = request.json
    tasks.append(new_task)
    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(debug=True)
