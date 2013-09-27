#!/usr/bin/python2

import sys
sys.path.append("/home/tsp/code")

import web

import config
import model
from view import render as render
from datetime import date
import calendar


class Index:

    def GET(self, day=date.today()):
        """Show index."""
        today = date.today()
        raise web.seeother("/" + str(today.year) + "/" + str(today.month))
        
        
class View:

    def GET(self, year, month):
        """Shows different month and year view."""
        date_obj = date
        cal = calendar
        year = int(year)
        month = int(month)
        
        # Reset the month and year based on going too high or too low.
        if month is 13:
            raise web.seeother("/" + str(year + 1) + "/1")
        elif month is 0:
            raise web.seeother("/" + str(year - 1) + "/12")
        
        return render.index(date_obj, cal, year, month, model.get_events())


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
