#!/usr/bin/env python3
'''Mock logging in'''


from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''check if locale is present and supported'''
    requested_locale = request.args.get('locale')
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    if hasattr(g, 'user') and g.user and 'locale' in g.user and
    g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.accept_languages.best_match
    (app.config['LANGUAGES'])
    if header_locale:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user(user_id):
    '''returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed'''
    return users.get(user_id)


@app.before_request
def before_request():
    '''use get_user to find a user if any,
    and set it as a global on flask.g.user'''
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def index():
    '''route'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
