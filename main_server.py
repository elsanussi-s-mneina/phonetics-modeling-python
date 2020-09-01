"""
This module allows certain functionality of the program to be used
over the internet or a local area network.

It sets up a server over HTTP locally.

The API follows REST conventions.
"""

from flask import Flask, jsonify, render_template
# Flask is a third-party framework we use to be able
# to handle HTTP requests conveniently.

from english_us_text import BEFORE_SERVER_START_MESSAGE
from ipa import voiced_transcription, devoiced_transcription

app = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template("index.html")

@app.route("/voice_phoneme_j/<phoneme>", methods=["GET"])
def voice_phoneme_javascript(phoneme: str) -> str:
    """
    Given a phoneme in IPA, returns the
    voiced version of that phoneme in IPA.

    Wrapped in a route, and it sends JSON value
    when server is running.
    """
    return jsonify(voiced_transcription(phoneme))


@app.route("/voice_phoneme/<phoneme>", methods=["GET"])
def voice_phoneme_text(phoneme: str) -> str:
    """
    Given a phoneme in IPA, returns the
    voiced version of that phoneme in IPA.

    Wrapped in a route, and it sends a text value
    when server is running.
    """
    return voiced_transcription(phoneme)


@app.route("/devoice_phoneme/<phoneme>", methods=["GET"])
def devoice_phoneme_text(phoneme: str) -> str:
    """
    Given a phoneme in IPA, returns the
    voiceless version of that phoneme in IPA.

    Wrapped in a route, and it sends a text value
    when server is running.
    """
    return devoiced_transcription(phoneme)


def start_server():
    """
    Start being able to accept requests via HTTP.

    :return: None
    """
    print(BEFORE_SERVER_START_MESSAGE)
    # app.run(host="0.0.0.0", port=8080)
    app.run(port=8080)

if __name__ == "__main__":
    start_server()
