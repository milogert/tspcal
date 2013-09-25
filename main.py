#!/usr/bin/python2

import web

import config
import model
from view import render as render
from datetime import date

class Index:

    def GET(self):
        """Show index."""
        d = date
        return render.index(d)

config.app.internalerror = web.debugerror
#application = config.app.wsgifunc()

if __name__ == '__main__':
    config.app.run()
