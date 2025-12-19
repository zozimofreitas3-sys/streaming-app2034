from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/drive-links')
def drive_links():
    return   send_from_directory('static','drive-links.html')


@app.route('/ia-orquestrador')
def  ia-orquestrador():
    return  send_from_directory('static','ia-orquestrador.html')


@app.route('/miniwriter')
def  miniwriter():
    return  send_from_directory('static','miniwriter.html')






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
