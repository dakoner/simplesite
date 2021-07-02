import flask
import logging
from oauth2client import client, crypt

CLIENT_ID = '243774406021-jeqdr97jl8kl4dvhhpqtqrbt9kjfqqs9.apps.googleusercontent.com'
logging.basicConfig(level=logging.DEBUG)


class AuthApp(flask.Flask):

    def __init__(self, **kwargs):
        super(AuthApp, self).__init__(__name__, **kwargs)
        self.add_url_rule("/", view_func=self.index)
        self.add_url_rule("/auth", view_func=self.auth, methods=['POST'])

    def index(self):
        return flask.redirect(flask.url_for('static', filename='index.html'))

    def auth(self):
        token = flask.request.form['idtoken']

        try:
            idinfo = client.verify_id_token(token, CLIENT_ID)
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")

            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #    raise crypt.AppIdentityError("Wrong hosted domain.")
        except crypt.AppIdentityError:
            # Invalid token
            print("invalid token")
        userid = idinfo['sub']
        print("idinfo=%s" % idinfo)
        print("userid=%s" % userid)
        return flask.Response(idinfo['name'], status=200)


def create_app():
    app = AuthApp()
    return app


app = create_app()
