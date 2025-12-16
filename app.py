from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/drive-links')
def drive_links():
    return render_template('drive-links.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
