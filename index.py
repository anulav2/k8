from flask import Flask
#from logging.config import fileConfig
import logging
app = Flask(__name__)
#fileConfig('logging.cfg')
#logging.basicConfig(filename='demo.log', level=logging.DEBUG)
logging.basicConfig(filename='demo.log',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
@app.route("/")
def hello():
    #app.logger.info('Processing default request')
    return "Hello World"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("7777"), debug=True)
