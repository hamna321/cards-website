from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    input_text = request.form['input-text']
    response = requests.post('https://api.openai.com/v1/images/generations', headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }, json={
        'model': 'image-alpha-001',
        'prompt': input_text,
        'size': '1024x1024',
        'response_format': 'url'
    })
    data = response.json()
    return jsonify({'image_url': data['data'][0]['url']})

if __name__ == '__main__':
    app.run()
