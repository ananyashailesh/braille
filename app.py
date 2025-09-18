from flask import Flask, request, jsonify, send_from_directory
import braille

import os
app = Flask(__name__)
@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'frontend.html')

@app.route('/api/text-to-braille', methods=['POST'])
def text_to_braille():
    data = request.get_json()
    text = data.get('text', '')
    result = braille.textToBraille(text)
    return jsonify({'result': result})

@app.route('/api/braille-to-text', methods=['POST'])
def braille_to_text():
    data = request.get_json()
    braille_str = data.get('braille', '')
    result = braille.brailleToText(braille_str)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
