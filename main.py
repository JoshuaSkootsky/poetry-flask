from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/joshua")
def joshua():
    return "Hello there, Joshua..."
    
if __name__ == "__main__":
    app.run(debug=True)
