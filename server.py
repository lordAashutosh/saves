from flask import Flask, jsonify ,request

app = Flask(__name__)
@app.route("/", methods=['GET'])
def get_messages():
    return jsonify(
        {"message": "hello world!"}
    )
@app.route("/user-details", methods=['GET'])

def get_user_details():
    return jsonify(
        {"details": "Eternklxz"})
 
from flask import Flask, jsonify ,request
app = Flask(__name__)

players = [
    {"name": "dipesh", "address": "bajhang",'minecraft_exprience':"noob"},
    {"name": "raunak", "address": "birgunj",'minecraft_exprience':"pro"},
    {"name": "jasoon", "address": "ktm",'minecraft_exprience':"mediaterian"},
    {"name": "aayush", "address": "lalitpur",'minecraft_exprience':"beginner"},
    {"name": "yogendra ", "address": "sailung",'minecraft_exprience':"noob"},
    {"name": "Abhigyan", "address": "dhading",'minecraft_exprience':"mediaterian"},
    {"name": "eternxlkz", "address": "sindupalchok",'minecraft_exprience':"expert"},
    
    
    
    
]
@app.route('/players', methods=['GET'])
def get_players():
    query = request.args.get('query')
    if not query:
        return jsonify(players)
    for player in players:
        if player['name'] == query.capitalize():
            return jsonify(player)
    return jsonify({'messeges':f'given user {query} not found'})

@app.route('/get-char-count', methods=['GET'])
def get_char_count():
    text = request.args.get('text')
    count = len(text)
    return jsonify({'count': count})

                                