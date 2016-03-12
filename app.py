import os
from flask import Flask
#from twython import TwythonStreamer

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
#     exec(open("keys.py").read())

# string = "Lula" # searchs this string in stream tweets
# nb = 0 # nb seen

# def found():
# 	global nb
# 	nb = nb+1
# 	if ( nb > 2 ):
# 		print("Harris is popular!")

# class TWStreamer(TwythonStreamer):

# 	def on_success(self, data):
# 		if 'text' in data:
# 			print("Found it.")
# 			found()
# 			print(data['text'].encode('utf-8'))

# 	def on_error(self, status_code, data):
# 		print(status_code)
# 		self.disconnect()

# try:
# 	stream = TWStreamer(C_K, C_S, A_T, A_S)
# 	stream.statuses.filter(track = string)
# except KeyboardInterrupt:
# 	exit()
    print "teste"
    return "Hello from Python!"

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



