from flask import Flask, redirect, url_for, render_template
import datetime
import query

app = Flask(__name__)


@app.route('/')
def get_time():
    return render_template("index.html")
    # if query.emailExistsInUsers(email):
    #     return redirect(url_for("trades"))


# @app.route('/trades')
# def show_trades():
    
    
# @app.route('/{employee_id}')
# def show_profile():
    
    
if __name__ == '__main__':
    app.run(debug=True)