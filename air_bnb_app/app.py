from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/overview")
def overview():
    return render_template('overview.html')

@app.route("/map")
def map():
    return render_template('map.html')

@app.route("/neighborhood")
def neighborhood():
    return render_template('neighborhood.html')

@app.route("/room_type")
def room_type():
    return render_template('room_type.html')

@app.route("/availability")
def availability():
    return render_template('availability.html')

@app.route("/price_predictor")
def price_predictor():
    return render_template('price_predictor.html')

@app.route("/summary")
def summary():
    return render_template('summary.html')

@app.route("/conclusions")
def conclusions():
    return render_template('conclusions.html')

@app.route("/collaborators")
def collaborators():
    return render_template('collaborators.html')

if __name__ == "__main__":
    app.run(debug=True)
