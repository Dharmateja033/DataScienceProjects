import sys
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Testing Custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info('Testing Logging module')
    return "Pipeline established NOW!!"


if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)