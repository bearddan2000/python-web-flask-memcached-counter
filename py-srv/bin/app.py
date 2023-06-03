from flask import Flask, render_template
from pymemcache.client import base
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def main(value: int=0):
    byte_val = value.to_bytes(2, 'little')
    key = "123-456-789"
    writer = base.Client(('redis', 11211))
    writer.set(key, byte_val)

def increment() -> int:
    db = base.Client(('redis', 11211))
    key = "123-456-789"
    byte_val = db.get(key)
    value = int.from_bytes(byte_val, 'little')
    value += 1
    main(value)
    return value


@app.route("/")
def hello():
    title = 'Python Flask Memcached MVC Example'
    visits = increment()
    return render_template("index.html", title=title, visits=visits)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)
