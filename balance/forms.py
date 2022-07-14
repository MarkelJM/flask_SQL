from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha", validators=[DataRequired(message="Debes introducir una fecha")])
    concepto = StringField(
        "Concepto", validators=[
            DataRequired("Debes escribir un concepto"),
            Length(min=3, max=25, message="Debe tener entre 3 y 25 caracteres")
        ])
    tipo = RadioField(
        choices=[("I", "Ingreso"), ("G", "Gasto")],
        validators=[DataRequired(message="¿Es un gasto o un ingreso?")]
    )
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debes especificar un número")])

    submit = SubmitField("Guardar", render_kw={ "class": "blue-button" })