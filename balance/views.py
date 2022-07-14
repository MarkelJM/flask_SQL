from datetime import date

from flask import flash, render_template, redirect, request, url_for

from . import app
from .forms import MovimientosForm
from .models import DBManager


RUTA = 'data/balance.db'


@app.route("/")
def inicio():
    """
    Muestra la lista de movimientos cargados.
    """
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return render_template("nuevo.html")


@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    if request.method == "GET":
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimientoPorId(id)

        movimiento["fecha"] = date.fromisoformat(movimiento["fecha"])

        formulario = MovimientosForm(data=movimiento)
        return render_template("form_movimiento.html", form=formulario, id=id)

    elif request.method == "POST":
        form = MovimientosForm(data=request.form)
        if form.validate():
            db = DBManager(RUTA)
            consulta = "UPDATE movimientos SET cantidad=?, concepto=?, tipo=?, fecha=? WHERE id=?"
            params = (
                form.cantidad.data,
                form.concepto.data,
                form.tipo.data,
                form.fecha.data,
                form.id.data)
            resultado = db.consultaConParametros(consulta, params)
            if resultado:
                flash("Movimiento actualizado correctamente ;)", category="exito")
                return redirect(url_for("inicio"))
            return render_template("form_movimiento.html", form=form, id=id, errores=["Ha fallado la operación de guardar en la base de datos"])
        else:
            return render_template("form_movimiento.html", form=form, id=id, errores=["Ha fallado la validación de los datos"])


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db = DBManager(RUTA)
    consulta = "DELETE FROM movimientos WHERE id=?"
    params = (id,)
    esta_borrado = db.consultaConParametros(consulta, params)
    return render_template("borrar.html", resultado=esta_borrado)