# Movies:
# Actors:
#  -name, category
# Settings:
# Genre:
# Runtime:
# Title:
# Cast:

# movies_to_actors, a new attibute:
# my_movie, Kashif - Earl
# my_movie, Chico -Zeke

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask, render_template
app = Flask(__name__)

# app.config.update(dict(SECRET_KEY="ABC"))

print("Hello world!!!!!")


# app = Flask(__name__)

# Declair a DB
# initialize a DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sqlite.db'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)

# Define a
    def __repr__(self):
        return '<Title %r>' % self.title


# Declair admin
admin = Admin(app, name ='movielog', template_mode='bootstrap3')

# Created an object
admin.add_view(ModelView(Movies, db.session))

class


@app.route('/')
def home():
    print("Hello world!!!!!")
    return render_template('home.html', hellohello="how's everything?")


if __name__ == '__main__':
    app.run(debug=True)

