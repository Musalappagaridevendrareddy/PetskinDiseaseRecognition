from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.utils import redirect
from decode import decodeImage
from model_dog import image_recog_dog
from model_cat import image_recog_cat
from model_rabbit import image_recog_rabbit

app = Flask(__name__)


@app.route('/cat', methods=['GET', 'POST'])
def cat():
	if request.method == 'POST':
			f = request.files['file']
			f.save(f'./data/cat/{f.filename}')
			cat_data = image_recog_cat(f'./data/cat/{f.filename}')
			return redirect(url_for("success", filename=f.filename, data={'cat_data': cat_data}))
	return render_template('cat.html')


@app.route('/success/<filename>/<data>', methods=['GET', 'POST'])
def success(filename=None, data=None):
	if filename and data:
		return render_template('success.html', name=filename, data=data)
	return render_template('success.html')


@app.route('/dog', methods=['GET', 'POST'])
def dog():
	if request.method == 'POST':
		if request.files['file']:
			f = request.files['file']
			f.save(f'./data/dog/{f.filename}')
			dog_data = image_recog_dog(f'./data/cat/{f.filename}')
			return render_template("success.html", name=f.filename, data={'dog_data': dog_data})
	return render_template('dog.html')


@app.route('/rabbit', methods=['GET', 'POST'])
def rabbit():
	if request.method == 'POST':
			f = request.files['file']
			f.save(f'./data/rabbit/{f.filename}')
			rabbit_data = image_recog_rabbit(f'./data/cat/{f.filename}')
			return render_template("success.html", name=f.filename, data={'rabbit_data':rabbit_data})
	return render_template('rabbit.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == "POST":
		if request.form.get("cat"):
			return redirect(url_for('cat'))
		elif request.form.get('dog'):
			return redirect(url_for('dog'))
		elif request.form.get('rabbit'):
			return redirect(url_for('rabbit'))
	return render_template('upload.html')


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		if request.form.get("upload"):
			return redirect(url_for('upload'))
	return render_template('index.html')


@app.route('/cat/predict', methods=['POST'])
def catPredict():
	image = request.json['image']
	decodeImage(image)
	cat_data = image_recog_cat('data.jpg')
	return jsonify(cat_data)


@app.route('/dog/predict', methods=['POST'])
def dogPredict():
	image = request.json['image']
	decodeImage(image)
	dog_data = image_recog_dog('data.jpg')
	return jsonify(dog_data)


@app.route('/dog/predict', methods=['POST'])
def rabbitPredict():
	image = request.json['image']
	decodeImage(image)
	rabbit_data = image_recog_rabbit('data.jpg')
	return jsonify(rabbit_data)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
