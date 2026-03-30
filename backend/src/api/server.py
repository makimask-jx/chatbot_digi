from flask import Flask, render_template
from pathlib import Path

template_dir = Path(__file__).resolve().parent / "../../../frontend"
app = Flask(__name__, template_folder=str(template_dir))


@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
