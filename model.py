#!/usr/bin/python2

import datetime

import web

import db


def get_events():
    """Gets all events."""
    return list(db.data.select("events", order="date ASC"))


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
            time=input["time"],
            location="" if not input["location"] else input["location"],
            details="" if not input["details"] else input["details"]
    )