from flask import Flask, jsonify, request 

app = Flask(__name__) 

@app.route('/', methods=['GET']) 
def helloworld(): 
    name = request.args.get('name')  # Get 'name' from query parameters
    if name:
        data = {"message": f"Hello {name}"}
    else:
        data = {"message": "Hello World"}
    return jsonify(data)

if __name__ == '__main__': 
    app.run(debug=False)
