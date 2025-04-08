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
    ist = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        top_output = f"Error getting top output: {str(e)}"

    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {ist}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
