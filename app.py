from flask import Flask, render_template, request
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('score_predictor_1.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_score = None
    if request.method == 'POST':
        hours = float(request.form['hours'])
        attendance = float(request.form['attendance'])
        predicted_score = model.predict([[hours, attendance]])[0]

        # Plotting
        plt.figure()
        plt.bar(['Predicted Score'], [predicted_score], color='blue')
        plt.ylim(0, 100)
        plt.savefig('static/graph.png')
        plt.close()

    return render_template('index.html', score=predicted_score)

if __name__ == '__main__':
    app.run(debug=True)
