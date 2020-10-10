from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/irigasi')
def irigasi():
	return render_template('irigasi.html')

@app.route('/details')
def details():
	return render_template('details.html')

@app.route('/prediksi cuaca')
def prediksi_cuaca():
	return render_template('prediksi_cuaca.html')

if __name__ == '__main__':
	app.run(debug=True)