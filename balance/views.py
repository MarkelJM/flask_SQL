
from . import app


@app.route("/")
def inicio():
    return "pagina de inicio"


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "crear movimeinto"


@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    return f"actualizar movimeinto con ID={id}"


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    return f"Eliminar movimiento con ID={id}"
