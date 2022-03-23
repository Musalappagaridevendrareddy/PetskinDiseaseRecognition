from flask import Flask, render_template, request
from model_dog import image_recog_dog
from model_cat import image_recog_cat
from model_rabbit import image_recog_rabbit

app = Flask(__name__)


@app.route('/cat', methods=['GET', 'POST'])
def cat():
	if request.method == 'POST':
		if request.files['file']:
			f = request.files['file']
			f.save(f'./data/cat/{f.filename}')
			cat_data = image_recog_cat(f'./data/cat/{f.filename}')
			print({'cat_data': cat_data})
			return render_template("success.html", name=f.filename, data={'cat_data': cat_data})
	return render_template('cat.html')


@app.route('/dog', methods=['GET', 'POST'])
def dog():
	if request.method == 'POST':
		if request.files['file']:
			f = request.files['file']
			f.save(f'./data/dog/{f.filename}')
			dog_data = image_recog_cat(f'./data/cat/{f.filename}')
			print({'dog_data': dog_data})
			return render_template("success.html", name=f.filename, data={'dog_data': dog_data})
	return render_template('dog.html')


@app.route('/rabbit', methods=['GET', 'POST'])
def rabbit():
	if request.method == 'POST':
		if request.files['file']:
			f = request.files['file']
			f.save(f'./data/rabbit/{f.filename}')
			rabbit_data = image_recog_cat(f'./data/cat/{f.filename}')
			print({'rabbit_data':rabbit_data})
			return render_template("success.html", name=f.filename, data={'rabbit_data':rabbit_data})
	return render_template('rabbit.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	return render_template('upload.html')


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)
