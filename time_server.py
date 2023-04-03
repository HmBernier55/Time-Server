from flask import Flask, request, jsonify
from datetime import datetime, date, time


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


def current_date_time():
    now = datetime.now()
    return now


@app.route("/time", methods=["GET"])
def time():
    current = current_date_time()
    current_time = current.strftime("%H:%M:%S")
    return current_time


@app.route("/date", methods=["GET"])
def date():
    current = current_date_time()
    current_date = current.strftime("%m/%d/%Y")
    return current_date


@app.route("/age", methods=["POST"])
def age():
    in_data = request.get_json()
    years = calc_age(in_data)
    return jsonify(years)


def calc_age(in_data):
    old_date = datetime.strptime(in_data["date"], '%m/%d/%Y').date()
    current_date = current_date_time()
    diff_date = (current_date.date() - old_date).days
    num_years = float(diff_date)/365
    return num_years


@app.route("/until_next_meal/<meal>", methods=["GET"])
def meal_calc(meal):
    current = current_date_time()
    if meal == "breakfast":
        breakfast = datetime(current.year, current.month, current.day, 8, 0, 0)
        until_meal = (current - breakfast).seconds
    elif meal == "lunch":
        lunch = datetime(current.year, current.month, current.day, 13, 0, 0)
        until_meal = (current - lunch).seconds
    else:
        dinner = datetime(current.year, current.month, current.day, 18, 0, 0)
        until_meal = (current - dinner).seconds
    num_hours = float(until_meal)/3600
    return jsonify(num_hours)


if __name__ == "__main__":
    app.run()
