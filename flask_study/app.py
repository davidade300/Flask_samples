from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


tasks: list = []


class Task(Resource):
    def get(self, task_id):
        task = next((task for task in tasks if task["id"] == task_id), None)

        if task is None:
            return ({"error": "Task not found"}, 404)

        return task

    def post(self):
        if not request.json or "title" not in request.json:
            return ({"error": "Task not found"}, 404)

        new_task = {
            "id": len(tasks) + 1,
            "title": request.json["title"],
            "done": False,
        }
        tasks.append(new_task)

        return (new_task, 201)

    def put(self, task_id):
        task = next((task for task in tasks if task["id"] == task_id), None)

        if task is None:
            return (
                {"error": "Not Found", "message": "Request must be JSON"},
                400,
            )

        if not request.json:
            return (
                {"error": "Bad request", "message": "Request must be JSON"},
                400,
            )

        task.update(request.json)
        return jsonify(task)

    def delete(self, task_id):
        global tasks  # using the global tasks variable

        tasks = [task for task in tasks if task["id"] != task_id]
        return ({"result": "Task deleted"}, 204)


api.add_resource(Task, "/api/tasks", "/api/tasks/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)
