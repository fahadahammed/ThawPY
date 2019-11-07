#  Project ThawPY is developed by Fahad Ahammed on 11/7/19, 4:40 PM.
#
#  Last modified at 11/7/19, 4:33 PM.
#
#  Github: fahadahammed
#  Email: obak.krondon@gmail.com
#
#  Copyright (c) 2019. All rights reserved.

import datetime
import pytz
import os
import sys
import json
import jinja2


class Thaw:
    def __init__(self, site_source=None):
        self.time_zone = "Asia/Dhaka"
        self.site_source = "./thaw/templates"

    def list_of_files(self):
        to_return = []
        for root, dirs, files in os.walk(self.site_source):
            for filename in files:
                to_return.append(filename)
        return to_return

    def generate_html(self):
        title = "Thaw Site Generator !"
        user_name = "Fahad Ahammed"
        templateLoader = jinja2.FileSystemLoader(searchpath=self.site_source)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = "page.html"
        template = templateEnv.get_template(TEMPLATE_FILE)
        outputText = template.render(site_title=title, user_name=user_name)  # this is where to put args to the template renderer

        return outputText


if __name__ == "__main__":
    # print(Thaw().list_of_files())
    print(Thaw().generate_html())