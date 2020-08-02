#! /usr/bin/python3

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/FLASKAPPS/")
from BlogApp.WebBlogApp import app as application
# application.secret_key = 'Add your secret key'
