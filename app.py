from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/process#hero")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST", "GET"])
def process():
    # Get the input values from the form
    duration = float(request.form.get("duration"))
    diabetes = int(request.form.get("diabetes"))
    obesity = int(request.form.get("obesity"))
    pcv = float(request.form.get("pcv"))
    count = float(request.form.get("count"))
    bilirubin = float(request.form.get("bilirubin"))
    direct = float(request.form.get("direct"))
    phosphatase = float(request.form.get("phosphatase"))
    sgot = float(request.form.get("sgot"))
    sgpt = float(request.form.get("sgpt"))
    usg = int(request.form.get("usg"))
    highbp = float(request.form.get("highbp"))

    # Perform predictions using the loaded model
    input_data = [
        [
            duration,
            diabetes,
            obesity,
            pcv,
            count,
            bilirubin,
            direct,
            phosphatase,
            sgot,
            sgpt,
            usg,
            highbp,
        ]
    ]
    prediction = model.predict(scaler.fit_transform(input_data))

    # Return the prediction result to the user
    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
