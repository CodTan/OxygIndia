'''
app.py
'''
import itertools
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return 'Here we are!'

if __name__ == "__main__":
    app.run(debug=True)