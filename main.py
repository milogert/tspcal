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
        return render.index(date_obj, today, cal, model.get_events())


class New:

    def GET(self):
        """Insert a new event."""
        return render.new()

    def POST(self):
        input = web.input()

        if not input["title"] or not input["date"] or not input["time"]:
            raise web.seeother("/new")

        model.new_event(input)
        raise web.seeother("/")


class Delete:

    def GET(self, id):
        """Delete an event with the given id."""
        model.delete_event(id)
        raise web.seeother("/")


config.app.internalerror = web.debugerror
#application = config.app.wsgifunc()

if __name__ == '__main__':
    config.app.run()
