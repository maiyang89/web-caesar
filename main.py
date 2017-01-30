#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2, caesar, cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Caesar</title>
</head>
<body>
    <h1>Web Caesar</h1>
"""

form = """
        <form method="post">
            <label>Rotate By:
                <input type="text" name="rotation">
            </label>
            <br>
            <p>
                Type a message:
            </p>
            <textarea name="text" style="height: 100px; width: 400px;"></textarea>
            <br>
            <input type="submit">
        </form>
    """

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_header + form + page_footer)

    def post(self):
        text = self.request.get("text")
        rotation = int(self.request.get("rotation"))
        userentry = caesar.encrypt(text,rotation)

        updated_form = """
            <form method="post">
                <label>Rotate By:
                    <input type="text" name="rotation">
                </label>
                <br>
                <p>
                    Type a message:
                </p>
                <textarea name="text" style="height: 100px; width: 400px;">""" + cgi.escape(userentry) + """</textarea>
                <br>
                <input type="submit">
            </form>
        """

        self.response.write(page_header + updated_form + page_footer)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
