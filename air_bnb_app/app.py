from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/overview")
def overview():
    return render_template('overview.html')

@app.route("/data")
def data():
    return render_template('data.html')

@app.route("/pre_processing")
def pre_processing():
    return render_template('pre_processing.html')

@app.route("/machine_learning")
def machine_learning():
    return render_template('machine_learning.html')

@app.route("/linear_regression")
def linear_regression():
    return render_template('linear_regression.html')

@app.route("/trees")
def trees():
    return render_template('trees.html')

@app.route("/knn")
def knn():
    return render_template('knn.html')

@app.route("/gradient_boost")
def gradient_boost():
    return render_template('gradient_boost.html')

@app.route("/acknowledgement")
def acknowledgement():
    return render_template('acknowledgement.html')

@app.route("/summary")
def summary():
    return render_template('summary.html')

@app.route("/collaborators")
def collaborators():
    return render_template('collaborators.html')

if __name__ == "__main__":
    app.run(debug=True)
