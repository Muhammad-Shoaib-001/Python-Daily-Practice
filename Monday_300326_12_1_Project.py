from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Stackness is live"

@app.route('/about')
def about():
    return "This is about section"

@app.route('/feature')
def feature():
    return "This is Feature section"

@app.route('/footer')
def footer():
    return "This is Feature section"

@app.route('/status')
def status():
   return jsonify({"status":"Running","tool":"Stackness"})

if __name__ == '__main__':
    app.run(debug=True)
