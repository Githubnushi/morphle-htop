from flask import Flask
import getpass
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Nushitha Reddy"
    username = getpass.getuser()
    ist = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')

    try:
        top_output = subprocess.getoutput("top -b -n 1") 
    except Exception as e:
        top_output = f"Error getting top output: {str(e)}"

    return f"""
    <html>
    <head>
        <title>HTOP Viewer</title>
        <style>
            body {{
                color: #fff; 
                color: #000;
                font-family: monospace;
                padding: 20px;
            }}
            pre {{
                overflow-x: auto;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <h2>Name: {name}</h2>
        <h2>user: {username}</h2>
        <h2>Server Time (IST): {ist}</h2>
        <h3>TOP output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
