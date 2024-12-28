from flask import Flask, request, render_template
import requests

app = Flask(__name__)

api_key = "d03HKKIt.d4cV9hVzSX9LhnPfgpV31ppNeUewYrgM" # Your VEXT API Key

@app.route('/')
def home():
    return render_template('index.html')  # Assuming HTML file is in the templates folder

@app.route('/submit', methods=['POST'])
def submit():
    query = request.form['query']  # Get the query from the form
    headers = {
        'Content-Type': 'application/json',
        'Apikey': f'Api-Key {api_key}',
    }
    data = {"payload": query}
    url = 'https://payload.vextapp.com/hook/FUT7D4LJIH/catch/$(channel_token)'

    response = requests.post(url=url, json=data, headers=headers)
    return f'API Response: {response.text}'

if __name__ == '__main__':
    app.run(debug=True)
