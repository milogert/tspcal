#!/usr/bin/python2

import web

import config
import model
from view import render as render
from datetime import date
import calendar

class Index:

    def GET(self):
        """Show index."""
        date_obj = date
        today = date.today()
        # Make Sunday the first day.
        cal = calendar
        return render.index(date_obj, today, cal)

config.app.internalerror = web.debugerror
#application = config.app.wsgifunc()

if __name__ == '__main__':
    config.app.run()
