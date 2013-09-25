#!/usr/bin/python2

import web

import config
import form
import model
from view import render as render

class Index:

    def GET(self):
        """Show index."""
        return render.index()

config.app.internalerror = web.debugerror
#application = config.app.wsgifunc()

if __name__ == '__main__':
    config.app.run()
