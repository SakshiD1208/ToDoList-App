from flask import Flask, render_template, request

app = Flask(__name__)

# Sample tasks
tasks = [
    {'id': 1, 'name': 'Task 1', 'description': 'This is task 1', 'completed': False},
    {'id': 2, 'name': 'Task 2', 'description': 'This is task 2', 'completed': False},
    {'id': 3, 'name': 'Task 3', 'description': 'This is task 3', 'completed': False}
]

# Default user details
user_name = "Sakshi Dongare"
user_age = 22

@app.route('/', methods=['GET', 'POST'])
def home():
    global user_name, user_age
    if request.method == 'POST':
        # Update user name and age
        user_name = request.form['name']
        user_age = int(request.form['age'])
    
    return render_template('ToDoList.html', tasks=tasks, user_name=user_name, user_age=user_age)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        new_task = request.form['task']
        new_description = request.form['description']
        new_id = len(tasks) + 1  # Simple ID generation
        tasks.append({'id': new_id, 'name': new_task, 'description': new_description, 'completed': False})
    return render_template('ToDoList.html', tasks=tasks, user_name=user_name, user_age=user_age)

@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    task = next((item for item in tasks if item['id'] == id), None)
    if task:
        task['completed'] = not task['completed']  # Toggle completion status
    return render_template('ToDoList.html', tasks=tasks, user_name=user_name, user_age=user_age)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    global tasks
    tasks = [item for item in tasks if item['id'] != id]
    return render_template('ToDoList.html', tasks=tasks, user_name=user_name, user_age=user_age)

@app.route('/progress')
def progress():
    completed_tasks = sum(1 for task in tasks if task['completed'])
    total_tasks = len(tasks)
    percent = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    return render_template('progress.html', completed=completed_tasks, total=total_tasks, percent=percent, user_name=user_name, user_age=user_age)

if __name__ == "__main__":
    app.run(debug=True)
