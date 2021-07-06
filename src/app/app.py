import flask
import logging

logging.basicConfig(level=logging.DEBUG)

class App(flask.Flask):

    def __init__(self, **kwargs):
        super(App, self).__init__(__name__, **kwargs)
        self.add_url_rule("/", view_func=self.index)

    def index(self):
        return flask.redirect(flask.url_for('static', filename='index.html'))

app = App()
