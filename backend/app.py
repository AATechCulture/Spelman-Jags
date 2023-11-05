from flask import Flask
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import datetime

ma = Marshmallow()
cors = CORS()

app = Flask(__name__)
ma.init_app(app)
cors.init_app(app)


@app.route('/')
def get_time():
    return {
        'Name':"geek", 
        "Age":"22",
        "Date": datetime.datetime.now(),
        "programming":"python"
        }

@app.route('/trades')
def show_trades():
    
    
@app.route('/{employee_id}')
def show_profile():
    
    
if __name__ == '__main__':
    app.run(debug=True)