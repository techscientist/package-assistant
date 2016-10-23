""" 
[fTerm] assistant.py

This package provides useful assistant commands.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303


synonyms = {
    "whatstheweather":"weather",
    }

def weather(cityname):
    """Return wttr.in's weather forecast."""
    return "curl -4 http://wttr.in/%s" % (cityname)
