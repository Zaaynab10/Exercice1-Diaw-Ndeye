from Controller.TodoController import TodoController
from Model.TodoModel import Todo

class Router:
    def __init__(self):
        self.controller = TodoController(Todo())

    def handle(self, method, path, data=None):
        if method == "GET" and path == "/todos":
            return self.controller.get_all()

        elif method == "POST" and path == "/todos":
            return self.controller.create(data)

        elif method == "PATCH" and path.startswith("/todos/"):
            try:
                id = int(path.split("/")[2])
                return self.controller.update(id, data)
            except:
                return {"status": 400, "error": "ID invalide"}

        elif method == "DELETE" and path.startswith("/todos/"):
            try:
                id = int(path.split("/")[2])
                return self.controller.delete(id)
            except:
                return {"status": 400, "error": "ID invalide"}

        return {"status": 404, "error": "Route non trouvée"}
