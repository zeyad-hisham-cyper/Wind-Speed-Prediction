from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    data15 = request.form['o']
    data16 = request.form['p']
    data17 = request.form['q']

    data1 = float(data1)
    data2 = float(data2)
    data3 = float(data3)
    data4 = float(data4)
    data5 = float(data5)
    data6 = float(data6)
    data7 = float(data7)
    data8 = float(data8)
    data9 = float(data9)
    data10 = float(data10)
    data11 = float(data11)
    data12 = float(data12)
    data13 = float(data13)
    data14 = float(data14)
    data15 = float(data15)
    data16 = float(data16)
    data17 = float(data17)

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16,data17]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















