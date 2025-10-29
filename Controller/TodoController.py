
class TodoController:
    def __init__(self, todo_model):
        self.todo_model = todo_model

    def get_all(self):
        try:
            tasks = self.todo_model.get_all()
            return {"status": 200, "data": tasks}
        except Exception as error:
            print("Erreur TodoController.get_all:", error)
            return {"status": 500, "error": "Erreur serveur"}

    def create(self, title):
        try:
            if not title:
                return {"status": 400, "error": "Le titre de la tâche est requis"}
            
            task = self.todo_model.create(title)
            return {"status": 201, "data": task}
        except Exception as error:
            print("Erreur TodoController.create:", error)
            return {"status": 500, "error": "Erreur serveur"}

    def completed(self, id, done):
        try:
            if id is None or done is None:
                return {"status": 400, "error": "L'id et le statut sont requis"}

            task = self.todo_model.completed(id, done)
            if not task:
                return {"status": 404, "error": "Tâche non trouvée"}

            return {"status": 200, "data": task}
        except Exception as error:
            print("Erreur TodoController.completed:", error)
            return {"status": 500, "error": "Erreur serveur"}

    def delete(self, id):
        try:
            if id is None:
                return {"status": 400, "error": "L'id est requis"}

            task = self.todo_model.delete(id)
            if not task:
                return {"status": 404, "error": "Tâche non trouvée"}

            return {"status": 200, "message": "Tâche supprimée", "data": task}
        except Exception as error:
            print("Erreur TodoController.delete:", error)
            return {"status": 500, "error": "Erreur serveur"}
 