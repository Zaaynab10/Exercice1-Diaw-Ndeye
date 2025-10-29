class Todo:
    def __init__(self):
        self.todos = []
        self.id = 1

    def create(self, title):
        new_task = {"id": self.id, "title": title, "done": False}
        self.todos.append(new_task)
        self.id += 1
        return new_task

    def get_all(self):
        return self.todos

    def completed(self, id, done):
        for task in self.todos:
            if task["id"] == id:
                task["done"] = done
                return task
        return None

    def delete(self, id):
        for task in self.todos:
            if task["id"] == id:
                self.todos.remove(task)
                return task
        return None
