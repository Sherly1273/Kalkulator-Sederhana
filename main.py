from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("input", "")

        if request.form.get("submit") == "=":
            try:
                hasil = eval(user_input)
            except:
                hasil = "Error"

    return render_template("index.html", hasil=hasil, input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
