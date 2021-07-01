#
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask

import common.flask.auth as auth


class Routes(object):
    """
    Class with base route definitions, responsible for registration of base
    routes and additional module blueprints.
    """
    def __init__(self, oauth2=auth.oauth2, redirect=flask.redirect,
                 render_template=flask.render_template, request=flask.request,
                 Response=flask.Response, session=flask.session,
                 url_for=flask.url_for):
        # Dependency injection
        self.oauth2 = oauth2
        self.redirect = redirect
        self.render_template = render_template
        self.request = request
        self.Response = Response
        self.session = session
        self.url_for = url_for
        self.add_url_rule('/', 'upload', self.upload, methods=('GET', 'POST', ))
    def index(self):
        """
        Homepage.
        """
        return self.Response('OK', status=constants.HTTP_OK)
