from flask import Flask, jsonify, request
from numpy import matrix, round, array2string
from scipy import linalg

app = Flask(__name__)

@app.route("/", methods=['POST'])
def task():
	matrix1 = matrix(str(request.json['matrix1'])) 
	matrix2 = matrix(str(request.json['matrix2']))
	matrix1I = linalg.inv(matrix1)
	result = matrix1I * matrix2
	strResult = array2string(result, precision=4, separator=' ').replace('\n','').replace('[','').replace(']]','').replace(']',';').strip()
	return jsonify({'result' : strResult});

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)
