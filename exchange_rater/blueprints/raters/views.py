# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required


from exchange_rater.services.raters import

blueprint = Blueprint("rates", __name__, url_prefix="/api/v1/rates")


@blueprint.route("/exchanges")
@login_required
def rates():
    return dict()

