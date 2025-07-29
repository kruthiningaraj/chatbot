from flask import Flask, render_template, request, jsonify, send_file
from src.chatbot_response import get_response
from src.certificate_generator import generate_certificate

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    response = get_response(msg)
    return jsonify({"response": response})

@app.route("/certificate", methods=["POST"])
def certificate():
    name = request.form["name"]
    email = request.form["email"]
    file = generate_certificate(name, email)
    return send_file(file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
