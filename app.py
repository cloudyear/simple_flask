from flask import Flask, redirect, url_for, Response, request, session, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return Response("hello")


if __name__ == "__main__":
    app.run(port=5001)
