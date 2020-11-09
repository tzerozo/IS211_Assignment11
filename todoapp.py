#!/usr/bin/env python
# coding: utf-8
# Lang Tuang | Week11 | 11/09/2020 


from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)

todolist = []



@app.route('/')
def tdl():
    return render_template('index.html')



@app.route('/submit', methods = ['POST'])
def submit():
    task    = request.form['task']
    email   = request.form['email']   #had AttributeError: as i put request.email
    priority= request.form['priority']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not todo:
        return redirect('/')
    elif priority == 'priority':
        return redirect('/')
    else:
        todolist.append((task, priority, email))

    print (todolist)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todolist.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# **** IGNORE the followings ****
# (insert at top)
#class Tasks:
#   task     = None
#   email    = None
#   priority = None

# (replace if : under /submit)
#if not re.match (r'[^@]+@[^@]+\.[^@]+', email):
#    return render_template ('index.html', task=task)
#else:
#    task          = Tasks()
#    task.task     = todo
#    task.priority = priority
#    task.email    = email
#    todolist.append(task)
#    return render_template ('index.html', todolist = todolist)

   
   