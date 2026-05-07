from flask import Flask, render_template, request

app = Flask(__name__)

# Mock database
REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    # Validation logic
    if not name or not sport:
        return render_template("failure.html")

    # Success logic
    REGISTRANTS[name] = sport
    return render_template("success.html")
