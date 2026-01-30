from flask import Flask, jsonify, request, abort

app = Flask(__name__)

items =[{"id":1, "item_name":"laptop", "description":"Dell laptop"}]

@app.route("/items", methods=["GET"])
def get_items():
    return items

@app.route("/items/<id>", methods=["GET"])
def get_item(id):

    for item in items:
        if item["id"] == int(id):
            return item

    return abort(404)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5555, debug=True)

