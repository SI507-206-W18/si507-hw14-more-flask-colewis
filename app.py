from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model.get_entries())

@app.route("/admin", methods=["POST"])
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

@app.route("/delete_entry", methods=["POST"])
def delete_entry():
    pass
    # model.
    # db = get_db()
    # db.execute('delete from entries where id = ?'[request.form['entry_id']])
    # db.commit()
    # flash('Entry deleted')
    # return redirect(url_for('show_entries'))

if __name__=="__main__":
    model.init()
    app.run(debug=True)
