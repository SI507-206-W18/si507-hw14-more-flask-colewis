from flask import Flask, render_template, request, redirect
import model
import json

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/admin") #, methods=["POST"])
def admin():
    #model.delete_instance()
    return render_template("admin.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")

@app.route("/delete", methods=["DELETE"])
def delete_entry():
    model.delete_entry(request.form['id'])
    return redirect('/admin')

if __name__=="__main__":
    model.init()
    app.run(debug=True)
