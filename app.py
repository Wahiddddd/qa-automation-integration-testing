from flask import Flask, request, jsonify

from db.database import get_connection

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    required_fields = ["username", "email", "role"]

    #validation if field empty
    if not data or any(
        field not in data or not data[field]
        for field in required_fields
    ):
        return jsonify({
            "message": "username, email, dan role harus diisi"
        }), 400

    username = data["username"]
    email = data["email"]
    role = data["role"]

    # Validasi tipe data
    if not isinstance(username, str) or not isinstance(email, str) or not isinstance(role, str):
        return jsonify({
            "message": "username, email, dan role harus berupa string"
        }), 400

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO users (username, email, role)
            VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (username, email, role)
        )

        connection.commit()

        user_id = cursor.lastrowid

        return jsonify({
            "id": user_id,
            "username": username,
            "email": email,
            "role": role
        }), 201

    finally:
        cursor.close()
        connection.close()

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        
        # Check if user exists first (optional, but good practice for 404)
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        if not cursor.fetchone():
            return jsonify({"error": "User not found"}), 404
            
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        
        return jsonify({"message": "User deleted successfully"}), 200
        
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(debug=True)