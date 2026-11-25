from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/todos")
def list_todos():
    return jsonify(todos)

@app.post("/todos")
def add_todo():
    todo = {"id": len(todos) + 1, "title": request.json.get("title", "")}
    todos.append(todo)
    return jsonify(todo), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
