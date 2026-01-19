from flask import Flask, render_template, request
from utils.receipt import generate_receipt
from utils.verify import verify_receipt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        bvn = request.form["bvn"]
        nin = request.form["nin"]
        amount = request.form["amount"]

        receipt = generate_receipt(
            name=name,
            bvn=bvn,
            nin=nin,
            amount=amount
        )

        is_valid, message = verify_receipt(receipt)

        return render_template(
            "receipt.html",
            receipt=receipt,
            valid=is_valid,
            message=message
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
