gettext = lambda s: s
"""
excerpt from a typical django settings file
"""

# some includes
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# some comments
# Lorem ipsum dolor sit

# Find an replace this one!
SECRET_KEY = "REPLACEME"

# But ignore all other lines like these
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# also be able to handle such things:

SECRET_KEY = "REPLACEME"
SECRET_KEY='REPLACEME WAS JUST USED AS A PLACEHOLDER' #single quoted
  SECRET_KEY = "actually every line that is a string assignment to SECRET_KEY will be replaced" #indented with spaces
	SECRET_KEY = "see! also this one cool ay?!?" # indented with tab
