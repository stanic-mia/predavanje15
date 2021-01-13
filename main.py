from flask import Flask, render_template


app = Flask(__name__)

# kontroler za početnu stranicu
@app.route("/")
def index():
    return render_template("index.html")

# kontroler za kontakt
@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run()
