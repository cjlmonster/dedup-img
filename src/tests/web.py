import os
from flask import Flask, render_template, jsonify
import json

root = r'e:/Pictures'

app = Flask(__name__, static_folder=root, static_url_path='/static')


@app.get('/')
def home():
    return render_template('index.html', alg='PHash')


@app.get('/filter')
def get_filter():
    filter_json = os.path.join(root, 'filter.json')
    with open(filter_json, 'r', encoding='utf-8') as f:
        result = json.load(f)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
