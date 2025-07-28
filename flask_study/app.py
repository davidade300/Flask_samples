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
    return (jsonify(new_task), 201)


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task:
        task.update(request.json)
        return jsonify(task)

    return (jsonify({"error": "Task not found"}), 404)


# captures an integer from the url and passes it to the function
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    return f"User Id: {user_id}"


if __name__ == "__main__":
    app.run(debug=True)
