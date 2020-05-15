from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/cv', methods=["GET", "POST"])
def cv():
    if request.method == "POST":
        return send_file("Resume.pdf", attachment_filename="Caitlyn_Resume.pdf", as_attachment=True)
    else:
        return render_template("cv.html")   

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1')
