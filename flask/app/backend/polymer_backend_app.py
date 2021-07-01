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
from oauth2client import client, crypt

CLIENT_ID='243774406021-jeqdr97jl8kl4dvhhpqtqrbt9kjfqqs9.apps.googleusercontent.com'

class PolymerBackendApp(flask.Flask):
    def __init__(self, **kwargs):
        super(PolymerBackendApp, self).__init__(__name__, **kwargs)
        self.add_url_rule('/', 'index', self.index, methods=('GET', 'POST', ))

    def index(self):
        token = flask.request.form['idtoken']

        try:
            idinfo = client.verify_id_token(token, CLIENT_ID)
            
            # Or, if multiple clients access the backend server:
            #idinfo = client.verify_id_token(token, None)
            #if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #    raise crypt.AppIdentityError("Unrecognized client.")
            
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
            
            # If auth request is from a G Suite domain:
            #if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #    raise crypt.AppIdentityError("Wrong hosted domain.")
        except crypt.AppIdentityError:
                # Invalid token
            print("invalid token")
        userid=idinfo['sub']
        print(idinfo)
        print("userid=%s", userid)
        return flask.Response('OK', status=200)
