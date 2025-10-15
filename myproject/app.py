# Example route returning structured JSON data
@app.route("/api/data")
def get_data():
    return jsonify({
        "status": "ok",
        "message": "Package test successful",
        "data": [1, 2, 3, 4, 5]
    })