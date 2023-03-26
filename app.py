from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS



messages = []

app = Flask(__name__)
CORS(app) # Comment out

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route("/summary", methods=['GET', 'POST'])
def incoming_sms():
    if 'Body' in request.form:
        message = request.form['Body']
        response = MessagingResponse()
        response.message(f"You said: {message}")
        messages.append(message)
        return Response(str(response), mimetype='text/xml')
    else:
        return f"Text me!\nMessages:\n{messages}"


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)