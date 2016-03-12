import os
from flask import Flask

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/<name>")
def hello(name):
    return flask.render_template('hello.html', name=name)
    #return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
#    return flask.render_template('hello.html')



