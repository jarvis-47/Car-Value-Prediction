from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

# Configure CORS to allow requests from localhost
CORS(app)


@app.route("/get_brand_names", methods=["GET"])
def get_brand_names():
    response = jsonify({"brands": util.get_brand_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/get_model_names", methods=["GET"])
def get_model_names():
    response = jsonify({"models": util.get_model_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/get_fuel_types", methods=["GET"])
def get_fuel_types():
    response = jsonify({"fuel_types": util.get_fuel_types()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_car_price", methods=["GET", "POST"])
def predict_car_price():
    dist = request.form["dist"]
    year = int(request.form["model_year"])
    fuel_type = request.form["fuel_type"]
    brand = request.form["brand"]
    model = request.form["model"]

    response = jsonify(
        {"estimated_car_price": util.predict_price(dist, year, fuel_type, brand, model)}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Car Value Prediction...")
    util.load_saved_artifacts()
    app.run()
