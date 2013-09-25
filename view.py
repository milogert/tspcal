# Python-native modules
import os

# For web.py
import web

# User-created modules
import config
import model

# Template Functions
# Wrapper for string cast.
def t_str(the_int):
    return str(the_int)


def t_type(o):
    return type(o)

# Template Globals
# Add functions and variables that you need to access in the templates
t_globals = {
    'datestr': web.datestr,
    'str': t_str,
    'type': t_type
}

render = web.template.render(
    os.path.join(os.path.dirname(__file__), 'templates/'),
    cache=False,
    base='a_base',
    globals=t_globals
)
render._keywords['globals']['render'] = render
