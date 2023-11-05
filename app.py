from flask import Flask, redirect, url_for, render_template, request
import datetime
import query

app = Flask(__name__)

@app.route('/trades')
def show_trades():
    return "hello world"
    
@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["username"]
        id = query.get_id_from_email(email)
        if id:
            print(id)
            return redirect(url_for("show_trades"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    
@app.route('/')
def reroute():
    return render_template("login.html") #redirect(url_for("login"))



    
    
# @app.route('/{employee_id}')
# def show_profile():
    
    
if __name__ == '__main__':
    app.run(debug=True)