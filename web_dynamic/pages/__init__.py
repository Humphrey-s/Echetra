from flask import Blueprint

app_pages = Blueprint("app_pages", __name__, url_prefix="/")

from web_dynamic.pages.login import *
from web_dynamic.pages.projects import *
