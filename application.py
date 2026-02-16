from flask import Flask,jsonify,request
import os
app = Flask(__name__)
@app.route('/api/greet',methods=['GET'])
def greet():
    return jsonify({'message':'Hello from the Cloud Web Service!'})
@app.route('/api/sum',methods=['POST'])
def sum_values():
    data = request.json
    result = data['a']+data['b']
    return jsonify({'sum':result})
if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))  # Dynamic port for cloud
    app.run(host='0.0.0.0', port=port)
