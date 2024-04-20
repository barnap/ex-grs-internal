import sys
import random

from dao import dao_user, db_utils, dao_conditions_info
import config
#
from utils import utils#, spotify_utils as helper
from flask import Response

from math import floor
from random import randint

sys.path.append('../')


def get_available_conditions():
    conditions = dao_conditions_info.get_conditions_info()
    random.shuffle(conditions)
    Agg = None
    Exp = None
    for condition in conditions:
        if int(condition["required"] > condition["assigned"]):
            Agg = condition["AGGREGATION"]
            Exp = condition["EXPLANATION"]
            break
    return Agg, Exp


def update_available_conditions(Agg, Exp):
    dao_conditions_info.increment_assigned_conditions_info(Agg, Exp)
    return None
