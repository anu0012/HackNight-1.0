import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
# @app.route('/index')
# def index():
#     return flask.render_template('index.html')

@app.route('/',methods = ['POST','GET'])
def result():
	if request.method == 'POST':
		to_predict_list = request.form.to_dict()
		to_predict_list=list(to_predict_list.values())
		to_predict_list = list(map(int, to_predict_list))
		print (to_predict_list)
		result = ValuePredictor(to_predict_list)
		if int(result)==1:
			prediction='Yes, Leave can be given'
		else:
			prediction='No, model do not suggest to give leave'
		return render_template("result.html",prediction=prediction)
	else:
		return flask.render_template('index.html')

def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1,24)
	print (to_predict)
	loaded_model = pickle.load(open("model.pkl","rb"))
	result = loaded_model.predict(to_predict)
	return result[0]

if __name__ == '__main__':
	port = int(os.environ.get('PORT',9090))
	app.run(port=port, debug=True)