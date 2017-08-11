import pedlbot
import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/")
def pedlbot():
    subprocess.call("pedlbot.py", shell=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)