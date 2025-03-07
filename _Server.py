from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 1: Home Route
@app.route('/')
def home():
    return jsonify(message="Welcome to the API!")

# Route 2: Echo Route
@app.route('/echo/<string:text>', methods=['GET'])
def echo(text):
    return jsonify(echoed_text=text)

# Route 3: Character Count Route (takes 'name' as parameter)
@app.route('/count_characters', methods=['GET'])
def count_characters():
    name = request.args.get('name', '')
    if not name:
        return jsonify(error="No name provided"), 400
    char_count = len(name)
    return jsonify(name=name, character_count=char_count)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
