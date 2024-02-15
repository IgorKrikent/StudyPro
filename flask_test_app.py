from flask import Flask, render_template
from forms import ContactForm
from models import db, User

app = Flask(import_name=__name__, template_folder="templates")

app.config['SECRET_KEY'] = 'some_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)


@app.route('/')
def home():
    """Home page"""

    return render_template('home.HTML', title='Home')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    """Create a form with 'name' fild,
    when form submitted - add user in database and return 'hello_user' template"""

    form = ContactForm()

    if form.validate_on_submit():

        user = User(name=form.name.data)

        db.session.add(user)
        db.session.commit()

        return render_template('hello_user.HTML', title='Glad to see you', user=user)

    return render_template('welcome.HTML', title='Welcome', form=form)


@app.route('/all_users')
def view_all_users():
    """Find all users"""

    users = User.query.all()

    return render_template('all_users.HTML', title='All users', users=users)


if __name__ == '__main__':

    with app.app_context():

        db.create_all()

    app.run(port=9999, debug=True)
