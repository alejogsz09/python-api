from flask import Flask, jsonify, abort, request

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    if not request.json or 'name' not in request.json:
        abort(400)  # Bad Request si no envía 'name'

    new_day = {
        "id": len(days) + 1,
        "name": request.json["name"]
    }

    days.append(new_day)
    return jsonify(new_day), 201


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hola desde el método GET"})


if __name__ == "__main__":
    app.run(debug=True)

