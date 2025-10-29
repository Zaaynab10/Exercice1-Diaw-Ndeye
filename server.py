import json

from flask import Flask
from Routes.TodoRoutes import todo_bp  
app = Flask(__name__)
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)