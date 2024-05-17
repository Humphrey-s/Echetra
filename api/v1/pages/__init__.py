#!/usr/bin/python3
from flask import Blueprint

app_pages = Blueprint('app_pages', __name__, url_prefix="/")


#from api.v1.pages.login import *
from api.v1.pages.hackathons import *
from api.v1.pages.project import *
from api.v1.pages.task import *
