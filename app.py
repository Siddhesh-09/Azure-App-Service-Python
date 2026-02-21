from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Example data you might fetch from a database or API
    user_data = {
        "title": "Dashboard",
        "status": "Online",
        "features": ["Fast Performance", "Python 3.14 Ready", "Clean UI"]
    }
    return render_template("index.html", data=user_data)

if __name__ == "__main__":
    app.run(debug=True)