from flask import Blueprint, request, jsonify
from Controller.TodoController import TodoController

from Model.TodoModel import Todo

todo_controller = TodoController(Todo())

todo_bp = Blueprint("todo_bp", __name__)

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    res = todo_controller.get_all()
    return jsonify(res), res["status"]

@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    res = todo_controller.create(data)
    return jsonify(res), res["status"]

@todo_bp.route("/todos/<int:id>", methods=["PATCH"])
def update_todo(id):
    data = request.json
    res = todo_controller.update(id, data)
    return jsonify(res), res["status"]

@todo_bp.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    res = todo_controller.delete(id)
    return jsonify(res), res["status"]
