from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/overview")
def overview():
    return render_template('overview.html')

@app.route("/linear_regressions")
def linear_regressions():
    return render_template('linear_regressions.html')

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

@app.route("/conclusions")
def conclusions():
    return render_template('conclusions.html')

@app.route("/collaborators")
def collaborators():
    return render_template('collaborators.html')

if __name__ == "__main__":
    app.run(debug=True)
