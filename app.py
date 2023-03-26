from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

messages = []

app = Flask(__name__)

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