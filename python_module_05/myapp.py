from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/index.html', methods = ['GET'])
def samplefunction():
    #access your DB get your results
    data = {"data":"Processed Data"}
    return jsonify(data)

if __name__ == '__main__':
    port = 8080                             # the custom port you want
    app.run(host='127.0.0.1', port=port)
