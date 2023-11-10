# app.py
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class RegistrationForm(FlaskForm):
    email = EmailField('Email')
    username = StringField('Nome de Usuário')
    password = PasswordField('Senha')
    submit = SubmitField('Cadastrar')

    def validate_email(self, field):
        if '@' not in field.data:
            raise ValidationError('Por favor, insira um email válido.')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        return 'Usuário {} cadastrado com sucesso!'.format(username)
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
