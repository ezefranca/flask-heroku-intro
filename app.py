import os
from flask import Flask
#from twython import TwythonStreamer

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route('/')
def hello():
    return flask.render_template('hello.html')
    #return "Hello from Python!"
#@app.route("/")
#def hello():
#    print "teste"
#    return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



