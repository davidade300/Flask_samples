from flask import Blueprint, jsonify, request

blog_bp = Blueprint("blog", __name__)

posts: list = [
    {"id": 1, "title": "First Post", "content": "This is my first post"},
    {"id": 2, "title": "Second Post", "content": "This is my second post"},
]


# Route to get all posts


@blog_bp.route("/posts", methods=["POST"])
def create_post():
    new_post = request.get_json()
    posts.append(new_post)
    return (jsonify(new_post), 201)


# route to a specific post
@blog_bp.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)

    if post is None:
        return (jsonify({"error": "Post not found"}), 404)

    return jsonify(post)
