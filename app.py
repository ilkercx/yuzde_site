from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    result_color = "black"
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            y = float(request.form["y"])
            z = float(request.form["z"])
            operation = request.form["operation"]
            leverage = request.form.get("leverage")
            leverage = float(leverage) if leverage else 1

            a = x * (y / 100)
            b = a * (1 + (z / 100))
            fark = (b - a) * leverage

            if operation == "increase":
                result = x + fark
                result_color = "green"
            elif operation == "decrease":
                result = x - fark
                result_color = "red"
            else:
                result = "Gecersiz islem!"
                result_color = "black"

        except Exception as e:
            result = f"Hata: {e}"
            result_color = "black"

    return render_template("index.html", result=result, result_color=result_color)

if __name__ == "__main__":
    app.run(debug=True)
