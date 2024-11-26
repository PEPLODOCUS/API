from flask import Flask, jsonify, request

app = Flask(__name__)

# Data (usually you'd use a database here)
tasks = [
    {'id': 1, 'title': 'Buy groceries', 'done': False},
    {'id': 2, 'title': 'Do laundry', 'done': False}
]

@app.route('/')
def home():
    return "Welcome to the REST API"
# GET - Fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# GET - Fetch a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

# POST - Create a new taskoo
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': new_task['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# PUT - Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    updated_task = request.get_json()
    task['title'] = updated_task.get('title', task['title'])
    task['done'] = updated_task.get('done', task['done'])
    return jsonify({'task': task})

# DELETE - Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
