from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']

    # Send the user's message to your Rasa chatbot (replace with your Rasa server URL)
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
    rasa_response = requests.post(rasa_url, json={'message': user_message})

    # Get the chatbot's response
    if rasa_response.status_code == 200:
        bot_response = rasa_response.json()[0]['text']
    else:
        bot_response = "Sorry, something went wrong with the chatbot."

    return jsonify(bot_response)

