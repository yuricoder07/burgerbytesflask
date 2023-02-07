import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        with open('users.json', 'a') as f:
            f.write(json.dumps({'title': title, 'ingredients': ingredients, 'instructions': instructions}))

if __name__ == '__main__':
    app.run(debug=True)
