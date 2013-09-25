#!/usr/bin/python2

# For web.py
import web

# User-created modules
import db

## Webpy Variables
urls = (
    '/', 'main.Index',
    '/view/(\d+)', 'main.View',
    '/delete/(\d+)', 'main.Delete',
    '/edit/(\d+)', 'main.Edit'
)

app = web.application(urls, globals(), autoreload=False)
