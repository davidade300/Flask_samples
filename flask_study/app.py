from blog.routes import blog_bp
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "your_secret_key"

jwt = JWTManager(app)

users = {}


@app.route("/register", methods=["POST"])  # type: ignore
def register():
    username = request.json.get("username")  # type: ignore
    password = request.json.get("password")  # type: ignore

    if username in users:
        return (jsonify({"msg": "user alreayd exists!"}), 400)

    users[username] = password  # real app = hashed passwords

    return (jsonify({"msg": "User registered successfully!"}), 201)


@app.route("/login", methods=["POST"])  # type: ignore
def login():
    username = request.json.get("username")  # type: ignore
    password = request.json.get("password")  # type: ignore

    if username not in users or users[username] != password:
        return (jsonify({"msg": "Bad username or password!"}), 401)

    access_token = create_access_token(identity=username)

    return (jsonify(access_token=access_token), 200)


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return (jsonify(msg="This is a protected route!"), 200)


# Register the blueprint with a URL prefix
app.register_blueprint(blog_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
