from flask import Flask, render_template, url_for, request, redirect
from caption import *
from gtts import gTTS
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)

		path2 = "./static/{}".format(img.filename)+".mp3"

		caption = caption_this_image("static/"+img.filename)

		output = gTTS(text = caption, lang = 'en', slow = False)
		output.save(path2)

		
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption,
			'sound':path2
		}
	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)