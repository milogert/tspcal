#!/usr/bin/python2

# Web.py
import web

# Normal database for operations on the data this pertains to.
data = web.database(
    host='milogert.com',
    port=3306,
    dbn='mysql',
    db='tsp',
    user='tsp',
    pw='tsp'
)
