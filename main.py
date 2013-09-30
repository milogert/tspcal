#!/usr/bin/python2

import sys

import web

import config
import model
from view import render as render
from datetime import date
import time
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

        events = model.get_month_events(year, month)
        return render.index(date_obj, cal, year, month, events)


class Day:

    def GET(self, year, month, day):
        """Zooms in on a specific day."""
        year = int(year)
        month = int(month)
        day = int(day)
        cal = calendar

        # Reset the day/month/year if they go too high or too low.
        if month is 13:
            raise web.seeother("/" + str(year + 1) + "/1/1")
        elif month is 0:
            raise web.seeother("/" + str(year - 1) + "/12/31")

        events = model.get_day_events(year, month, day)
        return render.day(year, month, day, cal, events)


class New:

    def GET(self):
        """Insert a new event."""
        return render.new()

    def POST(self):
        input = web.input()

        input["starttime"] = time.strptime(input["starttime"] + ":00", "%H:%M:%S")

        if not input["title"] or not input["date"] or not input["starttime"] or not input["endtime"] or input["starttime"] <= input["endtime"]:
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
