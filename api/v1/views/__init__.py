#!/usr/bin/python3
from flask import Blueprint

all_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.status import *
from api.v1.views.users import *
from api.v1.views.restaurants import *
from api.v1.views.foods import *
from api.v1.views.reviews import *
