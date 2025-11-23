from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict_datapoint():
    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race/ethnicity'),
            parental_level_of_education=request.form.get('parental level of education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test preparation course'),
            reading_score=float(request.form.get('reading score')),
            writing_score=float(request.form.get('writing score'))
        )

        pred_df = data.get_data_as_data_frame()
        pipeline = PredictPipeline()
        results = pipeline.predict(pred_df)

        return render_template("home.html", results=round(results[0], 2))

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')