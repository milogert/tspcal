#!/usr/bin/python2

import datetime

import web

import db


def delete_event(id):
    """Deletes event with the given id."""
    db.data.delete("events", where="id=$id", vars=locals())


def get_day_events(year, month, day):
    """Gets events for a specific day."""
    return list(db.data.select(
            "events",
            where="year=$year AND month=$month AND day=$day",
            order="time ASC",
            vars=locals()
    ))


def get_events():
    """Gets all events."""
    return list(db.data.select("events", order="date ASC"))


def get_month_events(year, month):
    """Gets month events."""
    return list(db.data.select(
            "events",
            where="year=$year AND month=$month",
            order="date ASC",
            vars=locals()
    ))


def new_event(input):
    """Inserts a new event into the events table."""
    dates = input["date"].split("-")
    db.data.insert(
            "events",
            title=input["title"],
            year=dates[0],
            month=dates[1],
            day=dates[2],
            date=input["date"],
            starttime=input["startTime"],
            endtime=input["endTime"],
            location="" if not input["location"] else input["location"],
            details="" if not input["details"] else input["details"]
    )