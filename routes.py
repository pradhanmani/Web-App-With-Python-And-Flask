from app import app, db
from flask import flash ,render_template, redirect , url_for , get_flashed_messages
from models import Task
from datetime import datetime , timezone
import forms 

@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.order_by(Task.id.asc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods = ["GET", "POST"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.now(timezone.utc))
        db.session.add(t)
        db.session.commit()
        flash("Task added to the database")
        return redirect(url_for("index"))
    return render_template("add.html", form = form)

    #FOR EDIT SECTION
@app.route('/edit/<int:task_id>',methods = ["GET", "POST"])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.now(timezone.utc)
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for("index"))
        
        form.title.data = task.title
        return render_template("edit.html", form=form, task=task, task_id=task.id)
    else:
        flash("Task Not Found")
    return redirect(url_for("index"))
          
    #FOR DELETE SECTION
@app.route('/deletet/<int:task_id>',methods = ["GET", "POST"])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task has been deleted")
            return redirect(url_for("index"))

        return render_template("delete.html", form=form, task_id=task.id, title=task.title)
    else:
        flash("Task Not Found")
    return redirect(url_for("index"))